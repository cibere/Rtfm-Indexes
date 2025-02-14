# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
#     "requests",
#     "yarl==1.18.2",
# ]
# ///
import sys
from pathlib import Path

import requests
from msgspec import json, msgpack
from yarl import URL


def get_local_file(path: Path) -> bytes:
    return path.read_bytes()


def get_web_file(url: URL) -> bytes:
    return requests.get(str(url), timeout=10).content


def main():
    args = sys.argv[1:]
    loc = args[0]

    if loc.startswith(("http://", "https://")):
        content = get_web_file(URL(loc))
    else:
        content = get_local_file(Path(loc))

    try:
        after = Path(args[1])
    except IndexError:
        after = None

    data = msgpack.decode(content)
    pretty = json.format(json.encode(data)).decode()
    print(pretty)

    if after:
        after.write_text(pretty)
        print(f"Wrote result to {after}")


if __name__ == "__main__":
    main()
