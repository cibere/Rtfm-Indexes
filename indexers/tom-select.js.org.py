# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class TomSelectJs(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=662e3a3a9d206ebad6d19f341b85acbd",
        "payload": {"params": "query=te&hitsPerPage=20", "indexName": "tom-select"},
    },
): ...


TomSelectJs.build(__name__)
