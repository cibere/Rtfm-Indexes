# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class LaravelLivewireSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://laravel-livewire.com/favicon.ico",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=cec0554d960fa30b4b0b610f372a8636",
        "payload": {
            "hitsPerPage": 5,
            "facetFilters": ["version:2.x"],
            "indexName": "livewire-framework",
        },
    },
): ...


LaravelLivewireSearchAPI.build(__name__)
