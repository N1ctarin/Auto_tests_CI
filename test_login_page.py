from page.login_page import LoginPage


def test_autorizeitio_in_watchdog(browser):
    link = "https://iiot.ekfgroup.com/auth"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_name()
    page.should_be_password_name()
    page.input_email()
    page.input_password()
    page.input_button_in_click()
    page.should_name_EKF()
