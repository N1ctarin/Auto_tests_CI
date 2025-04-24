import pytest
from playwright.sync_api import sync_playwright

from playwright.async_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    Selectors,
    async_playwright,
)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        yield page
        page.close()
        browser.close()



#Заготовка на будущее
@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, browser_name: str) -> BrowserType:
    if browser_name == "chromium":
        return playwright.chromium
    if browser_name == "firefox":
        return playwright.firefox
    if browser_name == "webkit":
        return playwright.webkit
    raise Exception(f"Invalid browser_name: {browser_name}")