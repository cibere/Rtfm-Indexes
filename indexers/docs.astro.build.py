# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class AstroBuildSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.astro.build/favicon.svg",
    options={
        "url": "https://7afbu8epju-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.8.5); Browser (lite); docsearch (3.5.1); docsearch-react (3.5.1); docsearch.js (3.5.1)&x-algolia-api-key=4440670147c44d744fd8da35ff652518&x-algolia-application-id=7AFBU8EPJU",
        "payload": {
            "indexName": "astro",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20&clickAnalytics=true&facetFilters=%5B%5B%22lang%3Aen%22%5D%5D&attributesToHighlight=%5B%22hierarchy.lvl0%22%5D",
        },
    },
): ...


AstroBuildSearchAPI.build(__name__)
