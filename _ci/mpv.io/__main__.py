import selenium, sys, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import Self
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

log = logging.getLogger("mpv.io")


class MpvIoParser:
    browser: webdriver.Firefox

    def __init__(self, url: str) -> None:
        self.url = url
        self.cache = {}

    def __enter__(self) -> Self:
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)
        self.browser.get(self.url)
        return self

    def __exit__(self, *args):
        self.browser.quit()
        del self.browser

    def parse_toc(
        self,
    ) -> None:
        el = self.browser.find_element(By.CLASS_NAME, "manual-navigation")
        for tag in el.find_elements(By.TAG_NAME, "li"):
            log.debug("Found %r", tag)
            atag = tag.find_element(By.TAG_NAME, "a")
            log.debug("Got atag: %r", atag)

            text = atag.get_attribute("innerText")
            assert text
            href = atag.get_attribute("href")
            assert href

            log.debug("Adding item to cache. Label: %r, Href: %r", text, href)
            self.cache[text] = href

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

            log.debug("Adding item to cache. Label: %r, Href: %r", text, href)
            self.cache[text] = href


def index_url(url: str):
    parser = MpvIoParser(url)

    with parser:
        parser.parse_toc()
        parser.parse_anchor_links()

    import json

    print(json.dumps(parser.cache, indent=4))
    return parser.cache


def index():
    return {
        "master": index_url("https://mpv.io/manual/master"),
        "stable": index_url("https://mpv.io/manual/stable"),
    }
