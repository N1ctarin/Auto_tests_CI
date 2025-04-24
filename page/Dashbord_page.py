from playwright.sync_api import Page

from page.Base_page import BasePage
from page.Locators import DashboardPageLocator


class DashbordPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def add_operative_dashbord_in_project(self, name):
        self.page.click(DashboardPageLocator.ICON_DASHBORD)
        self.page.click(DashboardPageLocator.ADD_DASHBORD)
        self.page.click(DashboardPageLocator.CHOOSE_OPERATIVE_DASHBORD)
        self.page.fill(DashboardPageLocator.NAME_OPERATIVE_DASHBORD, name)
        self.page.click(DashboardPageLocator.BUTTON_SAVE_DASHBORD)

