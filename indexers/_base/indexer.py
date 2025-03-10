from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, ClassVar, Self

from msgspec import Struct, msgpack

from .structs import VariantManifest
from .utils import FILE_EXT, UrlStr, indexes_dir


class BaseIndexer[KwargsT]:
    variant: ClassVar[str | None] = None
    file: ClassVar[str]
    favicon_url: ClassVar[str | None] = None
    _filename_suffix: str | None = None

    def __init__(self, **kwargs: KwargsT) -> None:
        self._kwargs_to_attrs(self, **kwargs)

    def __init_subclass__(cls, **kwargs: KwargsT) -> None:
        cls._kwargs_to_attrs(cls, **kwargs)

    @classmethod
    def _kwargs_to_attrs(cls, obj: Any, **kwargs: KwargsT) -> None:
        if "base_url" in kwargs:
            kwargs["_raw_base_url"] = kwargs.pop("base_url")

        for key, value in kwargs.items():
            setattr(obj, key, value)

    @property
    def _filename(self) -> str:
        return Path(self.file).name.removesuffix(".py") + (self._filename_suffix or "")

    @property
    def name(self) -> str:
        return self._filename + (f"-{self.variant}" if self.variant else "")

    @classmethod
    def _save(cls, data: Struct, filename: str) -> None:
        indexes_dir.mkdir(exist_ok=True)

        file = indexes_dir / f"{filename}.{FILE_EXT}"

        def enc_hook(obj: Any) -> Any:
            if isinstance(obj, UrlStr):
                return str(obj)
            return repr(obj)

        file.write_bytes(msgpack.encode(data, enc_hook=enc_hook))
        print(f"Wrote to {file}")

    def _runner(self) -> None:
        raise NotImplementedError

    @classmethod
    def _run_with_variant(cls, variant: str) -> Self:
        cls.variant = variant
        self = cls()
        self._runner()
        return self

    def save_variant_manifest(
        self, *variations: str, filename: str | None = None
    ) -> None:
        if sys.argv[-1] == "--debug":
            return

        data = VariantManifest(variations)
        self._save(data, filename or self._filename)

    @classmethod
    def build(cls, name: str, *variations: str, save_manifest: bool = True) -> None:
        if name != "__main__":
            if not name.startswith("__CIDEX_FILENAME_OVERRIDE:"):
                return
            cls.file = name.removeprefix("__CIDEX_FILENAME_OVERRIDE:").removesuffix(
                "__"
            )

        if not variations:
            return cls()._runner()

        self = [cls._run_with_variant(variant) for variant in variations][0]  # noqa: RUF015 # all iterations need to run, but just need one of the self values, so we don't need to create another to save

        if save_manifest:
            self.save_variant_manifest(*variations)
