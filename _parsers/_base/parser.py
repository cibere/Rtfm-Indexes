from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, ClassVar, Self

from ._types import Cache
from .indexer import BaseIndexer
from .structs import CacheIndex, Entry
from .utils import UrlStr

if TYPE_CHECKING:
    from types import TracebackType


class BaseParser[KwargsT](BaseIndexer[KwargsT]):
    _raw_base_url: ClassVar[str]

    @property
    def base_url(self) -> UrlStr:
        return UrlStr(self._raw_base_url.replace("{VAR}", self.variant or ""))

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
        metadata = CacheIndex(
            cache=self.serialize_cache(cache),
            name=self.name,
            favicon_url=self.favicon_url,
        )
        return self._save(metadata, self.name)

    def __truediv__(self, piece: Any) -> UrlStr:
        return self.base_url / str(piece) if self.base_url else UrlStr(piece)


class BaseAsyncParser[KwargsT](BaseParser[KwargsT]):
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


class BaseSyncParser[KwargsT](BaseParser[KwargsT]):
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
