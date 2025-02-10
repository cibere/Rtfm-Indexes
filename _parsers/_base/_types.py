from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .structs import Entry

type Cache = Mapping[str, str | Entry]
