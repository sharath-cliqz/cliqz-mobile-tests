from utils import AllUtils
from common.exceptionList import TopBarFailure

class Action3DotsMenu(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def getAction3DotMenu(self):
        if self.isPlatform("android"):
            return self.getElement("threeDotsMenu", "complete", timeout=5)
        else:
            return self.getElement("actionMenu", "complete", timeout=5)

    def getButtonInMenu(self, button, isPopup=False):
        if self.isPlatform("ios"):
            return self.getElement("actionMenu", button, timeout=3)
        else:
            if isPopup == False:
                return self.getElement("threeDotsMenu", button,
                                   baseElement=self.getAction3DotMenu(), timeout=3)
            else:
                return self.getElement("threeDotsMenu", button, timeout=3)

    def goToSettings(self):
        try:
            self.get3DotButton().click()
            self.getButtonInMenu("settings").click()
        except:
            if self.isPlatform("ios"):
                try:
                    self.enableAddressBar()
                    self.clearAndCancelAddressBar()
                    self.get3DotButton().click()
                    self.getButtonInMenu("settings").click()
                except Exception as e:
                    self.log(e)
                    raise TopBarFailure("Error going to Settings.")
            else:
                raise TopBarFailure("Error going to Settings.")