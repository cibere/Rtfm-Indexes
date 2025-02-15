# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4==4.13.3",
#     "certifi==2025.1.31",
#     "charset-normalizer==3.4.1",
#     "idna==3.10",
#     "msgspec==0.19.0",
#     "requests==2.32.3",
#     "soupsieve==2.6",
#     "typing-extensions==4.12.2",
#     "urllib3==2.3.0",
# ]
# ///

from __future__ import annotations

import bs4
import requests
from _base import BaseSyncParser, Entry


class SS64Parser(
    BaseSyncParser,
    file=__file__,
    base_url="https://ss64.com/{VAR}",
    favicon="https://ss64.com/favicon.svg",
):
    soup: bs4.BeautifulSoup

    def __init__(self) -> None:
        self.cache: dict[str, str | Entry] = {}

    @property
    def is_powershell(self) -> bool:
        return self.variant == "ps"

    def build_cache(self) -> dict[str, str | Entry]:
        res = requests.get(self.base_url, timeout=10)
        self.soup = bs4.BeautifulSoup(res.content, "html.parser")

        container = self.soup.find_all("table")[-1]
        assert isinstance(container, bs4.Tag)

        rows = container.find_all("tr")
        for row in rows:
            if not isinstance(row, bs4.Tag):
                continue

            tds = row.find_all("td")
            if not tds:
                continue

            tds0 = tds[0]
            if not isinstance(tds0, bs4.Tag) or tds0.attrs.get("class") == "ix":
                continue

            cmd_name_td = tds[1]
            if not isinstance(cmd_name_td, bs4.Tag):
                continue

            atag = cmd_name_td.find("a")
            if isinstance(atag, bs4.Tag):
                command_name = atag.text.strip()
                path = str(atag.attrs.get("href", "")).strip()
            else:
                command_name = cmd_name_td.text.strip()
                path = ""

            aliases = []
            if self.is_powershell:
                raw_aliases = tds[2].text.strip().replace(" ", "")
                if raw_aliases:
                    aliases = raw_aliases.split("/")

            short_description = tds[-1].text
            url = self / path

            if command_name:
                name = f"{command_name}"
                self.cache[name] = Entry(name, url, {"sub": short_description})
                alias_sub_prefix = f"Alias of: {name} | "
            else:
                alias_sub_prefix = ""

            for alias in aliases:
                self.cache[alias] = Entry(
                    alias, url, {"sub": f"{alias_sub_prefix}{short_description}"}
                )

        return self.cache


SS64Parser.build(__name__, "mac", "bash", "nt", "ps")
