# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class KnexJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    # favicon_url="",
    options={
        "url": "https://v7e3ehupd6-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.19.1); Browser (lite); docsearch (3.5.2); docsearch-react (3.5.2); docsearch.js (3.5.2)&x-algolia-api-key=44b5077836c1c8fba0f364383dde7fb4&x-algolia-application-id=V7E3EHUPD6",
        "payload": {
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
            "facetFilters": [],
            "indexName": "knex",
        },
    },
): ...


KnexJsSearchAPI.build(__name__)
