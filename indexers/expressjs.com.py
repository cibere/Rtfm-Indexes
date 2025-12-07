# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class ExpressJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://expressjs.com/images/favicon.png",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=7164e33055faa6ecddefd9e08fc59f5d",
        "payload": {
            "params": "hitsPerPage=5&facetFilters=%5B%22lang%3Aen%22%5D",
            "indexName": "expressjs",
        },
    },
): ...


ExpressJsSearchAPI.build(__name__)
