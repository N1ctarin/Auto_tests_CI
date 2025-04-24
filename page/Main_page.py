from playwright.sync_api import Page
from page.Base_page import BasePage
from page.Locators import MainPageLocator

class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def push_button_creat_new_project(self):
        self.page.click(MainPageLocator.BUTTON_CREAT_NEW_PROJECT)

    def enter_name_new_project(self, name):
        self.page.fill(MainPageLocator.NAME_NEW_PROJECT, name)

    def enter_description_new_project(self, descriptions):
        self.page.fill(MainPageLocator.DESCRIPTION_NEW_PROJECT, descriptions)

    def push_button_save_new_project(self):
        self.page.click(MainPageLocator.SAVE_NEW_PROJECT_BUTTON)

    def click_delete_project(self):
        BasePage.click_on_selector_with_text(self," Удалить проект")
        self.page.click(MainPageLocator.DELETE_BUTTON)
