from resources.common.utility import Utility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time


class HomepageLocators(object):

    TWEET = (By.XPATH, '//*[@data-testid="tweet"]')
    TWEET_TEXTAREA = (By.XPATH, '//*[@data-testid="tweetTextarea_0"]')
    FILE_INPUT = (By.XPATH, '//*[@data-testid="fileInput"]')
    SUBMIT_TWEET_BTN = (By.XPATH, '//*[@data-testid="tweetButtonInline"]')


class HomepageController(Utility):

    def __init__(self, driver):
        Utility.__init__(self, driver)
        self.driver = driver

    def homepage_is_displayed(self):
        self.wait_for_loading(HomepageLocators.TWEET)

    def type_tweet(self, text):
        self.type_to_field(HomepageLocators.TWEET_TEXTAREA, text)

    def type_unique_tweet(self):
        global ts
        ts = time.time()
        self.type_tweet('Tweeting at ' + str(ts))

    def attach_media(self, filepath):
        self.driver.find_element(*HomepageLocators.FILE_INPUT).send_keys(filepath)

    def submit_tweet(self):
        self.click_item(HomepageLocators.SUBMIT_TWEET_BTN)

    def tweet_is_displayed(self, tweet_message, media=False):
        try:
            WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located((By.XPATH, '//*[@data-testid="tweet"]//*[text()="' + tweet_message + '"]')))
            if media:
                WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_element_located((By.XPATH, '//*[@data-testid="tweet"]//*[text()="' + tweet_message + '"]/ancestor::node()[3]//*[@data-testid="tweetPhoto"]')))
        except TimeoutException:
            print('Tweet is not displayed')
            raise

    def unique_tweet_is_displayed(self, media=False):
        self.tweet_is_displayed('Tweeting at ' + str(ts), media)