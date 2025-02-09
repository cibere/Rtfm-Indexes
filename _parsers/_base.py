# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "msgspec==0.19.0"
# ]
# ///

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Self, TypeVar, overload

from msgspec import Struct, json

if TYPE_CHECKING:
    from types import TracebackType

    from flogin import ResultConstructorKwargs

parsers_dir = Path(__file__).parent
root = parsers_dir.parent
indexes_dir = root / "indexes"
indexes_dir.mkdir(exist_ok=True)

KwargsT = TypeVar("KwargsT", default=dict[str, Any])
type Cache = Mapping[str, str | Entry]


class UrlStr(str):
    def __truediv__(self, other: str) -> UrlStr:
        return UrlStr(self.rstrip("/") + "/" + other.lstrip("/"))


class _BaseParser[KwargsT]:
    name: ClassVar[str]
    suffix: str | None
    base_url: UrlStr | None

    @overload
    def __init_subclass__(
        cls, *, file: str, suffix: str, **kwargs: KwargsT
    ) -> None: ...
    @overload
    def __init_subclass__(cls, *, file: str, **kwargs: KwargsT) -> None: ...
    @overload
    def __init_subclass__(cls, **kwargs: KwargsT) -> None: ...

    def __init_subclass__(cls, **kwargs) -> None:
        file = kwargs.pop("file", None)
        suffix = kwargs.get("suffix")
        name = None

        if file:
            path = Path(file)
            name = path.name.removesuffix(".py")
        else:
            name = getattr(cls, "name", None)

        if suffix:
            if name:
                name += f"-{suffix}"
            if cls.base_url:
                cls.base_url = UrlStr(cls.base_url.replace("{SUF}", suffix))

        if name:
            cls.name = name

        if "base_url" in kwargs:
            kwargs["base_url"] = UrlStr(kwargs["base_url"])

        for key, value in kwargs.items():
            setattr(cls, key, value)

    def serialize_cache(self, cache: Cache) -> Cache:
        serialized = {}
        for key, value in cache.items():
            if isinstance(value, Entry):
                value.url.replace("%23", "#")
            else:
                value = value.replace("%23", "#")
            serialized[key] = value

        return serialized

    def _save(self, cache: Cache) -> None:
        file = indexes_dir / f"{self.name}.json"
        file.write_bytes(
            json.format(
                json.encode(
                    self.serialize_cache(cache),
                    enc_hook=lambda obj: str(obj)
                    if isinstance(obj, UrlStr)
                    else repr(obj),
                )
            )
        )
        print(f"Wrote to {file}")

    def __truediv__(self, piece: Any) -> UrlStr:
        return self.base_url / str(piece) if self.base_url else UrlStr(piece)


class BaseAsyncParser[KwargsT](_BaseParser[KwargsT]):
    async def build_cache(self) -> Cache:
        raise NotImplementedError

    async def start(self) -> None:
        async with self:
            self._save(await self.build_cache())

    @classmethod
    def build(cls) -> None:
        asyncio.run(cls().start())

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> bool:
        return False


class BaseSyncParser[KwargsT](_BaseParser[KwargsT]):
    def build_cache(self) -> Cache:
        raise NotImplementedError

    def start(self) -> None:
        with self:
            self._save(self.build_cache())

    @classmethod
    def build(cls) -> None:
        cls().start()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> bool:
        return False


class Entry(Struct):
    text: str
    url: str
    options: ResultConstructorKwargs | None = None
    ctx_menu_items: list[str] | None = None
