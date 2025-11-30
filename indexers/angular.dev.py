# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class AngularSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://angular.dev/assets/icons/favicon-32x32.png",
    options={
        "url": "https://l1xwt2uj7f-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.20.2); Lite (5.20.2); Browser&x-algolia-api-key=dfca7ed184db27927a512e5c6668b968&x-algolia-application-id=L1XWT2UJ7F",
        "payload": {
            "indexName": "angular_v17",
            "type": "default",
            "maxValuesPerFacet": 5,
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
            "hitsPerPage": 20,
            "snippetEllipsisText": "…",
            "highlightPreTag": "<ɵ>",
            "highlightPostTag": "</ɵ>",
            "attributesToHighlight": [],
            "attributesToSnippet": [
                "hierarchy.lvl1:10",
                "hierarchy.lvl2:10",
                "hierarchy.lvl3:10",
                "hierarchy.lvl4:10",
                "hierarchy.lvl5:10",
                "hierarchy.lvl6:10",
                "content:10",
            ],
        },
    },
): ...


AngularSearchAPI.build(__name__)
