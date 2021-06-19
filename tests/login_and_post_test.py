import os
import pytest
from selenium import webdriver
from resources import home_page
from resources import landing_page
from resources import login_page


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path='tests/drivers/chromedriver', options=options)


@pytest.fixture(autouse=True)
def setup_teardown():
    landing = landing_page.LandingPageController(driver)
    login = login_page.LoginPageController(driver)
    landing.go_to_twitter()
    landing.landingpage_is_displayed()
    landing.open_login_page()
    login.loginpage_is_displayed()
    login.login_with_credentials('@DummyRahmat', 'Kmzw4y87a@')
    yield
    driver.quit()


def test_login_and_post():
    home = home_page.HomepageController(driver)
    home.homepage_is_displayed()
    home.type_unique_tweet()
    home.attach_media(os.getcwd() + "./tests/test_files/robot-icons.png")
    home.submit_tweet()
    home.unique_tweet_is_displayed(media=True)
