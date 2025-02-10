from __future__ import annotations

from typing import Any, ClassVar

from .indexer import BaseIndexer
from .structs import ApiIndex


class BaseAPI(BaseIndexer):
    url: ClassVar[str]
    api_type: ClassVar[str]

    def get_headers(self) -> dict[str, str]:
        return {}

    def get_options(self) -> dict[str, Any]:
        return {}

    def _runner(self) -> None:
        data = ApiIndex(
            name=self.name,
            favicon_url=self.favicon_url,
            url=self.url,
            api_type=self.api_type,
            headers=self.get_headers(),
            options=self.get_options(),
        )
        self._save(data, self.name)
