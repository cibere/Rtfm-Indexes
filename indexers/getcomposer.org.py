# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GetComposerSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://getcomposer.org/favicon.ico",
    options={
        "url": "https://dlyn25jsfj-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.8.5); Browser (lite); docsearch (3.0.0-alpha.41); docsearch-react (3.0.0-alpha.41); docsearch.js (3.0.0-alpha.41)&x-algolia-api-key=59b32c5fdb7d9198939d01eebcc4ecab&x-algolia-application-id=DLYN25JSFJ",
        "payload": {
            "indexName": "getcomposer",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20",
        },
    },
): ...


GetComposerSearchAPI.build(__name__)
