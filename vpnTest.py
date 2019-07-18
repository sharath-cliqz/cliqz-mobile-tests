from pages.testPage import TestPage
from pages.freshtabPage import FreshTab
from pages.vpnPage import VpnPage
from pages.webPage import WebPage
from pages.database import Database
from ddt import ddt, data

import unittest
import xmlrunner


@ddt
class VpnTest(unittest.TestCase,
              TestPage,
              FreshTab,
              VpnPage,
              WebPage,
              Database):

    DEFAULT_LOCATION = "de"
    VPN_LOCATIONS = {
        "Austria": "at",
        "Bosnia": "ba",
        "Bulgaria": "bg",
        "Canada": "ca",
        "Croatia": "hr",
        "France": "fr",
        "Germany": "de",
        "Greece": "gr",
        "Hungary": "hu",
        "India": "in",
        "Italy": "it",
        "Netherlands": "nl",
        "Poland": "pl",
        "Portugal": "pt",
        "Romania": "ro",
        "Serbia": "rs",
        "Spain": "es",
        "Turkey": "tr",
        "Ukraine": "ua",
        "UK": ["uk", "nl"],
        "USA": "us",
        "Viet Nam": "vn",
    }
    FAILED_COUNTRIES = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.init_all()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.quit_all()

    def check_vpn(self, country, expected_loc):
        self.logger.info("\n*** Testing VPN for {} ***\n".format(country))
        self.driver.launch_app()
        FreshTab.skip_intro(self)
        status = False
        vpn_connection = False
        FreshTab.click_vpn_button(self)
        try:
            VpnPage.select_vpn_country(self, country)
            self.quick_wait(0.5)
            vpn_connection = VpnPage.connect_vpn(self)
            if not vpn_connection:
                raise Exception("VPN Not Connected")
            self.quick_wait(3)
            address_bar = FreshTab.find_address_bar(self)
            address_bar.set_value("https://api.cliqz.com/api/v1/config" + "\n")
            FreshTab.wait_for_reload_button(self)
            new_location = WebPage.get_location(self)
            if country != "Germany":
                self.assert_not_equal(new_location, self.DEFAULT_LOCATION, "Check that the Location is not the Default")
            self.assert_equal(new_location, expected_loc, "Check that the Location is as expected")
            status = True
            WebPage.print_location(self)
            FreshTab.click_vpn_button(self)
        except Exception as e:
            self.logger.error(e)
            self.driver.launch_app()
        finally:
            if vpn_connection:
                VpnPage.disconnect_vpn(self)
            self.quick_wait(0.5)
            # Database.update_status(self, country.lower(), status)
            FreshTab.click_vpn_button(self)
            self.logger.info("\n*** Test Run for {} Complete ***\n".format(country))
            if not status:
                raise Exception("\n\nERROR IN {}'s VPN CONNECTION !!\n\n".format(country))

    @data(*(country for country in VPN_LOCATIONS))
    def test_00_initial(self, country):
        try:
            self.check_vpn(country, self.VPN_LOCATIONS[country])
        except Exception as e:
            self.logger.error(e)
            self.FAILED_COUNTRIES[country] = self.VPN_LOCATIONS[country]

    @data(*(country for country in VPN_LOCATIONS))
    def test_01_retry(self, country):
        if country in self.FAILED_COUNTRIES:
            try:
                self.check_vpn(country, self.VPN_LOCATIONS[country])
            except Exception as e:
                self.logger.error(e)
                self.FAILED_COUNTRIES[country] = self.VPN_LOCATIONS[country]
        else:
            self.logger.info("*** VPN Test for {} was Passed in the initial Try ***".format(country.upper()))


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports', outsuffix="VPN-STATUS"))
