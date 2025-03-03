# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class NestJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.nestjs.com/assets/favicons/favicon-32x32.png",
    options={
        "url": "https://sdcbyan96j-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.19.0); Lite (5.19.0); Browser; docsearch (3.9.0); docsearch-react (3.9.0); docsearch.js (3.9.0)&x-algolia-api-key=6d1869890dab96592b191e63a8deb5b5&x-algolia-application-id=SDCBYAN96J",
        "payload": {
            "indexName": "nestjs",
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
        },
    },
): ...


NestJsSearchAPI.build(__name__)
