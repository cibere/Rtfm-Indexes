# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GithubSearchAPI(
    BaseAPI,
    file=__file__,
    favicon_url="https://github.com/favicon.ico",
    api_type="github",
): ...


GithubSearchAPI.build(__name__)
