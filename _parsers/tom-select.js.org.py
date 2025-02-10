# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
# ]
# ///
from __future__ import annotations

from _base import AlgoliaAPI


class TomSelectJs(
    AlgoliaAPI,
    url="https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;docsearch.js 2.6.3&x-algolia-application-id=BH4D9OD16A&x-algolia-api-key=662e3a3a9d206ebad6d19f341b85acbd",
    method="POST",
    response_type="algolia",
    file=__file__,
):
    def get_options(self) -> dict[str, str]:
        return {"params": "query=te&hitsPerPage=20", "indexName": "tom-select"}


if __name__ == "__main__":
    TomSelectJs.build()
