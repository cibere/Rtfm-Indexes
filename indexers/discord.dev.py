# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class DiscordSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="algolia",
    favicon_url="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png",
    options={
        "url": "https://7tyoyf10z2-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (4.23.3); Browser (lite); docsearch (3.3.1); docsearch-react (3.3.1)&x-algolia-api-key=786517d17e19e9d306758dd276bc6574&x-algolia-application-id=7TYOYF10Z2",
        "payload": {
            "indexName": "discord",
            "params": "attributesToRetrieve=%5B%22hierarchy.lvl0%22%2C%22hierarchy.lvl1%22%2C%22hierarchy.lvl2%22%2C%22hierarchy.lvl3%22%2C%22hierarchy.lvl4%22%2C%22hierarchy.lvl5%22%2C%22hierarchy.lvl6%22%2C%22content%22%2C%22type%22%2C%22url%22%5D&attributesToSnippet=%5B%22hierarchy.lvl1%3A10%22%2C%22hierarchy.lvl2%3A10%22%2C%22hierarchy.lvl3%3A10%22%2C%22hierarchy.lvl4%3A10%22%2C%22hierarchy.lvl5%3A10%22%2C%22hierarchy.lvl6%3A10%22%2C%22content%3A10%22%5D&snippetEllipsisText=%E2%80%A6&highlightPreTag=%3Cmark%3E&highlightPostTag=%3C%2Fmark%3E&hitsPerPage=20",
        },
    },
): ...


DiscordSearchAPI.build(__name__)
