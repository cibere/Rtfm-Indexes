from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from inspect import isawaitable
from typing import Any

from .indexer import BaseIndexer

type ContainerMembers = dict[str, tuple[type[BaseIndexer], tuple[str, ...]]]


class Container(BaseIndexer):
    def get_members(self) -> ContainerMembers | Coroutine[Any, Any, ContainerMembers]:
        """{variant:(cls, [subvariants])}"""

        raise NotImplementedError

    def _runner(self) -> None:
        variants = self.get_members()
        if isawaitable(variants):
            variants = asyncio.run(variants)

        for name, (cls, raw_subvariants) in variants.items():
            subvariants = [f"{name}-{subvar}" for subvar in raw_subvariants]
            cls.build("__main__", *subvariants, save_manifest=False)

            self.save_variant_manifest(
                *subvariants, filename=f"{self._filename}-{name}"
            )

        self.save_variant_manifest(*variants)
