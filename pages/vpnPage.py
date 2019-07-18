from pages.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MoBy


class VpnPage(BasePage):

    # ===============
    # Class Variables
    # ===============
    driver = None
    logger = None

    # ========
    # Locators
    # ========
    VPN_LOCATION_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "Choose VPN Location")}
    VPN_SELECTED_COUNTRY = {
        'ios': (MoBy.XPATH,
                "//XCUIElementTypeStaticText[@name='{}']/../XCUIElementTypeStaticText[@name!='{}']".format(
                    'Choose VPN Location', 'Choose VPN Location'
                ))
    }
    VPN_CONNECT_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "VPNButtonOutline")}
    VPN_ALLOW_BUTTON = {'ios': (MoBy.XPATH, "//XCUIElementTypeButton[@name='Allow']")}

    # THIS IS A METHOD TO GET THE VPN LIST LOCATOR
    @classmethod
    def get_vpn_locator(cls, country):
        return MoBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '{}')]".format(country)

    # ============
    # Page Methods
    # ============

    def get_vpn_location_button(self):
        return self.get_element(self.VPN_LOCATION_BUTTON, timeout=5)

    def get_country_elem(self, country):
        return self.get_element(self.get_vpn_locator(country), timeout=10)

    def get_selected_country_elem(self):
        return self.get_element(self.VPN_SELECTED_COUNTRY, timeout=5)

    def get_vpn_selected_country(self):
        return self.get_selected_country_elem().text

    def select_vpn_country(self, country):
        self.get_vpn_location_button().click()
        self.logger.info("Setting the VPN Location to: {}".format(country))
        count = 0
        while not self.get_country_elem(country).is_displayed() and count < 10:
            self.mobile_scroll("up")
            count += 1
        self.get_country_elem(country).click()

    def connect_vpn(self):
        if self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") != "disconnected":
            self.disconnect_vpn()
        self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).click()
        self.allow_vpn_connection()
        timer = self.timestamp()
        vpn_states = ["disconnected", "connecting"]
        while self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") in vpn_states and \
                (self.timestamp() - timer).seconds < 10:
            self.quick_wait(0.5)
        return self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") == "connected"

    def disconnect_vpn(self):
        if self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") == "connected":
            self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).click()
            timer = self.timestamp()
            while self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") != "disconnected" and \
                    (self.timestamp() - timer).seconds < 10:
                self.quick_wait(0.5)
        return self.get_element(self.VPN_CONNECT_BUTTON, timeout=5).get_attribute("value") == "disconnected"

    def allow_vpn_connection(self):
        try:
            self.get_element(self.VPN_ALLOW_BUTTON, timeout=5).click()
        except Exception as e:
            self.logger.error(e)
