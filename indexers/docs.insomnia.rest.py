# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class InsomniaRestSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    # favicon_url="",
    options={
        "url": "https://ibxe7r5kfs-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=IBXE7R5KFS&x-algolia-api-key=65f451796f36a6d7df9814965f5de7ac",
        "payload": {"indexName": "insomnia_docs", "hitsPerPage": 8},
    },
): ...


InsomniaRestSearchAPI.build(__name__)
