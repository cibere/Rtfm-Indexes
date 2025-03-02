# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GatlingDocsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.gatling.io/favicon.ico",
    options={
        "url": "https://6pcib797p6-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.19.1); Browser (lite); docsearch (3.5.2); docsearch-react (3.5.2); docsearch.js (3.5.2)&x-algolia-api-key=e53c31a608bc353fc4c4a3694438886f&x-algolia-application-id=6PCIB797P6",
        "payload": {
            "indexName": "gatling",
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


GatlingDocsSearchAPI.build(__name__)
