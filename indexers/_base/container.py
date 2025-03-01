from __future__ import annotations

import inspect
from collections.abc import Sequence

from .indexer import BaseIndexer


class Container(BaseIndexer):
    def _runner(self) -> None:
        variants: Sequence[tuple[str, type[BaseIndexer]]] = inspect.getmembers(
            self, lambda obj: issubclass(obj, BaseIndexer)
        )

        for name, cls in variants:
            cls._run_with_variant(name)
