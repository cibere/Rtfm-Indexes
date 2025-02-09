# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "msgspec==0.19.0"
# ]
# ///

from __future__ import annotations

import asyncio
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Self, TypeVar, overload

from msgspec import Struct, msgpack

if TYPE_CHECKING:
    from types import TracebackType

    from flogin import ResultConstructorKwargs

FILE_EXT = "cidex"

parsers_dir = Path(__file__).parent
root = parsers_dir.parent
indexes_dir = root / "indexes_v2"
indexes_dir.mkdir(exist_ok=True)

KwargsT = TypeVar("KwargsT", default=dict[str, Any])
type Cache = Mapping[str, str | Entry]


class UrlStr(str):
    def __truediv__(self, other: str) -> UrlStr:
        return UrlStr(self.rstrip("/") + "/" + other.lstrip("/"))


class ParsedIndex(Struct, tag="index"):
    cache: Cache
    name: str
    favicon_url: str | None
    version: str = "2.0"


class VariantManifest(Struct, tag="variant-manifest"):
    variants: Iterable[str]
    version: str = "2.0"


class _BaseParser[KwargsT]:
    variant: ClassVar[str | None] = None
    file: ClassVar[str]
    _raw_base_url: ClassVar[str]
    favicon_url: ClassVar[str | None] = None

    @property
    def base_url(self) -> UrlStr:
        return UrlStr(self._raw_base_url.replace("{VAR}", self.variant or ""))

    @property
    def _filename(self) -> str:
        return Path(self.file).name.removesuffix(".py")

    @property
    def name(self) -> str:
        return self._filename + (f"-{self.variant}" if self.variant else "")

    @overload
    def __init_subclass__(cls, *, file: str, **kwargs: KwargsT) -> None: ...
    @overload
    def __init_subclass__(cls, **kwargs: KwargsT) -> None: ...

    def __init_subclass__(cls, **kwargs) -> None:
        if "base_url" in kwargs:
            kwargs["_raw_base_url"] = kwargs.pop("base_url")

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

    def save(self, cache: Cache) -> None:
        metadata = ParsedIndex(self.serialize_cache(cache), self.name, self.favicon_url)
        return self._save(metadata, self.name)

    @classmethod
    def _save(cls, data: Struct, filename: str) -> None:
        file = indexes_dir / f"{filename}.{FILE_EXT}"

        def enc_hook(obj: Any) -> Any:
            if isinstance(obj, UrlStr):
                return str(obj)
            return repr(obj)

        file.write_bytes(msgpack.encode(data, enc_hook=enc_hook))
        print(f"Wrote to {file}")

    def __truediv__(self, piece: Any) -> UrlStr:
        return self.base_url / str(piece) if self.base_url else UrlStr(piece)

    def _runner(self) -> None:
        raise NotImplementedError

    @classmethod
    def build(cls, *variations: str) -> None:
        if not variations:
            return cls()._runner()

        self = None
        for variant in variations:
            cls.variant = variant
            self = cls()
            self._runner()

        if self:
            data = VariantManifest(variations)
            self._save(data, self._filename)


class BaseAsyncParser[KwargsT](_BaseParser[KwargsT]):
    async def build_cache(self) -> Cache:
        raise NotImplementedError

    async def start(self) -> None:
        async with self:
            self.save(await self.build_cache())

    def _runner(self) -> None:
        asyncio.run(self.start())

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
            self.save(self.build_cache())

    def _runner(self) -> None:
        self.start()

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
