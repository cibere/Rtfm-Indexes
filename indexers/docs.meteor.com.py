# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class MeteorSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    # favicon_url="",
    options={
        "url": "https://2rbx3pr26i-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.14.2); Lite (5.14.2); Browser; docsearch (3.8.2); docsearch-react (3.8.2); docsearch.js (3.8.2)&x-algolia-api-key=7fcba92008b84946f04369df2afa1744&x-algolia-application-id=2RBX3PR26I",
        "payload": {
            "indexName": "meteor_docs_v3",
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
            "facetFilters": ["lang:en-US"],
        },
    },
): ...


MeteorSearchAPI.build(__name__)
