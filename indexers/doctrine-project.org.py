# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI, Container
from _base.indexer import BaseIndexer


class DocterineProject(Container, file=__file__):
    def get_api(self, *filters: str) -> type[BaseAPI]:
        class Sub(
            BaseAPI,
            file=__file__,
            api_type="algolia",
            options={
                "url": "https://yvytft9xmw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.20.0); Browser; instantsearch.js (4.58.0); JS Helper (3.14.2)",
                "payload": {
                    "indexName": "pages",
                    "params": "facets=%5B%5D&hitsPerPage=5",
                    "tagFilters": filters,
                },
                "headers": {
                    "x-algolia-api-key": "a6dada5f33f148586b92cc3afefeaaf6",
                    "x-algolia-application-id": "YVYTFT9XMW",
                },
            },
        ): ...

        return Sub

    def get_members(self) -> dict[str, type[BaseIndexer]]:
        return {
            key: self.get_api(*value)
            for key, value in {
                "doctrine-collections": ("collections", "latest"),
                "doctrine-data-fixtures": ("data-fixtures", "latest"),
                "doctrine-common": ("common", "latest"),
                "doctrine-dbal": ("doctrine-dbal", "latest"),
                "doctrine-event-manager": ("event-manager", "latest"),
                "doctrine-instantiator": ("instantiator", "latest"),
                "doctrine-inflector": ("inflector", "latest"),
                "doctrine-lexer": ("lexer", "latest"),
                "doctrine-migrations": ("migrations", "latest"),
                "doctrine-orm": ("orm", "latest"),
                "doctrine-mongodb-odm": ("mongodb-odm", "latest"),
                "doctrine-phpcr-odm": ("phpcr-odm", "latest"),
                "doctrine-persistence": ("persistence", "latest"),
                "doctrine-rst-parser": ("rst-parser", "latest"),
            }.items()
        }


DocterineProject.build(__name__)
