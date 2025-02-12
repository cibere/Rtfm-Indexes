from __future__ import annotations

from pathlib import Path
from typing import Any, ClassVar

from msgspec import Struct, msgpack

from .structs import VariantManifest
from .utils import FILE_EXT, UrlStr, indexes_dir


class BaseIndexer[KwargsT]:
    variant: ClassVar[str | None] = None
    file: ClassVar[str]
    favicon_url: ClassVar[str | None] = None

    def __init_subclass__(cls, **kwargs: KwargsT) -> None:
        if "base_url" in kwargs:
            kwargs["_raw_base_url"] = kwargs.pop("base_url")

        for key, value in kwargs.items():
            setattr(cls, key, value)

    @property
    def _filename(self) -> str:
        return Path(self.file).name.removesuffix(".py")

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
    def build(cls, name: str, *variations: str) -> None:
        if name != "__main__":
            if not name.startswith("__CIDEX_FILENAME_OVERRIDE:"):
                return
            cls.file = name.removeprefix("__CIDEX_FILENAME_OVERRIDE:").removesuffix(
                "__"
            )

        if not variations:
            return cls()._runner()

        self = None
        for variant in variations:
            cls.variant = variant
            self = cls()
            self._runner()

        if self:
            data = VariantManifest(variations)
            self._save(data, self._filename)
