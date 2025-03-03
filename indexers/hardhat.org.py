# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class HardHatSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://hardhat.org/favicon.ico",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.13.0); Browser (lite); docsearch (3.0.0); docsearch-react (3.0.0)&x-algolia-api-key=70d2567dd1257c8a53bbb823a0085f02&x-algolia-application-id=BH4D9OD16A",
        "payload": {
            "indexName": "hardhat",
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
            "hitsPerPage": "20",
        },
    },
): ...


HardHatSearchAPI.build(__name__)
