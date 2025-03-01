from __future__ import annotations

import sys
from typing import Any, ClassVar

from .indexer import BaseIndexer
from .structs import ApiIndex

BASE_URL = (
    "http://127.0.0.1:8787"
    if sys.argv[-1] == "--debug"
    else "https://rtfm-index-api.cibere.dev"
)


class BaseAPI(BaseIndexer):
    options: ClassVar[dict[str, Any]] = {}
    api_type: ClassVar[str]

    def _runner(self) -> None:
        self._save(
            ApiIndex(
                self.name,
                self.favicon_url,
                f"{BASE_URL}/{self.api_type}",
                self.options,
            ),
            self.name,
        )
