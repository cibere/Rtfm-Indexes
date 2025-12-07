# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class KtorSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    # favicon_url="",
    options={
        "url": "https://ohiv241qet-dsn.algolia.net/1/indexes/prod_JETBRAINSCOM_HELP/query?x-algolia-agent=Algolia for JavaScript (4.13.0); Browser",
        "payload": {
            "attributesToRetrieve": ["pageTitle", "url", "breadcrumbs", "mainTitle"],
            "attributesToSnippet": ["content:25"],
            "clickAnalytics": True,
            "facetFilters": ["product:docs", "version:3.1.1"],
            "hitsPerPage": 25,
            "snippetEllipsisText": "…",
            "typoTolerance": "min",
            "userToken": "ih740sxaqn7foy5p6ncgj",
        },
        "headers": {
            "x-algolia-api-key": "8c2683cac2d71d547b55183297abb506",
            "x-algolia-application-id": "OHIV241QET",
        },
    },
): ...


KtorSearchAPI.build(__name__)
