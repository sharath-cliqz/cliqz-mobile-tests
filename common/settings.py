import os, logging, datetime, time
from appium import webdriver as WD
from reportGenerator import ReportGenerator
from gecko.geckoConnect import GeckoDriver

class Settings:

    instance = None

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    referenceApk = os.path.realpath(scriptDir + '/../referenceApp/referenceApp.apk')
    deviceInduceSleep = 2
    implicitWaitTime = 5
    recordLogs = True
    takeScreenshot = False
    appiumServer = 'http://localhost:4723/wd/hub'
    platform_name = os.environ.get('platformName') or os.environ.get('TESTDROID_PLATFORM')
    device_type = os.environ.get('deviceType') or "default"
    device_name = os.environ.get('realDeviceName') or os.environ.get('deviceName')
    device_os_ver = os.environ.get('deviceOSVer') or os.environ.get('platformVersion') or "0.0"

    desired_caps_ios = {
        'platformName':'iOS',
        'bundleId': os.environ.get('bundleID'),
        "automationName": "XCUITest",
        'udid': os.environ.get('udid'),
        'deviceName': os.environ.get('deviceName'),
        'platformVersion' : os.environ.get('platformVersion'),
        'noReset' : True
    }

    desired_caps_android = {
        "platformName": "android",
        "appPackage": os.environ.get('appPackage'),
        "appActivity": os.environ.get('appActivity'),
        "deviceName": os.environ.get('deviceName'),
        "automationName": "UiAutomator2",
        "app": os.environ.get('app') or referenceApk,
        "noReset" : True
    }

    desired_capabilities_cloud = {
        'testdroid_apiKey': os.environ.get('TESTDROID_APIKEY'),
        'appium_url': os.environ.get('TESTDROID_URL') or appiumServer,
        'testdroid_target': platform_name.lower(),
        'testdroid_project': os.environ.get('TESTDROID_PROJECT'),
        'testdroid_testrun': os.environ.get('TESTDROID_TESTRUN'),
        'testdroid_device': os.environ.get('TESTDROID_DEVICE'),
        'testdroid_app': os.environ.get('TESTDROID_APP'),
        'platformName': platform_name,
        'deviceName': os.environ.get('TESTDROID_DEVICE'),
        'newCommandTimeout': os.environ.get('TESTDROID_CMD_TIMEOUT') or '60',
        'testdroid_testTimeout': os.environ.get('TESTDROID_TEST_TIMEOUT') or '1800',
        #'testdroid_findDevice': testdroid_find_device,
        'automationName': os.environ.get('TESTDROID_AUTOMATION'),
        'app': os.environ.get('TESTDROID_APP'),
        'noReset': True
    }
    if platform_name == 'ios':
        desired_capabilities_cloud['bundleID'] = os.environ.get('TESTDROID_BUNDLE_ID')
    elif platform_name == 'android':
        desired_capabilities_cloud['appPackage'] = os.environ.get('TESTDROID_BUNDLE_ID')
        desired_capabilities_cloud['appActivity'] = os.environ.get('TESTDROID_MAIN_ACTIVITY') or ".main.MainActivity"

    onBoardingComplete = False
    screenshot_count = 1

    result_check = (1, 1, 1)
    specialCleanUp = False
    eventsList = []
    fullLog = []
    fullReport = {}

    testCount = {'total': 0, 'pass': 0, 'fail': 0, 'skip': 0}
    featureTestCount = {'total': 0, 'pass': 0, 'fail': 0, 'skip': 0}

    def __init__(self):
        self.app_brand = "Cliqz-" if "cliqz" in (
                    os.environ.get('appPackage') or os.environ.get('bundleID') or os.environ.get(
                'TESTDROID_BUNDLE_ID')).lower() else "Ghostery-"
        self.logger = logging.getLogger("[AutoBots]")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        fhandler = logging.FileHandler(self.app_brand+'scriptlog.log')
        handler.setLevel(logging.DEBUG)
        fhandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)s :: %(message)s')
        handler.setFormatter(formatter)
        fhandler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.addHandler(fhandler)
        self.driver = None
        self.geckoDriver = None
        self.geckoDriverTime = datetime.datetime.now().replace(microsecond=0)
        self.instance = self
        self.fullReport = ReportGenerator().generator()
        self.BitBar = True if os.environ.get('TEST_LOCATION') == "BitBar" else False

    def getDriver(self):
        if self.driver == None:
            # set up webdriver
            print "\n\nWebDriver request initiated. Waiting for response, this typically takes 2-3 mins"
            self.start_time = datetime.datetime.now().replace(microsecond=0)
            print "Start Time:" + time.strftime("%H:%M:%S")
            if self.BitBar:
                self.driver = WD.Remote(command_executor=self.appiumServer,
                                              desired_capabilities=self.desired_capabilities_cloud)
            else:
                self.desired_caps = self.desired_caps_android if self.platform_name == "android" else self.desired_caps_ios
                self.driver = WD.Remote(self.appiumServer, self.desired_caps)
            end_time = datetime.datetime.now().replace(microsecond=0)
            print "WebDriver response received at: " + time.strftime("%H:%M:%S")
            print "Time Taken to Launch Appium: " + str(end_time - self.start_time) + "\n\n"
        return self.driver

    def getInstance(self):
        return self.instance

    def prettyPrintReport(self):
        for testSuite in sorted(self.fullReport):
            if self.fullReport[testSuite] == {}:
                break
            print "\n\n*** "+testSuite+" ***"
            for testMethod in sorted(self.fullReport[testSuite]):
                print "\n* "+testMethod+" *"
                for testCase in self.fullReport[testSuite][testMethod]:
                    print "-%s- %s" % (self.fullReport[testSuite][testMethod][testCase], testCase)

    def writeReport(self, filePointer, endString):
        filePointer.write("*****     TEST REPORT FILE     *****")
        filePointer.write("\n\n*** Device Details ***\n")
        filePointer.write("Device Name: "+ self.device_name.strip() +" \n")
        filePointer.write("Device OS: " + self.platform_name.strip() + " (" + self.device_os_ver.strip() + ") \n")
        filePointer.write("Device Type: " + self.device_type.strip() + " \n")
        for testSuite in sorted(self.fullReport):
            if self.fullReport[testSuite] == {}:
                break
            filePointer.write("\n\n*** "+testSuite+" ***\n")
            for testMethod in sorted(self.fullReport[testSuite]):
                filePointer.write("\n* "+testMethod+" *\n")
                for testCase in self.fullReport[testSuite][testMethod]:
                    filePointer.write("-"+self.fullReport[testSuite][testMethod][testCase]+"- "+testCase+"\n")
        filePointer.write(endString)

    def getGeckoDriver(self):
        if self.geckoDriver == None or (datetime.datetime.now().replace(microsecond=0) - self.geckoDriverTime).seconds >= 30:
            self.geckoDriver = GeckoDriver(self)
            self.geckoDriverTime = datetime.datetime.now().replace(microsecond=0)
        return self.geckoDriver