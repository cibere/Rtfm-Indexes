# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec",
# ]
# ///
from pathlib import Path
from msgspec import msgpack, json
import sys

args = sys.argv[1:]

before = Path(args[0])

try:
    after = Path(args[1])
except IndexError:
    after = None

data = msgpack.decode(before.read_bytes())
pretty = json.format(json.encode(data)).decode()
print(pretty)

if after:
    after.write_text(pretty)