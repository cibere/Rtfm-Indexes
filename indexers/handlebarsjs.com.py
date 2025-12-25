# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class SearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://handlebarsjs.com/images/favicon.png",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=ceae3bc4e38c4b10f99cc802d1e6db96",
        "payload": {
            "hitsPerPage": 5,
            "facetFilters": ["lang:en-US"],
            "indexName": "handlebarsjs",
        },
    },
): ...


SearchAPI.build(__name__)
