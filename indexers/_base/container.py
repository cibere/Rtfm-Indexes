from __future__ import annotations

from .indexer import BaseIndexer


class Container(BaseIndexer):
    def get_members(self) -> dict[str, tuple[type[BaseIndexer], tuple[str, ...]]]:
        """{variant:(cls, [subvariants])}"""

        raise NotImplementedError

    def _runner(self) -> None:
        variants = self.get_members()

        for name, (cls, raw_subvariants) in variants.items():
            subvariants = [f"{name}-{subvar}" for subvar in raw_subvariants]
            cls.build("__main__", *subvariants, save_manifest=False)

            self.save_variant_manifest(
                *subvariants, filename=f"{self._filename}-{name}"
            )

        self.save_variant_manifest(*variants)
