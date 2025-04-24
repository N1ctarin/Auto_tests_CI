from time import sleep
from conftest import browser
from page.Dashbord_page import DashbordPage
from page.Locators import LoginPageLocator, SettingsPageLocator, NotificationsPageLocator, ScriptsPageLocator,  \
        DashboardPageLocator
from page.Notifications_page import NotificationsPage
from page.Login_page import LoginPage
from page.json_page import Credu
from page.Main_page import MainPage
from page.Device_page import DevicePage
from page.Scripts_page import ScriptsPage
from page.Locators import DevicesPageLocator
from page.Locators import MainPageLocator
from page.json_page import DateForTesting
import pytest

b_url = ''

@pytest.fixture(scope="function")
def return_on_default_screen_project(request):
    page = request.getfixturevalue("browser")
    uri = b_url
    page.goto(uri)
    for i in range(5):
        if page.url == uri:
            break
        else:
            page.goto(uri)


class TestSuite:
        def test_login_in_stage(self, browser):
                link = "https://ekf-connect-industry.stage.iot.ekfgroup.com/auth"
                login_page = LoginPage(browser)
                login_page.open(link)
                login_page.enter_login(Credu.email)
                login_page.enter_password(Credu.password)
                login_page.click_login_button()
                login_page.check_visible_selector(LoginPageLocator.LOCATOR_EKF)
                assert login_page.is_check_success()

        def test_create_new_project(self, browser):
                main_page = MainPage(browser)
                main_page.push_button_creat_new_project()
                main_page.enter_name_new_project(DateForTesting.name_new_project)
                main_page.enter_description_new_project(DateForTesting.description_new_project)
                main_page.push_button_save_new_project()
                main_page.click_on_selector_with_text(DateForTesting.name_new_project)
                main_page.click_on_selector_with_text(DateForTesting.name_new_project)
                sleep(2)
                global b_url
                b_url = browser.url
                assert main_page.check_selector_on_space(MainPageLocator.PROJECT_NAME_SAVE_IN_TEXTSELECTOR)

        def test_create_new_dashbord(self, browser, return_on_default_screen_project):
                dashbord_page = DashbordPage(browser)
                dashbord_page.add_operative_dashbord_in_project(DateForTesting.name_dashbord)
                assert dashbord_page.check_selector_equals_text(DashboardPageLocator.NAME_OPERATIVE_DASHBORD_PARS_FROM_PROJECT, DateForTesting.name_dashbord)

        def test_check_folder_tags(self, browser, return_on_default_screen_project):
                device_page = DevicePage(browser)
                device_page.click_on_selector(DevicesPageLocator.DEVICES_BUTTON)
                assert device_page.check_selector_on_space(DevicesPageLocator.FOLDER_PROJECT_TAGS)

        def test_button_add_first_script(self, browser, return_on_default_screen_project):
                script_page = ScriptsPage(browser)
                script_page.click_on_selector(ScriptsPageLocator.SCRIPTS_BUTTON)
                assert script_page.check_selector_on_space('text="Добавить"')

        def test_check_templates_notifications(self, browser, return_on_default_screen_project):
                notifications_page = NotificationsPage(browser)
                notifications_page.click_on_selector(NotificationsPageLocator.NOTIFICATIONS_BUTTON)
                notifications_page.click_on_selector(NotificationsPageLocator.TEMPLATES_IN_NOTIFICATIONS)
                assert notifications_page.check_selector_on_space('text="Нарушение аварийных границ тега"')
                assert notifications_page.check_selector_on_space('text="Нарушение предупредительных границ тега"')
                assert notifications_page.check_selector_on_space('text="Завершение нарушения аварийных / предупредительных границ тега"')
                assert notifications_page.check_selector_on_space('text="Ошибка выполнения скрипта"')
                assert notifications_page.check_selector_on_space('text="Ошибка изменения исторических данных тега с помощью скрипта"')
                assert notifications_page.check_selector_on_space('text="Ошибка изменения тега с помощью скрипта"')
                assert notifications_page.check_selector_on_space('text="Тег в сети"')
                assert notifications_page.check_selector_on_space('text="Тег не в сети"')

        def test_check_tags_templates(self, browser, return_on_default_screen_project):
                device_page = DevicePage(browser)
                device_page.click_on_selector(DevicesPageLocator.DEVICES_BUTTON)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_ADD_TAGS)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_ADD_MODBUS_TAGS)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_ADD_MODBUS_TAGS_FROM_TEMPLATES)
                assert device_page.check_selector_equals_text(DevicesPageLocator.SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_PRO_RELE, "Группа регистров для PRO-Relay")
                assert device_page.check_selector_equals_text(DevicesPageLocator.SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_DMC, "Группа регистров для МФИ DMC-r")
                assert device_page.check_selector_equals_text(DevicesPageLocator.SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_SM_E, "Группа регистров для МФИ SM-E")
                assert device_page.check_selector_equals_text(DevicesPageLocator.SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_SM_H_SMG33H, "Группа регистров для МФИ SM-H, SM-G33H")

        def test_add_ePRO24_in_project(self, browser, return_on_default_screen_project):
                device_page = DevicePage(browser)
                device_page.click_on_selector(DevicesPageLocator.DEVICES_BUTTON)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_GATEWAY_EPRO24)
                device_page.add_access_to_broker(DevicesPageLocator.BUTTON_ADD_ACCESS_TO_BROKER_EPRO24, Credu.login_to_broker_ePRO24, Credu.password_to_broker)
                device_page.add_gateway_ePRO24_in_project(DateForTesting.name_gateway_in_project, DateForTesting.serial_number_gateway)
                assert device_page.check_selector_equals_text(DevicesPageLocator.SERIAL_NUMBER_GATEWAY_PARS_FROM_PROJECT, DateForTesting.serial_number_gateway)

        def test_add_MQTTgateway_in_project(self, browser, return_on_default_screen_project):
                device_page = DevicePage(browser)
                device_page.click_on_selector(DevicesPageLocator.DEVICES_BUTTON)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_GATEWAY_MQTT)
                device_page.add_access_to_broker(DevicesPageLocator.BUTTON_ADD_ACCESS_TO_BROKER_MQTT, Credu.login_to_broker_MQTT, Credu.password_to_broker)
                device_page.add_gateway_MQTT_in_project(DateForTesting.name_gateway_in_project)
                assert device_page.check_selector_equals_text(DevicesPageLocator.NAME_GATEWAY_MQTT_PARS_FROM_PROJECT, DateForTesting.name_gateway_in_project)

        def test_add_OPC_in_project(self, browser, return_on_default_screen_project):
                device_page = DevicePage(browser)
                device_page.click_on_selector(DevicesPageLocator.DEVICES_BUTTON)
                device_page.click_on_selector(DevicesPageLocator.BUTTON_OPC)
                device_page.add_OPC_in_project(Credu.name_opc, Credu.url_opc, Credu.login_OPC, Credu.password_OPC)
                assert device_page.check_selector_equals_text(DevicesPageLocator.NAME_OPC_PARS_FROM_PROJECT, Credu.name_opc)

        def test_delete_project(self, browser, return_on_default_screen_project):
                main_page = MainPage(browser)
                main_page.click_on_selector_without_waiting(DateForTesting.name_new_project)
                main_page.click_on_selector(SettingsPageLocator.SETTINGS_BUTTON)
                main_page.click_delete_project()
                assert main_page.is_not_element_present(MainPageLocator.PROJECT_NAME_SAVE_IN_TEXTSELECTOR)


#class TestOtladka(TestSuite):
#        def test_add_ePRO24_in_project(self, browser):
#                browser.goto('https://ekf-connect-industry.stage.iot.ekfgroup.com/p/439/dashboards/operational/530')
#                super().test_add_ePRO24_in_project(browser)

