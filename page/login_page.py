from playwright.sync_api import Page
from page.Locators import LoginPageLocator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, link):
        self.page.goto(link)

    def enter_login(self, login: str):
        self.page.fill(LoginPageLocator.POLE_LOGIN, login)

    def enter_password(self, password: str):
        self.page.fill(LoginPageLocator.POLE_PASSWORD, password)

    def click_login_button(self):
        self.page.click(LoginPageLocator.LOGIN_BUTTON)

    def enter_otp_1(self):
        self.page.fill(LoginPageLocator.OTP_1, '0')

    def enter_otp_2(self):
        self.page.focus(LoginPageLocator.OTP_2)
        self.page.press(LoginPageLocator.OTP_2)

    def enter_otp_3(self):
        self.page.fill(LoginPageLocator.OTP_3, "0")

    def enter_otp_4(self):
        self.page.fill(LoginPageLocator.OTP_4, "0")

    def is_check_success(self):
        return self.page.is_visible(LoginPageLocator.LOCATOR_EKF)

    def check_visible_selector(self, locator_check):
        self.page.wait_for_selector(locator_check)