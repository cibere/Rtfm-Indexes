# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
#     "requests==2.32.3",
# ]
# ///

from __future__ import annotations

import requests
from _base import BaseSyncParser


class FlowLauncherParser(
    BaseSyncParser,
    file=__file__,
    base_url="https://www.flowlauncher.com/docs",
    favicon_url="https://www.flowlauncher.com/public/favicon.ico",
):
    def build_cache(self) -> dict[str, str]:
        raw_content = requests.get(self / "_sidebar.md", timeout=10).content

        lines = raw_content.decode().splitlines()
        header = None

        cache = {}

        for line in lines:
            line = line.strip("-    ")
            if not line.startswith("[**"):
                header = line
            else:
                parts = line.split("**](/")
                name = parts[0].strip("*[]")
                loc = parts[1].strip("()")

                title = f"{name} - {header}" if header else name
                cache[title] = self / loc

        return cache


FlowLauncherParser.build(__name__)
