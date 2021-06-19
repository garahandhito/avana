from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class Utility(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_checking(self, locator, timeout=5, message=''):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            print(message)
            raise

    def wait_for_loading(self, locator, timeout=5, message=''):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(message)
            raise

    def click_item(self, locator):
        item = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(item)
        action.click(item)
        action.perform()

    def type_to_field(self, locator, text):
        field = self.driver.find_element(*locator)
        self.click_item(locator)
        field.clear()
        field.send_keys(text)
