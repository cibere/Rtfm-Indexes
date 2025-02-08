from pathlib import Path
from typing import Callable
import json
import sys
import runpy

type Indexes = dict[str, dict[str, str]]

ci_dir = Path(__file__).parent
root = ci_dir.parent
indexes_dir = root / "indexes"
indexes_dir.mkdir(exist_ok=True)


def dump_indexes(indexes: Callable[[], Indexes]) -> None:
    filename = indexes.__module__.split(".")[0]

    for name, index in indexes().items():
        file = indexes_dir / f"{filename}{f'-{name}' if name else ''}.json"
        file.write_text(json.dumps(index, indent=4))


if __name__ == "__main__":
    module = runpy.run_module(sys.argv[-1])
    dump_indexes(module["index"])
