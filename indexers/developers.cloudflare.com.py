# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class CloudflareSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://developers.cloudflare.com/favicon.png",
    options={
        "url": "https://d32wiyftuf-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.14.2); Lite (5.14.2); Browser; docsearch (3.8.2); docsearch-react (3.8.2); docsearch.js (3.8.2)&x-algolia-api-key=5cec275adc19dd3bc17617f7d9cf312a&x-algolia-application-id=D32WIYFTUF",
        "payload": {
            "indexName": "prod_devdocs",
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


CloudflareSearchAPI.build(__name__)
