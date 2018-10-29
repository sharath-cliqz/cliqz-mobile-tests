from utils import AllUtils
from common.exceptionList import SettingsFailure
from common.testDataAndRequirements import *

class Settings(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def isSettingsMenu(self):
        if self.getElements("settingsMenu", "settingsPrefsFrame", timeout=3) != []:
            return True
        else:
            return False

    def isSettingsContentMenu(self):
        if self.getElements("settingsContentMenu", timeout=3) != []:
            return True
        else:
            return False

    def whichSettingsSubMenu(self):
        if self.isSettingsMenu() and self.isPlatform('android'):
            subMenu = self.getElement("settingsMenu", "settingsSubMenu", timeout=3).text
            self.log("Inside: *"+subMenu+"* Submenu.")
            return subMenu.lower()
        else:
            self.log("Not a Settings Menu.")

    def getDefaultForSetting(self, setting):
        return defaultSettings[setting]

    def getSearchResultsForTestData(self):
        return searchResultsFor

    def getComplementarySearchEngines(self):
        return comSearch

    def getSettingsMenu(self):
        return self.getElement("settingsMenu", "complete", timeout=3)

    def getSettingButton(self, setting):
        try:
            return self.getElement("settingsMenu", setting, baseElement=self.getSettingsMenu(), timeout=1)
        except:
            return None

    def getSettingCheckboxSwitch(self, settingElem):
        try:
            if self.isPlatform("ios"):
                return self.getElement("settingsMenu", "switch", baseElement=settingElem, timeout=1)
            else:
                try:
                    return self.getElement("settingsMenu", "checkbox", baseElement=settingElem, timeout=1)
                except:
                    return self.getElement("settingsMenu", "switch", baseElement=settingElem, timeout=1)
        except:
            return None

    def getSettingSummary(self, settingElem):
        try:
            return self.getElement("settingsMenu", "settingSummary", baseElement=settingElem, timeout=1)
        except:
            return None

    def backToSettingsMenu(self):
        try:
            self.getElement("settingsBackToMenu", timeout=1).click()
        except Exception as e:
            self.log(e)
            self.log("Not inside a Setting Menu for a specific Setting.")

    def clickSettingsDoneButton(self):
        try:
            self.getElement("settingsDoneButton", timeout=1).click()
        except:
            self.log("Not inside Settings Menu. Or Already Out of Settings.")

    def getSettingElem(self, setting):
        try:
            count = 1
            settingButton = self.getSettingButton(setting)
            if self.isPlatform("ios"):
                condition = settingButton.is_displayed()
            else:
                condition = False if settingButton == None else True
            while not condition and count <= 5:
                self.mobileScroll(direction="up")
                settingButton = self.getSettingButton(setting)
                count += 1
                if self.isPlatform("ios"):
                    condition = settingButton.is_displayed()
                else:
                    if settingButton == None:
                        condition = False
                    elif settingButton != None and settingButton.is_enabled() == False:
                        condition = False
                    else:
                        condition = True
            return settingButton
        except Exception as e:
            self.log(e)
            raise SettingsFailure("Error in finding the required Setting("+setting+")")

    def openOrClickSetting(self, setting):
        elem = self.getSettingElem(setting)
        count = 50
        while not elem.is_enabled() and count <= 0:
            self.sleep(0.1)
            count -= 1
        elem.click()
        self.sleep(1)

    def getStatusValueForSetting(self, setting=None, settingElem=None):
        if settingElem == None and setting == None:
            raise SettingsFailure("Pass atleast Setting or Setting Elem.")
        if settingElem == None:
            settingElem = self.getSettingElem(setting)
        switch = self.getSettingCheckboxSwitch(settingElem)
        summary = self.getSettingSummary(settingElem)
        try:
            switchValue = self.convertToBool(switch.get_attribute('value' if self.isPlatform('ios') else 'checked'))
        except:
            switchValue = None
        try:
            summaryValue = summary.get_attribute('name') if self.isPlatform('ios') else summary.text
        except:
            summaryValue = None
        return {'switch': switchValue, 'summary': summaryValue}

    def clearData(self, dataType):
        try:
            switch = self.getElement("clearPrivateDataList", dataType, timeout=3)
            if self.isPlatform("ios"):
                switchValue = self.convertToBool(switch.get_attribute("value"))
            else:
                switchValue = self.convertToBool(switch.get_attribute("checked"))
            if switchValue != True:
                switch.click()
            self.getElement("clearPrivateDataList", "clearData", timeout=3).click()
            if self.isPlatform("ios"):
                self.getElement("clearPrivateDataList", "confirmationAccept", timeout=3).click()
                self.getElement("settingsBackToMenu", timeout=1).click()
        except:
            raise SettingsFailure("Error in Clearing Private Data.")

    def goOutOfSettings(self):
        if self.isPlatform('ios'):
            self.backToSettingsMenu()
            self.clickSettingsDoneButton()
        else:
            if self.isSettingsContentMenu():
                self.androidBackKey()
            while self.isSettingsMenu():
                self.clickSettingsDoneButton()

    def setSearchResultsFor(self, option):
        self.getElement("searchResultsForList", option, timeout=3).click()
        self.sleep(1)

    def setComplementarySearchEngine(self, option):
        self.getElement("complementarySearchList", option, timeout=3).click()
        self.sleep(1)
        if self.isPlatform("android"): self.getElement("complementarySearchList", "set", timeout=3).click()
        self.sleep(1)


    def changeSettingStatus(self, setting, status=None):
        settingElem = self.getSettingElem(setting)
        if self.getStatusValueForSetting(settingElem=settingElem)['switch'] != status:
            self.getSettingCheckboxSwitch(settingElem).click()
