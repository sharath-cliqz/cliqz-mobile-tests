import os
import datetime
import time
from appium import webdriver as WD
from src.logger import Logger
from src.configure import Configure
from src.elements import Elements
from src.browser import Browser

class Driver(Logger, Configure, Elements, Browser):

    def startDriver(self):
        Logger.__init__(self, name='[Web-Performance]')
        Configure.__init__(self, os.environ.get('CONFIG_FILE', 'lumen.config'))
        self.log("WebDriver request initiated. Waiting for response, this typically takes 2-3 mins")
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.log("Start Time: {}".format(time.strftime("%H:%M:%S")))
        self.driver = WD.Remote(self.appiumServer, self.desiredCaps)
        end_time = datetime.datetime.now().replace(microsecond=0)
        self.log("WebDriver response received at: {}".format(time.strftime("%H:%M:%S")))
        self.log("Time Taken to Launch Appium: {}".format(end_time - self.start_time))

    def quitDriver(self):
        self.sleep(5)
        self.log("Quitting Driver")
        self.end_time = datetime.datetime.now().replace(microsecond=0)
        self.log("End Time: {}".format(time.strftime("%H:%M:%S")))
        self.log("Test Run Time: {}".format(self.end_time-self.start_time))
        self.driver.quit()

    def sleep(self, secs):
        time.sleep(secs)