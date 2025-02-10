# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
# ]
# ///
from __future__ import annotations

from typing import Any

from _base import BaseAPI


class MathworksSearchAPI(
    BaseAPI,
    file=__file__,
    url="https://www.mathworks.com/help/search/suggest/doccenter/en/R2024b",
    favicon_url="https://www.mathworks.com/favicon.ico",
    api_type="Mathworks",
):
    def get_options(self) -> dict[str, Any]:
        return {"selectedsource": "mw", "width": "785.667"}

    def get_headers(self) -> dict[str, str]:
        return {"User-Agent": "python-flow.launcher.plugin.rtfm/1.0.0"}


MathworksSearchAPI.build(__name__)
