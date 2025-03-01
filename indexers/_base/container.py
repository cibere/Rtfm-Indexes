from __future__ import annotations

import inspect

from .indexer import BaseIndexer


class Container(BaseIndexer):
    def get_members(self) -> dict[str, type[BaseIndexer]]:
        return dict(inspect.getmembers(self, lambda obj: issubclass(obj, BaseIndexer)))

    def _runner(self) -> None:
        variants = self.get_members()

        for name, cls in variants.items():
            cls._run_with_variant(name)
