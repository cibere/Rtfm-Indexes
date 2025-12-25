# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

from typing import Any

from _base import BaseAPI


class PlotlySearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://dash.plotly.com/assets/favicon.ico?m=1740510067.0",
):
    def get_options(self) -> dict[str, Any]:
        index: dict[Any, Any] = {
            "python": "python_docs",
            "julia": "schema",
            "r": "r_docs",
        }
        return {
            "url": "https://7ek9khjw8m-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.24.5;instantsearch.js 2.3.3;JS Helper 2.23.0&x-algolia-application-id=7EK9KHJW8M&x-algolia-api-key=4dae07ded6a721de73bde7356eec9280",
            "payload": {
                "indexName": index[self.variant],
                "page": 0,
                "facets": [],
            },
            "base_url": "https://plotly.com/julia/"
            if self.variant == "julia"
            else "https://plotly.com",
        }


PlotlySearchAPI.build(__name__, "r", "python", "julia")
