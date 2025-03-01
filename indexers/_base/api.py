from __future__ import annotations

import inspect
import sys
from collections.abc import Sequence
from typing import Any, ClassVar

from .indexer import BaseIndexer
from .structs import ApiIndex

BASE_URL = (
    "http://127.0.0.1:8787"
    if sys.argv[-1] == "--debug"
    else "https://rtfm-index-api.cibere.dev"
)


class APIContainer(BaseIndexer):
    def _runner(self) -> None:
        variants: Sequence[tuple[str, type[BaseAPI]]] = inspect.getmembers(
            self, lambda obj: issubclass(obj, BaseAPI)
        )

        for name, cls in variants:
            cls._run_with_variant(name)


class BaseAPI(BaseIndexer):
    options: ClassVar[dict[str, Any]] = {}
    api_type: ClassVar[str]

    def get_options(self) -> dict[str, Any]:
        return self.options

    def _runner(self) -> None:
        self._save(
            ApiIndex(
                self.name,
                self.favicon_url,
                f"{BASE_URL}/{self.api_type}",
                self.get_options(),
            ),
            self.name,
        )
