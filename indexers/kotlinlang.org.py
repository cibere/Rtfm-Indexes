# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class KotlinLangSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://kotlinlang.org/assets/images/favicon.ico?v2=",
    options={
        "url": "https://7961pkyrxv-3.algolianet.com/1/indexes/prod_KOTLINLANG_WEBHELP/query?x-algolia-agent=Algolia for JavaScript (4.13.0); Browser",
        "payload": {
            "attributesToRetrieve": ["pageTitle", "url", "breadcrumbs", "mainTitle"],
            "attributesToSnippet": ["content:25"],
            "clickAnalytics": True,
            "facetFilters": ["product:help/kotlin-reference", "version:"],
            "hitsPerPage": 25,
            "snippetEllipsisText": "…",
            "typoTolerance": "min",
            "userToken": "405o01vjuhdlqf9cbxsoz",
        },
        "headers": {
            "x-algolia-api-key": "1bfad5fdbae302b33d844ed1b43ec4d5",
            "x-algolia-application-id": "7961PKYRXV",
        },
    },
): ...


KotlinLangSearchAPI.build(__name__)
