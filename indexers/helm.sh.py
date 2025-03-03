# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class SearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://helm.sh/img/favicon-152.png",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=8bca76b0664b04581dc9f9854e844a90",
        "payload": {
            "indexName": "helm",
            "hitsPerPage": 5,
        },
    },
): ...


SearchAPI.build(__name__)
