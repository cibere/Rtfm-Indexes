# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class BrowserstackSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://www.browserstack.com/favicon.ico",
    options={
        "url": "https://ynhf55kpox-dsn.algolia.net/1/indexes/prod_global_search_reindex/query?x-algolia-agent=Algolia for JavaScript (4.20.0); Browser (lite)&x-algolia-api-key=MDI3NWM0YzhmZWI0N2U4NzBkYTgxMjYxYWIyNzUzN2EyYWMwNTNmODgwMTVlZjM0OTZiMTM0MGYzODBjNGEyMGZpbHRlcnM9aGFzX2NvZGVfc25pcHBldCUzQWZhbHNl&x-algolia-application-id=YNHF55KPOX",
        "payload": {
            "hitsPerPage": 5,
            "clickAnalytics": False,
            "filters": "(type:documentation)",
            "optionalFilters": ["type:documentation"],
        },
        "raw_payload": True,
    },
): ...


BrowserstackSearchAPI.build(__name__)
