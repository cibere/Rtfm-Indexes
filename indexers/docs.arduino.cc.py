# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class ArduinoDocsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://cdn.arduino.cc/header-footer/prod/assets/favicon-arduino/favicon.ico",
    options={
        "url": "https://y2y10mz7jy-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.23.3); Browser (lite); JS Helper (3.14.0); react (18.2.0); react-instantsearch (6.40.4); autocomplete-core (1.17.0)&x-algolia-api-key=1de4271379988b2cb3d797b07fca6805&x-algolia-application-id=Y2Y10MZ7JY",
        "payload": {
            "indexName": "prod_documentation",
            "params": "facets=%5B%5D&filters=environment%3A'docs.arduino.cc'&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&page=0&query=t&tagFilters=",
        },
    },
): ...


ArduinoDocsSearchAPI.build(__name__)
