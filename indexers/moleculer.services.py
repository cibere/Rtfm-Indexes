# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class MoleculerServicesSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://moleculer.services/logo.svg",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=7d5514b7c3e161a428f04f33ba1bdab4",
        "payload": {
            "indexName": "moleculer",
            "hitsPerPage": 5,
            "facetFilters": ["version:0.14"],
        },
    },
): ...


MoleculerServicesSearchAPI.build(__name__)
