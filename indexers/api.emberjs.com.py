# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
#     "requests==2.32.5",
# ]
# ///
from __future__ import annotations

import os
from typing import Any

import requests
from _base import BaseAPI, Container, ContainerMembers

GH_TOKEN = os.environ["GITHUB_TOKEN"]


def fetch_versions() -> dict[str, int]:
    url = "https://api.github.com/repos/emberjs/ember.js/releases"
    url += "?per_page=100"

    headers = {"Authorization": f"token {GH_TOKEN}"}
    data = requests.get(url, headers=headers, timeout=10).json()

    versions: dict[str, int] = {}

    for release in data:
        if release["prerelease"] or release["draft"]:
            continue

        version: str = release["tag_name"].split("-")[0].removeprefix("v")

        major, minor, raw_micro = version.split(".")
        key = f"{major}.{minor}"
        micro = int(raw_micro)

        if micro > versions.get(key, -1):
            versions[key] = micro
    print(versions)
    return versions


VERSIONS = fetch_versions()


class EmberJs(Container, file=__file__):
    def get_members(self) -> ContainerMembers:
        return dict.fromkeys(VERSIONS, (EmberJsSearchAPI, ()))


class EmberJsSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://api.emberjs.com/assets/images/favicon.png",
):
    def get_options(self) -> dict[str, Any]:
        assert self._filename_suffix

        major, minor = self._filename_suffix.removeprefix("-").split(".")
        micro = VERSIONS[f"{major}.{minor}"]
        ver = f"{major}.{minor}.{micro}"

        return {
            "url": "https://y1omr4c7mf-dsn.algolia.net/1/indexes/methods/query?x-algolia-agent=Algolia for JavaScript (4.23.3); Browser",
            "payload": {
                "hitsPerPage": 15,
                "restrictSearchableAttributes": [
                    "hierarchy.lvl0",
                    "hierarchy.lvl1",
                    "hierarchy.lvl2",
                ],
                "tagFilters": [f"version:{ver}"],
                "facetFilters": ["access:-private"],
            },
            "headers": {
                "x-algolia-api-key": "c35425b69b31be1bb4786f0a72146306",
                "x-algolia-application-id": "Y1OMR4C7MF",
            },
            "url_template": f"https://api.emberjs.com/ember/{major}.{minor}/functions/{{class}}/{{name}}",
        }


EmberJs.build(__name__)  # , "6.2.0")
