from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

from msgspec import Struct
from msgspec import field as struct_field

if TYPE_CHECKING:
    from flogin import ResultConstructorKwargs

    from ._types import Cache


class BaseIndex(Struct):
    name: str
    favicon_url: str | None


class ApiIndex(BaseIndex, tag="api-index"):
    url: str
    options: dict[str, Any]
    version: str = "2.1"


class CacheIndex(BaseIndex, tag="cache-index"):
    cache: Cache
    version: str = "2.1"


class VariantManifest(Struct, tag="variant-manifest"):
    variants: Iterable[str]
    version: str = "2.1"


class Entry(Struct):
    text: str
    url: str
    options: ResultConstructorKwargs = struct_field(default_factory=dict)  # type: ignore
    ctx_menu_items: list[str] = struct_field(default_factory=list)
