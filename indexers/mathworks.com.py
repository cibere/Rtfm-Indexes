# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class MathworksSearchAPI(
    BaseAPI,
    file=__file__,
    favicon_url="https://www.mathworks.com/favicon.ico",
    api_type="mathworks",
): ...


MathworksSearchAPI.build(__name__)
