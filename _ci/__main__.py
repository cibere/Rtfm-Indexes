from __future__ import annotations

import importlib.util
import pathlib, json
from logging import getLogger, INFO
from typing import TYPE_CHECKING
from .logs import setup_logging

if TYPE_CHECKING:
    from collections.abc import Iterator

setup_logging(INFO)
log = getLogger("indexer")

ci_folder = pathlib.Path(__file__).parent
root = ci_folder.parent
indexes_folder = root / "indexes"
indexes_folder.mkdir(exist_ok=True)


def index_path(folder: pathlib.Path) -> Iterator[tuple[str, dict[str, str]]]:
    file = folder / "__main__.py"
    typename = file.name.removesuffix(".py")

    if file.name.startswith("_"):
        pass
    log.info(f"Builting {folder.name!r} at {file!r}")
    spec = importlib.util.spec_from_file_location(typename, file)
    assert spec
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)

    indexes: dict[str, dict[str, str]] = module.index()
    for key, index in indexes.items():
        yield f"{folder.name}-{key}", index


def built_cache():
    for folder in ci_folder.iterdir():
        if not folder.is_dir() or folder.name.startswith("_"):
            continue
        try:
            for name, index in index_path(folder):
                file = indexes_folder / f"{name}.json"
                file.write_text(json.dumps(index, indent=4))
        except Exception as e:
            log.exception(f"Unable to index {folder.name} @ {folder}", exc_info=e)
            continue


if __name__ == "__main__":
    built_cache()
