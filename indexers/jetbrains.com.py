# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class JetbrainsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://www.jetbrains.com/icon.svg?r=1234",
    options={
        "url": "https://ohiv241qet-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.7.0); Browser",
        "headers": {
            "x-algolia-api-key": "286ecbf5e280ae8a7568867b2607fb21",
            "x-algolia-application-id": "OHIV241QET",
        },
        "payloads": [
            {
                "params": "attributesToRetrieve=%5B%22pageTitle%22%2C%22url%22%2C%22mainTitle%22%5D&attributesToSnippet=%5B%22content%3A40%22%5D&queryLanguages=%5B%22en%22%5D&distinct=1&hitsPerPage=55",
                "indexName": "prod_WWW-JETBRAINS-COM_en-us",
            },
            {
                "params": "attributesToRetrieve=%5B%22pageTitle%22%2C%22url%22%2C%22mainTitle%22%5D&attributesToSnippet=%5B%22content%3A40%22%5D&queryLanguages=%5B%22en%22%5D&distinct=1&hitsPerPage=55",
                "indexName": "prod_JETBRAINSCOM_HELP",
            },
            {
                "params": "attributesToRetrieve=%5B%22pageTitle%22%2C%22url%22%2C%22mainTitle%22%5D&attributesToSnippet=%5B%22content%3A40%22%5D&queryLanguages=%5B%22en%22%5D&distinct=1&hitsPerPage=55",
                "indexName": "prod_PLUGINS-JETBRAINS-COM",
            },
        ],
    },
): ...


JetbrainsSearchAPI.build(__name__)
