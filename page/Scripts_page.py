from playwright.sync_api import Page

from page.Base_page import BasePage


class ScriptsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)