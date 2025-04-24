from typing import override

from playwright.sync_api import Page
from page.Base_page import BasePage
from page.Locators import DevicesPageLocator


class DevicePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @override
    def check_selector_equals_text(self, selector, text):
        self.page.wait_for_selector(selector, state='visible')
        d = (self.page.text_content(selector)).rstrip()
        return d == text

    def add_access_to_broker(self, locator, login, password):
        self.page.click(locator)
        self.page.fill(DevicesPageLocator.LOGIN_BROKER_ACCESS, login)
        self.page.fill(DevicesPageLocator.PASSWORD_BROKER_ACCESS, password)
        self.page.fill(DevicesPageLocator.PASSWORD_REPEAT_BROKER_ACCESS, password)
        self.page.click(DevicesPageLocator.BUTTON_SAVE_BROKER_ACCESS)

    def add_gateway_ePRO24_in_project(self, name_gateway, serial_number):
        self.page.click(DevicesPageLocator.BUTTON_ADD_NEW_GATEWAY_EPRO24_IN_PROJECT)
        self.page.fill(DevicesPageLocator.NAME_GATEWAY_IN_PROJECT, name_gateway)
        self.page.fill(DevicesPageLocator.SERIAL_NUMBER_GATEWAY_IN_PROJECT, serial_number)
        self.page.click(DevicesPageLocator.BUTTON_SAVE_GATEWAY_IN_PROJECT)

    def add_gateway_MQTT_in_project(self, name_gateway):
        self.page.click(DevicesPageLocator.BUTTON_ADD_NEW_GATEWAY_MQTT_IN_PROJECT)
        self.page.fill(DevicesPageLocator.NAME_GATEWAY_IN_PROJECT, name_gateway)
        self.page.click(DevicesPageLocator.BUTTON_SAVE_MQTT_GATEWAY_IN_PROJECT)

    def add_OPC_in_project(self, name_opc, url, login_opc, password_opc):
        self.page.click(DevicesPageLocator.BUTTON_ADD_OPC)
        self.page.fill(DevicesPageLocator.NAME_GATEWAY_IN_PROJECT, name_opc)
        self.page.fill(DevicesPageLocator.URL_OPC, url)
        self.page.fill(DevicesPageLocator.LOGIN_OPC, login_opc)
        self.page.fill(DevicesPageLocator.PASSWORD_OPC, password_opc)
        self.page.click(DevicesPageLocator.SAVE_ADD_OPC_IN_PROJECT)


