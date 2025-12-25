# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class NetlifySearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.netlify.com/netlify-icon.svg",
    options={
        "url": "https://4rtnpm1qf9-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=4RTNPM1QF9&x-algolia-api-key=260466eb2466a36278b2fdbcc56ad7ba",
        "payload": {"indexName": "docs-manual", "hitsPerPage": 20},
    },
): ...


NetlifySearchAPI.build(__name__)
