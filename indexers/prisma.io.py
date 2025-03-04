# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class PrismaSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://www.prisma.io/docs/img/favicon.png",
    options={
        "url": "https://mf58ujz648-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.19.0); Lite (5.19.0); Browser; docsearch (3.8.3); docsearch-react (3.8.3); docusaurus (3.7.0)&x-algolia-api-key=fd3d0a05bfe5d280348060ca5ea416be&x-algolia-application-id=MF58UJZ648",
        "payload": {
            "indexName": "prisma",
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


PrismaSearchAPI.build(__name__)
