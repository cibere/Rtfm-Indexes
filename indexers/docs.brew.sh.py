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
    favicon_url="https://docs.brew.sh/assets/img/homebrew.svg",
    options={
        "url": "https://d9hg3g8gs4-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.19.0); Lite (5.19.0); Browser; docsearch (3.9.0); docsearch-react (3.9.0); docsearch.js (3.9.0)&x-algolia-api-key=e3369d62b2366b374c54b2c5a2835a00&x-algolia-application-id=D9HG3G8GS4",
        "payload": {
            "indexName": "brew_all",
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
            "hitsPerPage": 20,
            "clickAnalytics": False,
            "facetFilters": ["site: docs"],
        },
    },
): ...


SearchAPI.build(__name__)
