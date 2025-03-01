# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class CapacitorJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://capacitorjs.com/docs/img/meta/favicon.png",
    options={
        "url": "https://3ivalo5ou4-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.19.1); Browser (lite); docsearch (3.6.1); docsearch-react (3.6.1); docusaurus (3.5.2)&x-algolia-api-key=5fdbbcbd186f2a1265494810dd0bf09c&x-algolia-application-id=3IVALO5OU4",
        "payload": {
            "indexName": "capacitorjs",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20&clickAnalytics=false&facetFilters=%5B%22language%3Aen%22%2C%5B%22docusaurus_tag%3Adefault%22%2C%22docusaurus_tag%3Adocs-default-current%22%5D%5D",
        },
    },
): ...


CapacitorJsSearchAPI.build(__name__)
