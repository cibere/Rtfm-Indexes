# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
#     "requests==2.32.5",
# ]
# ///

from __future__ import annotations

import requests
from _base import BaseSyncParser, Entry
from msgspec import Struct, json


class HeaderEntry(Struct):
    level: int
    title: str
    slug: str
    link: str
    children: list[HeaderEntry]


class Response(Struct):
    key: str
    path: str
    title: str
    lang: str
    headers: list[HeaderEntry]


decoder = json.Decoder(type=Response)


class DataSecurityDocs(
    BaseSyncParser,
    file=__file__,
    base_url="https://docs.datasecurity.org",
    favicon_url="https://docs.datasecurity.org/images/favicon.png",
):
    def build_entries(
        self, headers: list[HeaderEntry], parents: list[str] | None = None
    ) -> dict[str, Entry]:
        if not headers:
            return {}

        parents = parents or []
        cache = {}

        for header in headers:
            parts = [header.title, *parents]
            label = " - ".join(parts)

            cache[label] = Entry(label, self / header.link)
            cache.update(self.build_entries(header.children, parts))

        return cache

    def build_cache(self) -> dict[str, Entry]:
        raw_content = requests.get(
            self / "assets/index.html-cf1f0bed.js", timeout=10
        ).content

        stripped = (
            raw_content.strip()
            .removeprefix(b"const e=JSON.parse('")
            .removesuffix(b"');export{e as data};")
        )
        data = decoder.decode(stripped)

        return self.build_entries(data.headers)


DataSecurityDocs.build(__name__)
