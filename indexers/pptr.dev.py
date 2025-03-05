# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class PuppeteerSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://img.shields.io/npm/v/puppeteer.svg",
    options={
        "url": "https://dvky664lg7-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.14.2); Lite (5.14.2); Browser; docsearch (3.8.2); docsearch-react (3.8.2); docusaurus (3.6.3)&x-algolia-api-key=4dac1ae64b623f1d33ae0b4ce0ff16a4&x-algolia-application-id=DVKY664LG7",
        "payload": {
            "indexName": "pptr",
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
            "facetFilters": ["language:en", ["counter:1", "counter:2"]],
        },
    },
): ...


PuppeteerSearchAPI.build(__name__)
