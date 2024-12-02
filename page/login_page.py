from .base_page import BasePage
from .locators import LoginPageLocators
from .json_page import CreduForWatchdog
import json


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_name()
        self.should_be_password_name()
        self.find_input_button_in()
        self.input_email()
        self.input_password()
        self.shold_name_EKF()


    def should_be_login_url(self):
        assert "auth" in self.browser.current_url

    def should_be_login_name(self):
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_NAME)

    def should_be_password_name(self):
        assert self.browser.find_elements(*LoginPageLocators.PASSWORD_NAME)

    def input_email(self):
        tr = self.browser.find_elements(*LoginPageLocators.LOGIN_NAME)
        tr[0].send_keys(CreduForWatchdog.email)

    def input_password(self):
        tr = self.browser.find_elements(*LoginPageLocators.PASSWORD_NAME)
        tr[0].send_keys(*CreduForWatchdog.password)

    def input_button_in_click(self):
        self.browser.find_element(*LoginPageLocators.BUTTON_IN).click()

    def should_name_EKF(self):
        assert "EKF Connect Industry" in self.browser.find_element(*LoginPageLocators.NAME_EKF_ON_MAIN_PAGE).text