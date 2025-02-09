# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4==4.13.1",
#     "msgspec==0.19.0",
#     "requests==2.32.3",
# ]
# ///

from __future__ import annotations

from typing import TYPE_CHECKING

import bs4
import requests
from _base import BaseSyncParser

if TYPE_CHECKING:
    from bs4._typing import _QueryResults


class LuaParser(
    BaseSyncParser, file=__file__, suffix="5.4", base_url="https://ss64.com"
):
    soup: bs4.BeautifulSoup

    def __init__(self) -> None:
        self.cache: dict[str, str] = {}

    def parse_atags(self, tags: _QueryResults) -> None:
        for tag in tags:
            if not isinstance(tag, bs4.Tag):
                continue

            href = tag.attrs.get("href")
            if href:
                self.cache[tag.get_text()] = self / href

    def parse_nav(self) -> None:
        container = self.soup.find_all("ul", class_="contents menubar")[0]
        if isinstance(container, bs4.Tag):
            self.parse_atags(container.find_all("a"))

    def parse_index(self) -> None:
        container = self.soup.find_all("table", class_="menubar")[0]
        if isinstance(container, bs4.Tag):
            self.parse_atags(container.find_all("a"))

    def build_cache(
        self,
    ) -> dict[str, str]:
        res = requests.get("https://www.lua.org/manual/5.4", timeout=10)
        self.soup = bs4.BeautifulSoup(res.content, "html.parser")
        self.parse_nav()
        self.parse_index()
        return self.cache


if __name__ == "__main__":
    LuaParser().build()
