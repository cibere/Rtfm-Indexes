from __future__ import annotations

import runpy
from pathlib import Path

FILE_EXT = "cidex"

_bases_dir = Path(__file__).parent
indexers_dir = _bases_dir.parent
root = indexers_dir.parent
indexes_dir = root / "indexes_v2"


class UrlStr(str):
    def __truediv__(self, other: str) -> UrlStr:
        return UrlStr(self.rstrip("/") + "/" + other.lstrip("/"))


def alias(actual: str, aliased: str) -> None:
    file = indexers_dir / f"{actual}.py"
    name = f"__CIDEX_FILENAME_OVERRIDE:{aliased}__"
    runpy.run_path(str(file), run_name=name)
