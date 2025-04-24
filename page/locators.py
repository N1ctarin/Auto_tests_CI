from page.json_page import DateForTesting

class LoginPageLocator:
    POLE_LOGIN = 'input[name="login"]'
    POLE_PASSWORD = 'input[name="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'
    LOCATOR_EKF = '._projectTitle_1u7g0_25'
    OTP_1 = '//*[name()="input"][1]'
    OTP_2 = '//*[name()="input"][2]'
    OTP_3 = '//*[name()="input"][3]'
    OTP_4 = '//*[name()="input"][4]'

class MainPageLocator:
    BUTTON_CREAT_NEW_PROJECT = ' //div[@class="_projectsControls_1u7g0_43"]/descendant::button'
    NAME_NEW_PROJECT = 'input[name="title"]'
    DESCRIPTION_NEW_PROJECT = 'textarea[name="description"]'
    SAVE_NEW_PROJECT_BUTTON = 'button[type="submit"]'
    DELETE_BUTTON = 'button[type="submit"]'
    PROJECT_NAME_SAVE_IN_TEXTSELECTOR = f'text= "{DateForTesting.name_new_project}"'

class DevicesPageLocator:
    FOLDER_PROJECT_TAGS = '._plate_1tm1c_24'
    BUTTON_ADD_TAGS = '._root_1by0k_1.theme--primary.size--s'
    BUTTON_ADD_MODBUS_TAGS = '//div[@class="_dropdown_nutxt_7"]/descendant::div[1]'
    BUTTON_ADD_MODBUS_TAGS_FROM_TEMPLATES = '//div[@class="_header_1d731_9"]/button[2]'
    SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_PRO_RELE = '//div[@class="_area_9xzej_50"]/div[1]'
    SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_DMC = '//div[@class="_area_9xzej_50"]/div[2]'
    SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_SM_E = '//div[@class="_area_9xzej_50"]/div[3]'
    SELECTOR_TEMPLATES_MODBUS_TAGS_REGISTR_MFI_SM_H_SMG33H = '//div[@class="_area_9xzej_50"]/div[4]'
    DEVICES_BUTTON = '//nav[@class="_root_9clbt_1"]/a[2]'
    BUTTON_GATEWAY_EPRO24 = '//nav[contains(@class, "_container_1rsbt_1")]/a[2]'
    BUTTON_ADD_ACCESS_TO_BROKER_EPRO24 = '//div[@class="_headerControls_f0b9s_32"]/button'
    LOGIN_BROKER_ACCESS = 'input[name="userName"]'
    PASSWORD_BROKER_ACCESS = 'input[name="password"]'
    PASSWORD_REPEAT_BROKER_ACCESS = 'input[name="repeatPassword"]'
    BUTTON_SAVE_BROKER_ACCESS = '//div[@class="_formRow_1wv1k_23"][4]/button'
    BUTTON_ADD_NEW_GATEWAY_EPRO24_IN_PROJECT = '//div[@class="_headerControls_f0b9s_32"]/button'
    NAME_GATEWAY_IN_PROJECT = 'input[name="name"]'
    SERIAL_NUMBER_GATEWAY_IN_PROJECT = 'input[name="serial"]'
    BUTTON_SAVE_GATEWAY_IN_PROJECT = '//div[@class="_controls_qr2ky_28"]/button'
    SERIAL_NUMBER_GATEWAY_PARS_FROM_PROJECT = '//tr[@class="_root_10ld9_1"]/td[1]'
    BUTTON_GATEWAY_MQTT = '//nav[contains(@class, "_container_1rsbt_1")]/a[3]'
    BUTTON_ADD_NEW_GATEWAY_MQTT_IN_PROJECT = '//div[@class="_headerControls_2bb9a_28"]/button'
    BUTTON_SAVE_MQTT_GATEWAY_IN_PROJECT = '//div[@class="_controls_qof1s_21"]/button'
    NAME_GATEWAY_MQTT_PARS_FROM_PROJECT = '//tr[@class="_root_10ld9_1"]/td[1]/div'
    BUTTON_ADD_ACCESS_TO_BROKER_MQTT = '//div[@class="_headerControls_2bb9a_28"]/button'
    BUTTON_OPC = '//nav[contains(@class, "_container_1rsbt_1")]/a[4]'
    BUTTON_ADD_OPC = '//div[@class="_header_1cpxm_13"]/button'
    URL_OPC = 'input[name="url"]'
    LOGIN_OPC = 'input[name="login"]'
    PASSWORD_OPC = 'input[name="password"]'
    SAVE_ADD_OPC_IN_PROJECT = '//div[@class="_controls_ygk2m_46"]/button'
    NAME_OPC_PARS_FROM_PROJECT = '//tr[@class="_root_10ld9_1"]/td[1]'


class DashboardPageLocator:
    DASHBORD_BUTTON = '//nav[@class="_root_9clbt_1"]/a[1]'
    ICON_DASHBORD = '._toggle_1vuhj_1'
    ADD_DASHBORD = '//div[@class="_controls_1vuhj_72"]/button'
    CHOOSE_OPERATIVE_DASHBORD = '//div[@class="_list_1vuhj_37"]/div[1]'
    NAME_OPERATIVE_DASHBORD = 'input[name="title"]'
    BUTTON_SAVE_DASHBORD = '//div[@class="_actions_1vl4p_13"]/button'
    NAME_OPERATIVE_DASHBORD_PARS_FROM_PROJECT = '//div[@class="_info_1wv2s_9"]/h2'

class SettingsPageLocator:
    SETTINGS_BUTTON = '//nav[@class="_root_9clbt_1"]/a[6]'

class NotificationsPageLocator:
    NOTIFICATIONS_BUTTON = '//nav[@class="_root_9clbt_1"]/a[4]'
    TEMPLATES_IN_NOTIFICATIONS = '//nav[contains(@class, "_container_1rsbt_1")]/a[2]'

class ScriptsPageLocator:
    SCRIPTS_BUTTON = '//nav[@class="_root_9clbt_1"]/a[3]'