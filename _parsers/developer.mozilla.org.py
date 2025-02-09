# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
#     "requests",
# ]
# ///
from __future__ import annotations

import msgspec
import requests
from _base import BaseSyncParser, Cache
from msgspec import json


class DocEntry(msgspec.Struct):
    url: str
    title: str


doc_entry_decoder = json.Decoder(type=list[DocEntry])


class MdnParser(
    BaseSyncParser,
    file=__file__,
    base_url="https://developer.mozilla.org",
    favicon_url="https://developer.mozilla.org/favicon.ico",
):
    def build_cache(self) -> Cache:
        raw_content = requests.get(
            self / "en-US" / "search-index.json", timeout=10
        ).content

        data = doc_entry_decoder.decode(raw_content)

        return {entry.title: self / entry.url for entry in data}


if __name__ == "__main__":
    MdnParser.build()
