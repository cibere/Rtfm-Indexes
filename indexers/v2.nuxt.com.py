# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class NuxtSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://v2.nuxt.com/_nuxt/icons/icon_512x512.6dcbd4.png",
    options={
        "url": "https://1v8g7n9gf0-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.1.0); Browser (lite); docsearch (1.0.0-alpha.28); docsearch-react (1.0.0-alpha.28); docsearch.js (1.0.0-alpha.28); autocomplete-core (1.0.0-alpha.28)&x-algolia-api-key=60a01900a4b726d667eab75b6f337592&x-algolia-application-id=1V8G7N9GF0",
        "payload": {
            "indexName": "nuxtjs",
            "hitsPerPage": 20,
            "attributesToRetrieve": [
                "hierarchy.lvl0",
                "hierarchy.lvl1",
                "hierarchy.lvl2",
                "hierarchy.lvl3",
                "hierarchy.lvl4",
                "hierarchy.lvl5",
                "hierarchy.lvl6",
                "content",
                "type",
                "url",
            ],
            "attributesToSnippet": [
                "hierarchy.lvl1:10",
                "hierarchy.lvl2:10",
                "hierarchy.lvl3:10",
                "hierarchy.lvl4:10",
                "hierarchy.lvl5:10",
                "hierarchy.lvl6:10",
                "content:10",
            ],
            "snippetEllipsisText": "…",
            "facetFilters": ["language:en-US", "tags:main"],
        },
    },
): ...


NuxtSearchAPI.build(__name__)
