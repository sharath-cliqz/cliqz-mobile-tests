from os import environ
from pages.testPage import TestPage
from pages.freshtabPage import FreshTab
from pages.vpnPage import VpnPage
from pages.webPage import WebPage
from pages.database import Database


class WebPerformance(TestPage,
                     FreshTab,
                     VpnPage,
                     WebPage,
                     Database):

    website_list = [
        "http://Google.com",
        "http://Youtube.com",
        "http://Google.de",
        "http://Amazon.de",
        "http://Facebook.com",
        "http://Ebay.de",
        "http://Wikipedia.org",
        "http://Ebay-kleinanzeigen.de",
        "http://Vk.com",
        "http://Mail.ru",
        "http://Yandex.ru",
        "http://Xhamster.com",
        "http://Livejasmin.com",
        "http://Instagram.com",
        "http://Twitter.com",
        "http://Paypal.com",
        "http://Web.de",
        "http://Ok.ru",
        "http://Gmx.net",
        "http://Yahoo.com",
        "http://Pornhub.com",
        "http://Spiegel.de",
        "http://Twitch.tv",
        "http://T-online.de",
        "http://Bild.de",
        "http://Google.ru",
        "http://Netflix.com",
        "http://Reddit.com",
        "http://Live.com",
        "http://Chip.de",
        "http://Bing.com",
        "http://Shop-apotheke.com",
        "http://Aliexpress.com",
        "http://Blogspot.com",
        "http://Otto.de",
        "http://Postbank.de",
        "http://Mobile.de",
        "http://Microsoft.com",
        "http://Focus.de",
        "http://Heise.de",
        "http://Immobilienscout24.de",
        "http://Idealo.de",
        "http://Xvideos.com",
        "http://Welt.de",
        "http://Github.com",
        "http://Amazon.com",
        "http://Zdf.de",
        "http://Bahn.de",
        "http://Pinterest.de",
        "http://Dhl.de"
    ]

    def web_performance(self, country=None):
        self.logger.info("*** Start Run ! ***")
        if not country:
            if environ.get("PERFORMANCE_COUNTRY") != "":
                country = environ.get("PERFORMANCE_COUNTRY")
            else:
                raise Exception("Country not Defined.")
        self.driver.launch_app()
        FreshTab.skip_intro(self)
        FreshTab.click_vpn_button(self)
        result = {}
        try:
            VpnPage.select_vpn_country(self, country)
            self.quick_wait(0.5)
            VpnPage.connect_vpn(self)
            self.quick_wait(3)
            try:
                for i in range(1, self.config["repeatCount"]+1):
                    reload_button = FreshTab.stop_reload_button(self)
                    self.logger.info("*** Run Number: {} ***".format(i))
                    for link in self.website_list:
                        address_bar = FreshTab.find_address_bar(self)
                        start_time = self.timestamp(True)
                        address_bar.set_value(link + "\n")
                        error_time = FreshTab.wait_for_reload_button(self, reload_button)
                        error = self.timestamp(True)
                        diff_time = error - start_time - error_time
                        result_time = round(diff_time.seconds + (diff_time.microseconds / 1000000), 2)
                        self.logger.info("{} ::: {}".format(link, result_time))
                        if i == 1:
                            result[link] = {}
                            result[link] = [result_time]
                        else:
                            result[link].append(result_time)
                        # Database.add_perf_result(self, country.lower(), link, result_time)
            except Exception as page_err:
                self.logger.error(page_err)
            FreshTab.click_vpn_button(self)
            VpnPage.disconnect_vpn(self)
            FreshTab.click_vpn_button(self)
            FreshTab.close_all_tabs(self)
            self.reset_browser()
        except Exception as vpn_err:
            self.logger.error(vpn_err)
        finally:
            self.quick_wait(0.5)
            # TODO: DataBase Entry
        with open("logs/result-{}.log".format(country), "w") as f:
            f.write("LINK :: (AVG) :: [RUN_TIMES]\n")
            for link in result:
                times = ", ".join([str(x) for x in result[link]])
                avg = round(sum(result[link]) / len(result[link]), 2)
                f.write("\n{} :: ({}) :: [{}]".format(link, avg, times))
        FreshTab.click_vpn_button(self)
        self.logger.info("*** Run Complete ***")

    def main(self, vpn_country=None):
        error = None
        try:
            self.init_all()
            self.web_performance(vpn_country)
        except Exception as error:
            self.logger.error(error)
        finally:
            self.quit_all()
            if error:
                raise error


if __name__ == "__main__":
    WebPerformance().main()
