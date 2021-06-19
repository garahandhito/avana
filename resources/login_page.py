from resources.common.utility import Utility
from selenium.webdriver.common.by import By


class LoginPageLocators(object):

    USERNAME_FIELD = (By.XPATH, '//main//input[@name="session[username_or_email]"]')
    PASSWORD_FIELD = (By.XPATH, '//main//input[@name="session[password]"]')
    SUBMIT_LOGIN_BTN = (By.XPATH, '//*[@data-testid="LoginForm_Login_Button"]')


class LoginPageController(Utility):

    def __init__(self, driver):
        Utility.__init__(self, driver)
        self.driver = driver

    def loginpage_is_displayed(self):
        self.wait_for_loading(LoginPageLocators.USERNAME_FIELD)
        self.wait_for_loading(LoginPageLocators.PASSWORD_FIELD)

    def input_username(self, username):
        self.type_to_field(LoginPageLocators.USERNAME_FIELD, username)

    def input_password(self, password):
        self.type_to_field(LoginPageLocators.PASSWORD_FIELD, password)

    def submit_login(self):
        self.click_item(LoginPageLocators.SUBMIT_LOGIN_BTN)

    def login_with_credentials(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit_login()
