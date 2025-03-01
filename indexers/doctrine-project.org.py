# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from typing import Any, ClassVar

from _base import BaseAPI, Container
from _base.indexer import BaseIndexer


class BaseDoctrineProject(BaseAPI, file=__file__, api_type="algolia"):
    doctrine_project: ClassVar[str]

    def get_options(self) -> dict[str, Any]:
        return {
            "url": "https://yvytft9xmw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.20.0); Browser; instantsearch.js (4.58.0); JS Helper (3.14.2)",
            "payload": {
                "indexName": "pages",
                "params": "facets=%5B%5D&hitsPerPage=5",
                "tagFilters": [self.doctrine_project, self.variant],
            },
            "headers": {
                "x-algolia-api-key": "a6dada5f33f148586b92cc3afefeaaf6",
                "x-algolia-application-id": "YVYTFT9XMW",
            },
        }


class CollectionsProject(BaseDoctrineProject, doctrine_project="collections"): ...


class DataFixturesProject(BaseDoctrineProject, doctrine_project="data-fixtures"): ...


class CommonProject(BaseDoctrineProject, doctrine_project="common"): ...


class DbalProject(BaseDoctrineProject, doctrine_project="dbal"): ...


class EventManagerProject(BaseDoctrineProject, doctrine_project="event-manager"): ...


class InstantiatorProject(BaseDoctrineProject, doctrine_project="instantiator"): ...


class InflectorProject(BaseDoctrineProject, doctrine_project="inflector"): ...


class LexerProject(BaseDoctrineProject, doctrine_project="lexer"): ...


class MigrationsProject(BaseDoctrineProject, doctrine_project="migrations"): ...


class OrmProject(BaseDoctrineProject, doctrine_project="orm"): ...


class MongodbOdmProject(BaseDoctrineProject, doctrine_project="mongodb-odm"): ...


class PhpcrOdmProject(BaseDoctrineProject, doctrine_project="phpcr-odm"): ...


class PersistenceProject(BaseDoctrineProject, doctrine_project="persistence"): ...


class RstParserProject(BaseDoctrineProject, doctrine_project="rst-parser"): ...


class DocterineProject(Container, file=__file__):
    def get_members(self) -> dict[str, tuple[type[BaseIndexer], tuple[str, ...]]]:
        return {
            "doctrine-collections": (
                DataFixturesProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-data-fixtures": (
                DataFixturesProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-common": (
                CommonProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-dbal": (
                DbalProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-event-manager": (
                EventManagerProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-instantiator": (
                InstantiatorProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-inflector": (
                InflectorProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-lexer": (
                LexerProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-migrations": (
                MigrationsProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-orm": (
                OrmProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-mongodb-odm": (
                MongodbOdmProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-phpcr-odm": (
                PhpcrOdmProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-persistence": (
                PersistenceProject,
                (
                    "latest",
                    "stable",
                ),
            ),
            "doctrine-rst-parser": (
                RstParserProject,
                (
                    "latest",
                    "stable",
                ),
            ),
        }


DocterineProject.build(__name__)
