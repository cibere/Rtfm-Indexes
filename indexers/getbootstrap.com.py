# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from typing import Any

from _base import BaseAPI


class GetBootstrapSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://getbootstrap.com/docs/5.0/assets/img/favicons/favicon-32x32.png",
    options={
        "url": "",
        "payload": {
            "indexName": "bootstrap",
            "params": "hitsPerPage=5&facetFilters=%5B%22version%3A5.0%22%5D",
        },
    },
):
    def get_options(self) -> dict[str, Any]:
        return {
            "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=5990ad008512000bba2cf951ccf0332f",
            "payload": {
                "indexName": "bootstrap",
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
                "highlightPreTag": "<mark>",
                "highlightPostTag": "</mark>",
                "hitsPerPage": 20,
                "clickAnalytics": False,
                "facetFilters": [f"version:{self.variant}"],
            },
        }


GetBootstrapSearchAPI.build(
    __name__,
    "5.3",
    "5.2",
    "5.1",
    "5.0",
    "4.6",
    "4.5",
    "4.4",
    "4.3",
    "4.2",
    "4.1",
    "4.0",
)
