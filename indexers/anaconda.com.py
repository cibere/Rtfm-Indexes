# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "msgspec==0.19.0",
# ]
# ///
from __future__ import annotations

from _base import BaseAPI


class AnacondaSearchAPI(
    BaseAPI,
    file=__file__,
    api_type="mintlify",
    favicon_url="https://alpinejs.dev/favicon.png",
    options={
        "url": "https://api.mintlifytrieve.com/api/chunk/autocomplete",
        "payload": {
            "search_type": "fulltext",
            "extend_results": True,
            "highlight_delimiters": ["?", ",", ".", "!", "\n"],
            "score_threshold": 0.2,
            "filters": {"must_not": [{"field": "tag_set", "match": ["code"]}]},
            "highlight_window": 10,
            "highlight_max_num": 1,
            "highlight_max_length": 2,
            "highlight_strategy": "exactmatch",
            "page_size": 20,
        },
        "base_url": "https://www.anaconda.com/docs/",
        "token": "tr-Ef0O1GG473PDFHfclCabtti5n0mHNolw",
        "dataset": "d75752ce-477d-4baa-bbaa-5bb858783e9b",
    },
): ...


AnacondaSearchAPI.build(__name__)
