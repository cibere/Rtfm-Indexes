# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GradleSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.gradle.org/favicon.ico",
    options={
        "url": "https://6to4ytlgip-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.23.3); Browser (lite); autocomplete-core (1.18.1); autocomplete-js (1.18.1)&x-algolia-api-key=454eb4fae2f696182f30a284509468b3&x-algolia-application-id=6TO4YTLGIP",
        "payloads": [
            {
                "indexName": "gradledocs",
                "hitsPerPage": 5,
                "clickAnalytics": False,
                "userToken": "anonymous-af825cea-ff09-4c5e-96da-e64d34df032c",
                "filters": "type:content AND preference:1",
                "attributesToSnippet": [
                    "content:10",
                    "hierarchy.lvl1:5",
                    "hierarchy.lvl2:5",
                ],
                "attributesToHighlight": [
                    "content",
                    "hierarchy.lvl1",
                    "hierarchy.lvl2",
                ],
            },
            {
                "indexName": "gradledocs",
                "hitsPerPage": 2,
                "clickAnalytics": False,
                "userToken": "anonymous-af825cea-ff09-4c5e-96da-e64d34df032c",
                "filters": "type:content AND preference:2",
                "attributesToSnippet": [
                    "content:10",
                    "hierarchy.lvl1:5",
                    "hierarchy.lvl1:5",
                ],
                "attributesToHighlight": [
                    "content",
                    "hierarchy.lvl1",
                    "hierarchy.lvl2",
                ],
            },
            {
                "indexName": "gradledocs",
                "hitsPerPage": 2,
                "clickAnalytics": False,
                "userToken": "anonymous-af825cea-ff09-4c5e-96da-e64d34df032c",
                "filters": "type:content AND preference:3",
                "attributesToSnippet": [
                    "content:10",
                    "hierarchy.lvl1:5",
                    "hierarchy.lvl1:5",
                ],
                "attributesToHighlight": [
                    "content",
                    "hierarchy.lvl1",
                    "hierarchy.lvl2",
                ],
            },
            {
                "indexName": "gradledocs",
                "hitsPerPage": 2,
                "clickAnalytics": False,
                "userToken": "anonymous-af825cea-ff09-4c5e-96da-e64d34df032c",
                "filters": "type:content AND preference:4",
                "attributesToSnippet": [
                    "content:10",
                    "hierarchy.lvl1:5",
                    "hierarchy.lvl1:5",
                ],
                "attributesToHighlight": [
                    "content",
                    "hierarchy.lvl1",
                    "hierarchy.lvl2",
                ],
            },
        ],
    },
): ...


GradleSearchAPI.build(__name__)
