# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class EsLintSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://eslint.org/icon.svg",
    options={
        "url": "https://l633p0c2ir-dsn.algolia.net/1/indexes/eslint/query?x-algolia-agent=Algolia for JavaScript (4.22.1); Browser (lite)&x-algolia-api-key=bb6bbd2940351f3afc18844a6b06a6e8&x-algolia-application-id=L633P0C2IR",
        "payload": {"facetFilters": ["tags:docs"]},
    },
): ...


EsLintSearchAPI.build(__name__)
