from playwright.sync_api import Page
from abc import ABC


class BasePage(ABC):

    def __init__(self, page: Page):
        self.page = page

    def click_on_selector_with_text(self, text):
        self.page.wait_for_selector(f'text="{text}"', state='visible')
        self.page.click(f'text="{text}"')

    def click_on_selector_without_waiting(self, text):
        self.page.click(f'text="{text}"')

    def click_on_selector(self, selector):
        self.page.wait_for_selector(selector, state='visible')
        self.page.click(selector)

    def check_selector_on_space(self, selector):
        return self.page.locator(selector)

    def get_now_url(self, browser):
        return browser.url

    def is_not_element_present(self, selector):
        return self.page.query_selector(selector) is None

    def check_selector_equals_text(self, selector, text):
        self.page.wait_for_selector(selector, state='visible')
        return self.page.text_content(selector) == text