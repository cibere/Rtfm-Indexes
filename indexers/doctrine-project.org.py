# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "aiohttp==3.13.2",
#     "beautifulsoup4==4.14.3",
#     "msgspec==0.20.0",
# ]
# ///
from __future__ import annotations

import asyncio
from typing import Any, ClassVar

import aiohttp
import bs4
from _base import BaseAPI, Container, ContainerMembers


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
            "base_url": "https://www.doctrine-project.org",
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
    def _get_version(self, page: bytes) -> list[str]:
        versions = []

        soup = bs4.BeautifulSoup(page, "html.parser")
        table = soup.find("table")
        assert isinstance(table, bs4.Tag)

        for tr in table.find_all("tr"):
            assert isinstance(tr, bs4.Tag)
            raw_version_tag = tr.find("a")
            assert isinstance(raw_version_tag, bs4.Tag)

            version = raw_version_tag.text.strip()
            if len(parts := version.split(".")) > 2:
                version = ".".join(parts[:2])
            versions.append(version)

        return versions

    async def get_project_versions(
        self, session: aiohttp.ClientSession, project: type[BaseDoctrineProject]
    ) -> tuple[type[BaseDoctrineProject], tuple[str, ...]]:
        url = (
            f"https://www.doctrine-project.org/projects/{project.doctrine_project}.html"
        )
        async with session.get(url) as res:
            data = await res.content.read()

        vers = await asyncio.to_thread(self._get_version, data)
        versions = ("latest", "stable", *vers)

        print(f"Versions for {project.doctrine_project}: {', '.join(versions)}")

        return (project, tuple(versions))

    async def get_members(self) -> ContainerMembers:
        projects = (
            CollectionsProject,
            DataFixturesProject,
            CommonProject,
            DbalProject,
            EventManagerProject,
            InstantiatorProject,
            InflectorProject,
            LexerProject,
            MigrationsProject,
            OrmProject,
            MongodbOdmProject,
            PhpcrOdmProject,
            PersistenceProject,
            RstParserProject,
        )
        tasks = []

        async with aiohttp.ClientSession() as cs:
            tasks = [self.get_project_versions(cs, cls) for cls in projects]

            return {
                cls.doctrine_project: (cls, variants)
                for (cls, variants) in await asyncio.gather(*tasks)
            }


DocterineProject.build(__name__)
