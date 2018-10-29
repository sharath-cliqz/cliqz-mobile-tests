from common.exceptionList import *
from utils import AllUtils
class AlertBox(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def acceptDegbugger(self, deny=False):
        if self.isPlatform("ios"):
            raise DeviceTypeFailure("Gecko Driver connection works only for Android.")
        try:
            if deny==False:
                self.getElement("geckoConnAlert", "allow").click()
            else:
                self.getElement("geckoConnAlert", "deny").click()
        except Exception as e:
            self.log(e)
            raise AlertBoxFailure("Connection Request Box did not appear !")