# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "selenium==4.38.0",
#   "beautifulsoup4==4.14.3",
#   "msgspec==0.20.0",
# ]
# ///


from types import TracebackType
from typing import Self

from _base import BaseSyncParser, Cache, Entry, MutableCache
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class MpvIoParser(
    BaseSyncParser,
    file=__file__,
    favicon_url="https://mpv.io/images/favicon-5d3b2a52.png",
    base_url="https://mpv.io/manual/{VAR}",
):
    browser: webdriver.Firefox

    def __init__(self) -> None:
        self.cache: MutableCache = {}

    def __enter__(self) -> Self:
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)
        self.browser.get(self.base_url)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> bool:
        self.browser.quit()
        del self.browser
        return False

    def parse_toc(
        self,
    ) -> None:
        el = self.browser.find_element(By.CLASS_NAME, "manual-navigation")
        for tag in el.find_elements(By.TAG_NAME, "li"):
            atag = tag.find_element(By.TAG_NAME, "a")

            text = atag.get_attribute("innerText")
            href = atag.get_attribute("href")

            if text and href:
                self.cache[text] = Entry(text, href)

    def parse_anchor_links(self) -> None:
        for literalEl in self.browser.find_elements(By.CLASS_NAME, "literal"):
            if "docutil" not in str(literalEl.get_attribute("class")):
                continue
            try:
                anchor = literalEl.find_element(By.CLASS_NAME, "anchor")
            except NoSuchElementException:
                continue

            href = anchor.get_attribute("href")
            text = literalEl.get_attribute("innerText")

            if text and href:
                self.cache[text] = Entry(text, href)

    def build_cache(self) -> Cache:
        self.parse_toc()
        self.parse_anchor_links()
        return self.cache


MpvIoParser.build(__name__, "master", "stable")
