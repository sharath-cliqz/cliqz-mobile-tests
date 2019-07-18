from pages.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MoBy
from json import loads


class WebPage(BasePage):

    # ===============
    # Class Variables
    # ===============
    driver = None
    logger = None

    # ========
    # Locators
    # ========
    PAGE_CONTENT = {'ios': (MoBy.XPATH, "//XCUIElementTypeWebView//XCUIElementTypeStaticText")}

    # ============
    # Page Methods
    # ============
    def get_web_content(self):
        return self.get_element(self.PAGE_CONTENT, timeout=1).text

    def get_location(self):
        temp_json = loads(self.get_web_content())
        return temp_json['location.granular']

    def print_location(self):
        self.logger.info(self.get_location())
