from __future__ import annotations

from pathlib import Path

FILE_EXT = "cidex"

_bases_dir = Path(__file__).parent
parsers_dir = _bases_dir.parent
root = parsers_dir.parent
indexes_dir = root / "indexes_v2"


class UrlStr(str):
    def __truediv__(self, other: str) -> UrlStr:
        return UrlStr(self.rstrip("/") + "/" + other.lstrip("/"))
