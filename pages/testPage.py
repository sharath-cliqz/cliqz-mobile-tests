import logging
import json

from appium import webdriver
from os.path import join
from os.path import dirname
from os import environ
from datetime import datetime
from time import sleep
from subprocess import Popen, PIPE


class TestPage:

    # ===============
    # Class Variables
    # ===============
    appium = None
    driver = None
    logger = None
    driver_start_time = None
    config = {}
    handler = None

    # ============
    # Time Methods
    # ============
    @classmethod
    def timestamp(cls, microseconds=False):
        return datetime.now() if microseconds else datetime.now().replace(microsecond=0)

    @classmethod
    def quick_wait(cls, seconds=0.1):
        sleep(seconds)

    # ==============
    # Logger Methods
    # ==============
    @classmethod
    def init_logger(cls):
        if not cls.logger:
            cls.logger = logging.getLogger("vpn-test")
            cls.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(funcName)s(%(lineno)d)] :: %(message)s')
            formatter.default_time_format = '%H:%M:%S'
            cls.handler = logging.StreamHandler()
            cls.handler.setLevel(logging.DEBUG)
            cls.handler.setFormatter(formatter)
            cls.logger.addHandler(cls.handler)

    @classmethod
    def quit_logger(cls):
        try:
            cls.logger.info("Closing Logger.")
            cls.logger.removeHandler(cls.handler)
        except Exception as e:
            print("*** Error Removing Logger Handler. Error: {} ***\n\n\n".format(e))
        cls.logger = None

    # ==============
    # Appium Methods
    # ==============
    @classmethod
    def init_appium(cls):
        cls.appium = Popen("npm run appium-server".split(), stdout=PIPE, stderr=PIPE)
        cls.logger.info("Started Appium")
        cls.quick_wait(5)

    @classmethod
    def quit_appium(cls):
        cls.logger.info("Quitting Appium")
        cls.appium.terminate()
        cls.quick_wait(3)

    # ==============
    # Driver Methods
    # ==============
    @classmethod
    def init_driver(cls):
        cls.config = cls.config_data(environ.get("TEST_CONFIG", "lumen.config"), '../configs')
        cls.logger.info("WebDriver request initiated. Waiting for response, this typically takes 2-3 mins")
        cls.driver_start_time = cls.timestamp()
        cls.logger.info("Start Time: {}".format(cls.timestamp()))
        if environ.get("WEB_DRIVER_AGENT") != "":
            cls.logger.info("Found ENV for Web Driver Agent: {}".format(environ.get("WEB_DRIVER_AGENT")))
            cls.config['desiredCaps']['derivedDataPath'] = environ.get("WEB_DRIVER_AGENT")
        cls.driver = webdriver.Remote(cls.config['appiumServer'], cls.config['desiredCaps'])
        cls.logger.info("WebDriver response received at: {}".format(cls.timestamp()))
        cls.logger.info("Time Taken to Launch Appium: {}".format(cls.timestamp() - cls.driver_start_time))

    @classmethod
    def quit_driver(cls):
        cls.logger.info("Quitting Driver")
        cls.logger.info("End Time: {}".format(cls.timestamp()))
        cls.logger.info("Test Run Time: {}".format(cls.timestamp() - cls.driver_start_time))
        cls.driver.quit()

    # =============
    # Combi Methods
    # =============
    @classmethod
    def init_all(cls):
        cls.init_logger()
        cls.init_appium()
        cls.init_driver()

    @classmethod
    def quit_all(cls):
        try:
            cls.quit_driver()
        finally:
            cls.quit_appium()
            cls.quit_logger()

    # ===========
    # Config Data
    # ===========
    @classmethod
    def read_json(cls, filename, directory=""):
        relative_path = join(directory, filename)
        absolute_path = join(dirname(__file__), relative_path)
        with open(absolute_path) as config_file:
            return json.loads(config_file.read())

    @classmethod
    def config_data(cls, filename, directory=""):
        return cls.read_json(filename, directory)

    # ==============
    # Assert Methods
    # ==============
    def assert_equal(self, first, second, msg=None):
        try:
            if type(second) == list:
                assert first in second
            else:
                assert first == second
            self.logger.info("Assert [{}] :: {} == {} ? Result :: True".format(msg, first, second))
        except AssertionError as ae:
            self.logger.error("Assertion ERROR !!\n[{}]\nActual: {}\nExpected: {}".format(msg, first, second))
            raise ae

    def assert_not_equal(self, first, second, msg=None):
        try:
            assert first != second
            self.logger.info("Assert [{}] :: {} != {} ? Result :: True".format(msg, first, second))
        except AssertionError as ae:
            self.logger.error("Assertion ERROR !!\n[{}]\nActual: {}\nNOT Expected: {}".format(msg, first, second))
            raise ae
