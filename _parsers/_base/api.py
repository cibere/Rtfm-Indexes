from __future__ import annotations

from typing import Any, ClassVar

from .indexer import BaseIndexer
from .structs import ApiIndex


class BaseAPI(BaseIndexer):
    options: ClassVar[dict[str, Any]] = {}
    api_type: ClassVar[str]

    def _runner(self) -> None:
        self._save(
            ApiIndex(
                self.name,
                self.favicon_url,
                f"https://rtfm-index-api.cibere.dev/{self.api_type}",
                self.options,
            ),
            self.name,
        )
