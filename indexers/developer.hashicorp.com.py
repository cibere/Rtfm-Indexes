# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class HashicorpVaultSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://developer.hashicorp.com/favicon.svg",
    options={
        "url": "https://yy0ffni7mf-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.20.2); Lite (5.20.2); Browser; instantsearch.js (4.77.3); react (18.2.0); react-instantsearch (7.15.3); react-instantsearch-core (7.15.3); next.js (14.2.1); JS Helper (3.24.1)&x-algolia-api-key=074499cdb522e30a32ebbe75a6d05779&x-algolia-application-id=YY0FFNI7MF",
        "payload": {
            "indexName": "prod_DEVDOT_omni",
        },
    },
): ...


HashicorpVaultSearchAPI.build(__name__)
