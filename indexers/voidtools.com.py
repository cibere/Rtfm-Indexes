# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "aiohttp==3.11.17",
#   "beautifulsoup4==4.13.4",
#   "msgspec==0.19.0",
# ]
# ///

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Iterator
from types import TracebackType
from typing import Any, Self, TypeVar

import bs4
from _base import BaseAsyncParser, Cache, Entry, MutableCache
from aiohttp import ClientSession

MISSING: Any = object()

T = TypeVar("T")


def _remove_all_instances(iter: list[T], value: T) -> list[T]:
    while value in iter:
        iter.remove(value)
    return iter


class VoidToolsParser(
    BaseAsyncParser,
    file=__file__,
    base_url="https://www.voidtools.com",
    favicon_url="https://www.voidtools.com/favicon.ico",
):
    session: ClientSession
    cache: MutableCache

    def __init__(self) -> None:
        self.cache = {}

    def iter_toc(self, data: bytes) -> Iterator[tuple[int, str, str]]:
        """level, label, href"""

        soup = bs4.BeautifulSoup(data, "html.parser")

        toc = soup.find("div", class_="wikinav")
        assert isinstance(toc, bs4.Tag)

        for li in toc.find_all("li"):
            assert isinstance(li, bs4.Tag)

            atag = li.find("a")
            assert isinstance(atag, bs4.Tag)

            label = atag.get_text()
            href = str(atag["href"])
            level = int(str(li["class"]).strip("[]'qwertyuiopasdfghjklzxcvbnm"))
            yield level, label, href

    def get_toc(self, data: bytes) -> list[tuple[int, str, str]]:
        """level, label, href"""

        return list(self.iter_toc(data))

    async def parse_url(self, url: str) -> None:
        async with self.session.get(url) as res:
            data = await res.read()

        toc = await asyncio.to_thread(self.get_toc, data)
        l1 = MISSING
        l2 = MISSING
        l3 = MISSING

        for level, label, href in toc:
            match level:
                case 1:
                    l1 = label
                    l2 = l3 = MISSING
                case 2:
                    l2 = label
                    l3 = MISSING
                case 3:
                    l3 = label

            parts = _remove_all_instances([l3, l2, l1], MISSING)
            self.cache[parts[0]] = Entry(" - ".join(parts), self / href)

    async def build_cache(self) -> Cache:
        checked_urls: list[str] = []
        tasks: list[Awaitable[None]] = []

        await self.parse_url("https://www.voidtools.com/support/everything")

        for entry in self.cache.values():
            url = entry.url

            if url not in checked_urls:
                tasks.append(self.parse_url(url))
                checked_urls.append(url)

        await asyncio.gather(*tasks)
        return self.cache

    async def __aenter__(self) -> Self:
        self.session = ClientSession()
        await self.session.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> bool:
        await self.session.__aexit__(exc_type, exc_value, traceback)
        del self.session
        return False


VoidToolsParser.build(__name__)
