# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class PrometheusSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://prometheus.io/assets/favicons/favicon-32x32.png",
    options={
        "url": "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=48ac0b7924908a1fd40b1cb18b402ba1",
        "payload": {
            "indexName": "prometheus",
            "hitsPerPage": 20,
            "filters": "include:true",
        },
    },
): ...


PrometheusSearchAPI.build(__name__)
