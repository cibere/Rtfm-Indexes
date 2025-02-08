from __future__ import annotations

from typing import Iterator, Any, TypeVar, Awaitable

import bs4
import asyncio

from aiohttp import ClientSession
from yarl import URL

MISSING: Any = object()

T = TypeVar("T")


def _remove_all_instances(iter: list[T], value: T) -> list[T]:
    while value in iter:
        iter.remove(value)
    return iter


class VoidToolsParser:
    def __init__(self, session: ClientSession) -> None:
        self.session = session
        self.base_url = URL("https://www.voidtools.com")
        self.cache: dict[str, str] = {}

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
        async with self.session.get(self.base_url / url.lstrip("/")) as res:
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

            self.cache[" - ".join(_remove_all_instances([l3, l2, l1], MISSING))] = href

    async def start(self) -> None:
        checked_urls: list[str] = []
        tasks: list[Awaitable[None]] = []

        await self.parse_url("/support/everything")

        for key, url in self.cache.copy().items():
            if url not in checked_urls:
                tasks.append(self.parse_url(url))
                checked_urls.append(url)

        await asyncio.gather(*tasks)

    @classmethod
    async def async_start(cls) -> dict[str, str]:
        async with ClientSession() as cs:
            self = cls(cs)
            await self.start()
        return self.cache


def index():
    return {"voidtools.com": asyncio.run(VoidToolsParser.async_start())}
