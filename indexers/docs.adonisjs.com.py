# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class AdonisSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.adonisjs.com/icons/favicon.svg",
    options={
        "url": "https://kxecyamex8-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.19.1); Browser (lite); docsearch (3.6.1); docsearch-react (3.6.1); docsearch.js (3.6.1)&x-algolia-api-key=01279e9ede105d87a1ade54565b1a2fd&x-algolia-application-id=KXECYAMEX8",
        "payload": {
            "indexName": "adonisjs_next",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20&clickAnalytics=false",
        },
    },
): ...


AdonisSearchAPI.build(__name__)
