from time import sleep
from utils.scriptUtils import ScriptUtils
from utils.deviceUtils import DeviceUtils
from utils.appUtils import AppUtils
from utils.assertUtils import AssertUtils
from utils.testUtils import TestUtils

class AllUtils(TestUtils, ScriptUtils, DeviceUtils, AssertUtils, AppUtils):

    def sleep(self, seconds):
        return sleep(seconds)