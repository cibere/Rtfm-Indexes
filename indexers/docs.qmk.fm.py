# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4==4.13.1",
#     "msgspec==0.19.0",
#     "requests==2.32.3",
# ]
# ///

from __future__ import annotations

import re

import bs4
import requests
from _base import BaseSyncParser
from msgspec import Struct, json


class QmkLocalSearchField(Struct):
    title: str
    titles: list[str]


class QmkLocalSearchData(Struct):
    documentIds: dict[str, str]
    storedFields: dict[str, QmkLocalSearchField]


response_decoder = json.Decoder(type=QmkLocalSearchData)

THEME_FILE_PARSER_PATTERN = re.compile(r"([^\"]+VPLocalSearchBox[^\"]+)")
SEARCHBOX_FILE_PARSER_PATTERN = re.compile(r"([^\"]+localSearchIndexroot[^\"]+)")


class QmkDocs(
    BaseSyncParser,
    file=__file__,
    favicon="https://docs.qmk.fm/favicon.ico",
    base_url="https://docs.qmk.fm",
):
    def qmk_get_theme(self, text: bytes) -> list[str]:
        soup = bs4.BeautifulSoup(text.decode(), "html.parser")
        return [
            str(tag.attrs["href"])
            for tag in soup.find_all("link", rel="modulepreload")
            if isinstance(tag, bs4.Tag)
        ]

    def parse_index(self, filename: str) -> dict[str, str]:
        raw_content = requests.get(
            self / "assets" / "chunks" / filename, timeout=10
        ).content

        line = raw_content.splitlines()[0].decode()
        raw_json = (
            line.removesuffix("`;")
            .removeprefix("const _localSearchIndexroot = `")
            .replace("\\`", "`")
        )

        index = response_decoder.decode(raw_json)
        cache = {}

        for docid, field in index.storedFields.items():
            document = index.documentIds[docid]
            cache[field.title] = self / document

        return cache

    def find_match_from_url(self, *, url: str, pattern: re.Pattern[str]) -> str | None:
        raw_content = requests.get(self / url, timeout=10).content

        for match in pattern.finditer(raw_content.decode()):
            return match.group(0)

    def build_cache(self) -> dict[str, str]:
        raw_content = requests.get(self.base_url, timeout=10).content
        tags = self.qmk_get_theme(raw_content)

        for tag in tags:
            search_box_url = self.find_match_from_url(
                url=tag, pattern=THEME_FILE_PARSER_PATTERN
            )
            if search_box_url is None:
                continue
            index_name = self.find_match_from_url(
                url=search_box_url, pattern=SEARCHBOX_FILE_PARSER_PATTERN
            )
            if index_name is None:
                continue
            return self.parse_index(index_name.strip("/"))

        raise RuntimeError("Unable to find qmk index")


QmkDocs.build(__name__)
