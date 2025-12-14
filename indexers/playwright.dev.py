# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from typing import Any

from _base import BaseAPI


class PlayWrightSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://playwright.dev/python/img/playwright-logo.svg",
):
    def get_options(self) -> dict[str, Any]:
        return {
            "url": "https://k09icmcv6x-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.19.0); Lite (5.19.0); Browser; docsearch (3.8.3); docsearch-react (3.8.3); docusaurus (3.7.0)&x-algolia-api-key=a5b64422711c37ab6a0ce4d86d16cdd9&x-algolia-application-id=K09ICMCV6X",
            "payload": {
                "indexName": f"playwright-{self.variant}",
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
                "facetFilters": [
                    "language:en",
                    [
                        "docusaurus_tag:default",
                        "docusaurus_tag:docs-default-stable",
                        "docusaurus_tag:docs-community-current",
                    ],
                ],
            },
        }


PlayWrightSearchAPI.build(__name__, "nodejs", "python", "java", "dotnet")
