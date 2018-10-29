from utils import AllUtils
from common.exceptionList import OnboardingFailure

class Onboarding(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def startBrowsing(self):
        try:
            self.getElement("startBrowsingButton", timeout=3).click()
        except:
            self.log("The Button did not appear !!")

    def getOnboardingIntro(self):
        try:
            return self.getElement("onboarding", "intro", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Intro Screen")

    def getOnboardingIntroCheckBox(self):
        try:
            return self.getElement("onboarding", "introCheckbox", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Intro Human Web Checkbox")

    def getOnboardingAntiTrackerADBlocker(self):
        try:
            return self.getElement("onboarding", "antiTrackingAdblock", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Anti-Tracking AD-Blocker")

    def getOnboardingQuickSearch(self):
        try:
            return self.getElement("onboarding", "quickSearch", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Anti-Tracking AD-Blocker")

    def getOnboardingFreshTab(self):
        try:
            return self.getElement("onboarding", "freshTab", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Fresh Tab")

    def getOnboardingTrackerOptionListElem(self):
        try:
            return self.getElement("onboarding", "trackerOptionList", timeout=3)
        except Exception as e:
            self.log(e)
            raise OnboardingFailure("Error in Onboarding Fresh Tab")

    def getAllTrackerButtonsData(self, listElem):
        buttonData = []
        buttonList = self.getElements("onboarding", "trackerButton", baseElement=listElem, timeout=3)
        for button in buttonList:
            data = self.getTrackerButtonData(button)
            buttonData.append({
                'elem': button,
                'name': data['name'],
                'status': data['status']
            })
        return buttonData

    def getTrackerButtonData(self, buttonElem):
        if self.isPlatform("ios"):
            return {'name': buttonElem.get_attribute('name'), 'status': buttonElem.get_attribute('value')}
        else:
            return {'name': buttonElem.text, 'status': buttonElem.get_attribute('checked')}