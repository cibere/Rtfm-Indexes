# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class MobxJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://badge.fury.io/js/mobx.svg",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript 3.21.0;docsearch.js 1.5.0&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=500db32fbdbd53a814f42aafdfa26bd4",
        "payload": {
            "indexName": "mobxjs",
            "hitsPerPage": 5,
        },
    },
): ...


MobxJsSearchAPI.build(__name__)
