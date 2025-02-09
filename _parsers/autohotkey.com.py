# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
#     "requests",
# ]
# ///
from __future__ import annotations

from typing import TYPE_CHECKING

import requests
from _base import BaseSyncParser, Cache
from msgspec import json

if TYPE_CHECKING:
    from collections.abc import Iterator


DATA_INDEX_URL = "https://raw.githubusercontent.com/AutoHotkey/AutoHotkeyDocs/refs/heads/v{0}/docs/static/source/data_index.js"
DATA_TOC_URL = "https://raw.githubusercontent.com/AutoHotkey/AutoHotkeyDocs/refs/heads/v{0}/docs/static/source/data_toc.js"
TocTree = list[tuple[str, str] | tuple[str, str, "TocTree"]]

decoder = json.Decoder()


class AutoHotkeyParser(
    BaseSyncParser,
    file=__file__,
    base_url="https://autohotkey.com/docs/v{SUF}",
    favicon_url="https://www.autohotkey.com/favicon.ico",
):
    def fetch_index(self) -> dict[str, str]:
        url = DATA_INDEX_URL.format(self.suffix)
        raw_content = requests.get(url, timeout=10).content

        content = (
            raw_content.decode().strip().removeprefix("indexData = ").removesuffix(";")
        )

        data: list[tuple[str, str] | tuple[str, str, int]] = decoder.decode(content)

        return {name: self / str(extra[0]) for name, *extra in data}

    def parse_toc(self, tree: TocTree) -> Iterator[tuple[str, str]]:
        for entry in tree:
            if len(entry) == 2:
                yield entry
            else:
                for key, value in self.parse_toc(entry[2]):
                    yield f"{key} - {entry[0]}", value

    def fetch_toc(self) -> dict[str, str]:
        url = DATA_TOC_URL.format(self.suffix)
        raw_content = requests.get(url, timeout=10).content

        content = (
            raw_content.decode().strip().removeprefix("tocData = ").removesuffix(";")
        )

        tree: TocTree = decoder.decode(content)

        return {name: self / url for name, url in self.parse_toc(tree)}

    def build_cache(self) -> Cache:
        return self.fetch_index() | self.fetch_toc()


class AutoHotkeyV2(AutoHotkeyParser, suffix="2"): ...


class AutoHotkeyV1(AutoHotkeyParser, suffix="1"): ...


if __name__ == "__main__":
    AutoHotkeyV1.build()
    AutoHotkeyV2.build()
