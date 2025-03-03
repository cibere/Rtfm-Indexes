# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class IconicFrameworkSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://ionicframework.com/docs/img/meta/favicon-96x96.png",
    options={
        "url": "https://o9qsl985bs-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.20.0); Browser (lite); docsearch (3.5.2); docsearch-react (3.5.2); docusaurus (3.0.1)&x-algolia-api-key=ceb5366064b8fbf70959827cf9f69227&x-algolia-application-id=O9QSL985BS",
        "payload": {
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
            "indexName": "ionicframework",
        },
    },
): ...


IconicFrameworkSearchAPI.build(__name__)
