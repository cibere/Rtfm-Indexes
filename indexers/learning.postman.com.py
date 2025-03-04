# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class PostmanSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://learning.postman.com/icons/favicon-32x32.png",
    options={
        "url": "https://4a5n71xyh0-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.20.3); Search (5.20.3); Browser&x-algolia-api-key=b1d4a6aacf529568748a640b2dc50d13&x-algolia-application-id=4A5N71XYH0",
        "payload": {
            "indexName": "docs-next",
            "distinct": True,
            "hitsPerPage": 20,
        },
        "url_template": "https://learning.postman.com{slug}",
    },
): ...


PostmanSearchAPI.build(__name__)
