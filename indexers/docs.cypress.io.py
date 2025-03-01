# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class CypressSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://docs.cypress.io/favicon.svg",
    options={
        "url": "https://r9kda5fmjb-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.22.1); Browser (lite); docsearch (3.5.2); docsearch-react (3.5.2); docusaurus (3.1.1)&x-algolia-api-key=b4af59e23bc2fa05281af7dcf13fcae5&x-algolia-application-id=R9KDA5FMJB",
        "payload": {
            "indexName": "cypress_docs",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20&clickAnalytics=false&facetFilters=%5B%5D",
        },
    },
): ...


CypressSearchAPI.build(__name__)
