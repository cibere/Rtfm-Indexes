# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class SearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://www.gatsbyjs.com/icons/icon-512x512.png?v=3ad5294f3fa6c06e2d07ab07c76df2cf",
    options={
        "url": "https://hq84ml84er-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.14.2); Browser (lite); docsearch (3.2.1); docsearch-react (3.2.1)&x-algolia-api-key=7b41e08b93bde09e5ced2e15fb5fa595&x-algolia-application-id=HQ84ML84ER",
        "payload": {
            "indexName": "gatsbyjs",
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
        },
    },
): ...


SearchAPI.build(__name__)
