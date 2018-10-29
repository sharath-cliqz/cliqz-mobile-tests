from utils import AllUtils
from time import sleep
import unittest, os, sys, datetime, xmlrunner, importlib
from common.settings import Settings
#from testSuites.testCompleteSuite import CompleteSuite
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from pages.pageOnboarding import Onboarding

if os.environ.get('TEST_TYPE') == "performance":
    mainPackage = "performanceSuites."
else:
    mainPackage = "testSuites."

reload(sys)
sys.setdefaultencoding('utf8')

class TestRunner(getattr(importlib.import_module(mainPackage+os.environ.get('MODULE')), os.environ.get('TEST')), AllUtils, unittest.TestCase):
#class TestRunner(CompleteSuite, AllUtils, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.settings = Settings()
        cls.driver = cls.settings.getDriver()
        if cls.settings.platform_name == "android" and os.environ.get('TEST_TYPE') != "debug": cls.driver.reset()

    def setUp(self):
        self.settings.featureTestCount = {'total': 0, 'pass': 0, 'fail': 0, 'skip': 0}
        self.screenshot_dir = os.getcwd() + "/screenshots"
        self.log("Will save screenshots at: " + self.screenshot_dir)
        if not os.path.exists(self.screenshot_dir):
            self.log('Creating directory %s' % self.screenshot_dir)
            os.mkdir(self.screenshot_dir)
        self.settings.screenshot_count = 1
        self.test_start_time = datetime.datetime.now().replace(microsecond=0)
        if self.settings.result_check == (1, 1, 1):
            self.settings.result_check = (None, None, None)
        if (self.settings.result_check != (None, None, None)) and ("SkipTest" not in str(self.settings.result_check)):
            self.driver.launch_app()
            if os.environ.get("TEST_TYPE") != "performance":
                self.log("!!!! PERFORMING SPECIAL CLEANUP !!!!")
                self.driver.reset()
                self.sleep(3)
                Onboarding(self.settings).startBrowsing()
                #if self.isPlatform("android"):
                    #FreshTab(self.settings).clearAndCancelAddressBar()
                self.sleep(5)
        #self.settings.specialCleanUp = False

    def tearDown(self):
        testName = str(self.id()).split(".")[-1]
        self.test_end_time = datetime.datetime.now().replace(microsecond=0)
        result = sys.exc_info()
        self.settings.result_check = result
        self.log("Test Case Execution Complete !")
        self.log("Test Execution Time:  " + str(self.test_end_time - self.test_start_time))
        self.log("Test Case Error: " + str(result[1]) + "\n")
        if result != (None, None, None):
            if "SkipTest" in str(result):
                self.settings.featureTestCount['total'] += 1
                self.settings.featureTestCount['skip'] += 1
            else:
                self.screenshot("Test End Screenshot", override=True)
                self.sleep(2)
                self.driver.close_app()
        self.log("| Total: " + str(self.settings.featureTestCount['total']) + " | Pass: " + str(
            self.settings.featureTestCount['pass']) + " | Fail: " + str(self.settings.featureTestCount['fail']) + " | Skipped: " + str(
            self.settings.featureTestCount['skip']) + " |\n\n")
        self.settings.testCount['total'] += self.settings.featureTestCount['total']
        self.settings.testCount['pass'] += self.settings.featureTestCount['pass']
        self.settings.testCount['fail'] += self.settings.featureTestCount['fail']
        self.settings.testCount['skip'] += self.settings.featureTestCount['skip']
        sleep(2)
        self.getTelemetryLogs()

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        # telemetryFile = open("telemetry.log", "w")
        # for event in cls.settings.eventsList: DeviceUtils().prettyPrintEvents(event, telemetryFile)
        # telemetryFile.close()
        deviceLogFile = open(cls.settings.app_brand+"devicelog.log", "w")
        for item in cls.settings.fullLog: deviceLogFile.write(str(item['message']) + "\n")
        deviceLogFile.close()
        end_time = datetime.datetime.now().replace(microsecond=0)
        endString = "\n\n*** TEST SUITE EXECUTION COMPLETE !! *** \n\n"
        endString += "Total Time taken by the Test Suite: " + str(end_time - cls.settings.start_time) + "\n\n"
        endString += "| Total: " + str(cls.settings.testCount['total']) + " | Pass: " + str(cls.settings.testCount['pass']) + " | Fail: " + str(
            cls.settings.testCount['fail']) + " | Skipped: " + str(cls.settings.testCount['skip']) + " |\n"
        print endString
        cls.settings.prettyPrintReport()
        reportFileName = os.environ.get('reportFile') or "testreport.log"
        reportFile = open(cls.settings.app_brand+reportFileName, "w")
        cls.settings.writeReport(reportFile, endString)
        reportFile.close()



if __name__ == "__main__":
    #suite = unittest.TestLoader().loadTestsFromModule(TestScript)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    device_type = (os.environ.get('deviceType') or "default").replace(" ", "")
    device_name = (os.environ.get('realDeviceName')\
                  or os.environ.get('platformName')\
                  or os.environ.get('TESTDROID_PLATFORM')).replace(" ", "")
    device_os_ver = (os.environ.get('deviceOSVer') or "0.0").replace(" ", "")
    app_brand = "Cliqz-" if "cliqz" in (os.environ.get('appPackage') or os.environ.get('bundleID') or os.environ.get('TESTDROID_BUNDLE_ID')).lower() else "Ghostery-"
    outSuffix = app_brand + device_name + "-" + device_os_ver + "-" + device_type
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports', outsuffix=outSuffix))