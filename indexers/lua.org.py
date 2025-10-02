# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4==4.14.0",
#     "msgspec==0.19.0",
#     "requests==2.32.5",
# ]
# ///

from __future__ import annotations

from typing import TYPE_CHECKING

import bs4
import requests
from _base import BaseSyncParser, Cache, Entry, MutableCache

if TYPE_CHECKING:
    from bs4._typing import _QueryResults


class LuaParser(
    BaseSyncParser,
    file=__file__,
    base_url="https://www.lua.org/manual/{VAR}",
    favicon_url="https://www.lua.org/favicon.ico",
):
    soup: bs4.BeautifulSoup

    def __init__(self) -> None:
        self.cache: MutableCache = {}

    def parse_atags(self, tags: _QueryResults) -> None:
        for tag in tags:
            if not isinstance(tag, bs4.Tag):
                continue

            href = tag.attrs.get("href")
            if href:
                label = tag.get_text()
                self.cache[label] = Entry(label, self / href)

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
    ) -> Cache:
        res = requests.get("https://www.lua.org/manual/5.4", timeout=10)
        self.soup = bs4.BeautifulSoup(res.content, "html.parser")
        self.parse_nav()
        self.parse_index()
        return self.cache


LuaParser.build(__name__, "5.4")
