# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class GithubSearchAPI(
    BaseAPI,
    file=__file__,
    url="https://docs.github.com/api/search/v1",
    favicon_url="https://github.com/favicon.ico",
    api_type="Github",
): ...


GithubSearchAPI.build(__name__)
