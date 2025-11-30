# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from typing import Any

from _base import BaseAPI

attrs = {
    "attributesToRetrieve": [
        "url_path",
        "description",
        "page_title",
        "headings",
        "external_url",
        "type",
        "products",
    ]
}


class HashicorpSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://developer.hashicorp.com/favicon.svg",
):
    def get_options(self) -> dict[str, Any]:
        variant_filter = f"(products:{self.variant})"
        if self.variant == "hcp":
            variant_filter = "(products:hcp OR edition:hcp)"

        return {
            "url": "https://yy0ffni7mf-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.20.2); Lite (5.20.2); Browser; instantsearch.js (4.77.3); react (18.2.0); react-instantsearch (7.15.3); react-instantsearch-core (7.15.3); next.js (14.2.1); JS Helper (3.24.1)&x-algolia-api-key=074499cdb522e30a32ebbe75a6d05779&x-algolia-application-id=YY0FFNI7MF",
            "payloads": [
                {
                    "indexName": "prod_DEVDOT_omni",
                    "filters": variant_filter,
                }
                | attrs,
                {
                    "indexName": "prod_DEVDOT_omni",
                    "filters": f"(type:docs) AND {variant_filter}",
                }
                | attrs,
                {
                    "indexName": "prod_DEVDOT_omni",
                    "filters": f"(type:integration) AND {variant_filter}",
                }
                | attrs,
                {
                    "indexName": "prod_DEVDOT_omni",
                    "filters": f"(type:tutorial) AND {variant_filter}",
                }
                | attrs,
            ],
            "is_hashicorp": True,
        }


HashicorpSearchAPI.build(
    __name__,
    "consul",
    "hcp",
    "terraform",
    "packer",
    "vault",
    "boundary",
    "nomad",
    "waypoint",
    "vagrant",
)
