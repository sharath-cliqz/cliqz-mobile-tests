from pages.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MoBy


class FreshTab(BasePage):

    # ===============
    # Class Variables
    # ===============
    driver = None
    logger = None
    intro_complete = False

    # ========
    # Locators
    # ========
    SKIP_INTRO_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "IntroViewController.skipIntroButton")}
    TABS_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "TabToolbar.tabsButton")}
    DONE_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "TabTrayController.doneButton")}
    CLOSE_ALL_TABS_CONFIRMATION = {'ios': (MoBy.ACCESSIBILITY_ID, "TabTrayController.deleteButton.closeAll")}
    URL_BAR = {'ios': (MoBy.ACCESSIBILITY_ID, "url")}
    ADDRESS_BAR = {'ios': (MoBy.ACCESSIBILITY_ID, "address")}
    STOP_RELOAD_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "TabToolbar.stopReloadButton")}
    VPN_BUTTON = {'ios': (MoBy.ACCESSIBILITY_ID, "vpnButton")}

    # ============
    # Page Methods
    # ============

    def enable_address_bar(self):
        try:
            address_bar = self.get_element(self.ADDRESS_BAR, timeout=1)
            address_bar.click()
            return address_bar
        except Exception as e:
            try:
                self.logger.error(e)
                self.get_element(self.URL_BAR, timeout=1).click()
                return self.get_element(self.ADDRESS_BAR, timeout=1)
            except Exception as e:
                self.logger.error(e)
                raise Exception("Address Bar could not be Enabled/Does not Exist.")

    def find_address_bar(self):
        self.skip_intro()
        return self.enable_address_bar()

    def wait_for_reload_button(self, button=None):
        button = self.stop_reload_button() if not button else button
        timer = self.timestamp(True)
        while (not button.text == "Reload") and ((self.timestamp(True) - timer).seconds < 60):
            timer = self.timestamp()
            self.quick_wait(0.25)
        return self.timestamp(True) - timer

    def stop_reload_button(self):
        return self.get_element(self.STOP_RELOAD_BUTTON, timeout=1)

    def skip_intro(self):
        if not self.intro_complete:
            try:
                self.get_element(self.SKIP_INTRO_BUTTON, timeout=1).click()
                self.logger.info("Skipped Intro.")
            except Exception as e:
                self.logger.error(e)
                self.logger.info("Seems like Intro did not appear.")
            self.intro_complete = True
        else:
            self.logger.info("Intro already Skipped.")

    def reset_browser(self):
        self.driver.reset()
        self.intro_complete = False
        self.quick_wait(1)

    def close_all_tabs(self):
        self.open_tabs_overview()
        self.long_press(self.get_element(self.DONE_BUTTON))
        try:
            self.get_element(self.CLOSE_ALL_TABS_CONFIRMATION).click()
        except Exception as e:
            self.logger.error(e)
            self.long_press(self.get_element(self.DONE_BUTTON))
            self.get_element(self.CLOSE_ALL_TABS_CONFIRMATION).click()
        self.quick_wait(1)

    def open_tabs_overview(self):
        self.get_element(self.TABS_BUTTON).click()

    def click_vpn_button(self):
        self.get_element(self.VPN_BUTTON).click()
