# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class SearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    # favicon_url="",
    options={
        "url": "https://p6kicoku8e-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.17.0); Browser (lite); autocomplete-core (1.9.2); autocomplete-js (1.9.2)&x-algolia-api-key=9ac9f1177f81bc8cb5f6cf30485e62db&x-algolia-application-id=P6KICOKU8E",
        "payload": {
            "indexName": "production",
            "hitsPerPage": 50,
            "clickAnalytics": False,
            "filters": '(section:"Docs" OR section:"Registry" OR section:"Tutorials")',
        },
        "url_template": "https://www.pulumi.com{href}",
    },
): ...


SearchAPI.build(__name__)
