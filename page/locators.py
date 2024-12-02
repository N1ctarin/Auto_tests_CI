from  selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_NAME = (By.NAME, "login")
    PASSWORD_NAME = (By.NAME, "password")
    BUTTON_IN = (By.CSS_SELECTOR, '.C1RLE.theme--primary.size--m')
    NAME_EKF_ON_MAIN_PAGE = (By.CLASS_NAME, 'nrlsb')