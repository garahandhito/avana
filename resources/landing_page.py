from resources.common.utility import Utility
from selenium.webdriver.common.by import By


class LandingPageLocators(object):

    SIGNUP_BTN = (By.XPATH, '//*[@data-testid="signupButton"]')
    LOGIN_BTN = (By.XPATH, '//*[@data-testid="loginButton"]')


class LandingPageController(Utility):

    def __init__(self, driver):
        Utility.__init__(self, driver)
        self.driver = driver

    def go_to_twitter(self):
        self.driver.get('https://twitter.com')

    def landingpage_is_displayed(self):
        self.wait_for_loading(LandingPageLocators.SIGNUP_BTN)
        self.wait_for_loading(LandingPageLocators.LOGIN_BTN)

    def open_signup_page(self):
        self.click_item(LandingPageLocators.SIGNUP_BTN)

    def open_login_page(self):
        self.click_item(LandingPageLocators.LOGIN_BTN)
