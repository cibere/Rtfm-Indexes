from __future__ import annotations

from typing import ClassVar

from .indexer import BaseIndexer
from .structs import ApiIndex


class BaseAPI(BaseIndexer):
    response_type: ClassVar[str]
    url: ClassVar[str]
    method: ClassVar[str]

    def get_headers(self) -> dict[str, str]:
        return {}

    def _runner(self) -> None:
        raise NotImplementedError


class AlgoliaAPI(BaseAPI):
    def get_options(self) -> dict[str, str]:
        raise NotImplementedError

    def _runner(self) -> None:
        data = ApiIndex(
            name=self.name,
            favicon_url=self.favicon_url,
            url=self.url,
            api_type="Algolia",
            headers=self.get_headers(),
            options=self.get_options(),
        )
        self._save(data, self.name)
