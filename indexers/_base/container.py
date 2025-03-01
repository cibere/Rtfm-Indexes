from __future__ import annotations

import sys

from .indexer import BaseIndexer


class Container(BaseIndexer):
    def get_members(self) -> dict[str, tuple[type[BaseIndexer], tuple[str, ...]]]:
        """{variant:(cls, [subvariants])}"""

        raise NotImplementedError

    def _runner(self) -> None:
        variants = self.get_members()

        for name, (cls, subvariants) in variants.items():
            cls.build("__main__", *[f"{name}-{subvar}" for subvar in subvariants])

        if sys.argv[-1] == "--debug":
            return

        self.save_variant_manifest(*variants)
