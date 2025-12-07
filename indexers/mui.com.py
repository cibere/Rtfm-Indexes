# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class MuiSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://mui.com/static/favicon.ico",
    options={
        "url": "https://tzgz85b9tb-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.14.2); Lite (5.14.2); Browser; docsearch (3.8.2); docsearch-react (3.8.2)&x-algolia-api-key=8177dfb3e2be72b241ffb8c5abafa899&x-algolia-application-id=TZGZ85B9TB",
        "payload": {
            "indexName": "material-ui",
            "attributesToRetrieve": [
                "hierarchy.lvl0",
                "hierarchy.lvl1",
                "hierarchy.lvl2",
                "hierarchy.lvl3",
                "hierarchy.lvl4",
                "hierarchy.lvl5",
                "content",
                "type",
                "url",
                "productId",
                "productCategoryId",
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
            "hitsPerPage": 40,
            "clickAnalytics": False,
            "facetFilters": ["version:master", "language:en"],
            "optionalFilters": ["productId:material-ui"],
            "analyticsTags": ["language:en", "product:material-ui"],
        },
    },
): ...


MuiSearchAPI.build(__name__)
