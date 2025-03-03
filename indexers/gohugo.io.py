# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GohugoSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://gohugo.io/favicon-32x32.png",
    options={
        "url": "https://d1bplzhgyq-dsn.algolia.net/1/indexes/*/queries",
        "payload": {
            "indexName": "hugodocs",
            "attributesToHighlight": ["hierarchy", "content"],
            "attributesToRetrieve": ["hierarchy", "url", "content"],
        },
        "headers": {
            "X-Algolia-API-Key": "6df94e1e5d55d258c56f60d974d10314",
            "X-Algolia-Application-Id": "D1BPLZHGYQ",
        },
    },
): ...


GohugoSearchAPI.build(__name__)
