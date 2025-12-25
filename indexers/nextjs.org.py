# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class NextJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://nextjs.org/favicon.ico",
    options={
        "url": "https://nntahqi9c5-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.10.5); Browser (lite)&x-algolia-api-key=948b42d1edd177a55c6d6ae8dab24621&x-algolia-application-id=NNTAHQI9C5",
        "payload": {
            "indexName": "nextjs_docs_canary",
            "filters": "isApp:true",
        },
        "base_url": "https://nextjs.org",
    },
): ...


NextJsSearchAPI.build(__name__)
