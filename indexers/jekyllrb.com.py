# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class JekllrbSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://jekyllrb.com/favicon.ico",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=50fe39c839958dfad797000f33e2ec17",
        "payload": {"indexName": "jekyllrb", "hitsPerPage": 5},
    },
): ...


JekllrbSearchAPI.build(__name__)
