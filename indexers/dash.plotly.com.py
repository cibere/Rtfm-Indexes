# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class DashPlotlySearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://dash.plotly.com/assets/favicon.ico?m=1740510067.0",
    options={
        "url": "https://7ek9khjw8m-dsn.algolia.net/1/indexes/dash_oss_docs/query?x-algolia-agent=Algolia for JavaScript (4.22.1); Browser (lite)&x-algolia-api-key=4dae07ded6a721de73bde7356eec9280&x-algolia-application-id=7EK9KHJW8M",
        "payload": {},
        "base_url": "https://dash.plotly.com",
    },
): ...


DashPlotlySearchAPI.build(__name__)
