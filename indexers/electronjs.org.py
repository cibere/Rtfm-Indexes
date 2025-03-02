# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class ElectronJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://www.electronjs.org/assets/img/favicon.ico",
    options={
        "url": "https://mg3srmk3k0-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.14.2); Lite (5.14.2); Browser; docsearch (3.8.2); docsearch-react (3.8.2); docusaurus (3.7.0)&x-algolia-api-key=fdc2cf6080e499639d7e6b0278851ed4&x-algolia-application-id=MG3SRMK3K0",
        "payload": {
            "indexName": "electronjs",
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
                ["docusaurus_tag:default", "docusaurus_tag:docs-default-current"],
            ],
        },
    },
): ...


ElectronJsSearchAPI.build(__name__)
