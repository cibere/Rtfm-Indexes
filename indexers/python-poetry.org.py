# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4==4.14.2",
#     "msgspec==0.19.0",
#     "requests==2.32.5",
# ]
# ///
from __future__ import annotations

from typing import Any

import bs4
import requests
from _base import BaseAPI


class PythonPoetrySearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://python-poetry.org/images/logo-origami.svg",
):
    def get_versions(self):
        data = requests.get("https://python-poetry.org/docs/", timeout=10).content
        soup = bs4.BeautifulSoup(data, "html.parser")
        select = soup.find("ul", attrs={"data-select-target": "menu"})
        assert isinstance(select, bs4.Tag)
        for opt in select.find_all("li", {"id": "listbox-option-0"}):
            if not isinstance(opt, bs4.Tag):
                continue

            atag = opt.find("a")
            if not isinstance(atag, bs4.Tag):
                continue
            href = str(atag["href"])
            if len(href.split("/")) == 4 and href.startswith("/docs/"):
                yield href.removeprefix("/doc/").removesuffix("/")

    def get_options(self) -> dict[str, Any]:
        return {
            "url": "https://sihvopcwni-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (5.20.1); Search (5.20.1); Browser; autocomplete-core (1.18.0); autocomplete-js (1.18.0)&x-algolia-api-key=ed995fb51a9bb73b4d9da7857ea3a368&x-algolia-application-id=SIHVOPCWNI",
            "payload": {
                "indexName": "docs",
                "filters": f"version:{self.variant}",
                "hitsPerPage": 5,
            },
            "base_url": "https://python-poetry.org",
        }


def get_versions():
    data = requests.get("https://python-poetry.org/docs/", timeout=10).content
    soup = bs4.BeautifulSoup(data, "html.parser")
    select = soup.find("ul", attrs={"data-select-target": "menu"})
    assert isinstance(select, bs4.Tag)
    for opt in select.find_all("li", {"id": "listbox-option-0"}):
        if not isinstance(opt, bs4.Tag):
            continue

        atag = opt.find("a")
        if not isinstance(atag, bs4.Tag):
            continue
        href = str(atag["href"])
        if not href.startswith("/docs/"):
            continue

        span = atag.find("span", class_="truncate")
        if not isinstance(span, bs4.Tag):
            continue
        yield span.text.strip()


PythonPoetrySearchAPI.build(__name__, *get_versions())
