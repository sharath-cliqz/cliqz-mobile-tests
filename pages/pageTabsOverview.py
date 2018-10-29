from utils import AllUtils
from common.exceptionList import TabsOverviewFailure
from time import sleep

class TabsOverview(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def getTabsPanel(self):
        try:
            return self.getElement("tabsPanel", "complete", timeout=1, absNoScr=True)
        except:
            return None

    def getHeaderBar(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getTabsButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header_tabsButton", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getNavNormalTabsButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header_normalTabs", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getNavPrivateTabsButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header_privateTabs", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getNavAddTabButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header_addTab", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getNavTabsMenuButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "header_tabsMenu", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getTabsList(self, baseElem=None):
        try:
            return self.getElements("tabsPanel", "tabs_complete", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getSettingsButton(self, baseElem=None):
        try:
            return self.getElement("debugElem", "settingsButton", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getPrivateTabsEmpty(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "privateTabsEmpty", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getPrivateTabsText(self, baseElem=None):
        try:
            return self.getElement("tabsPanel", "privateTabsText", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getDoneButton(self, baseElem=None):
        try:
            return self.getElement("tabsPanel",
                               "header_closeAllTabsOrDoneButton", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def isTabsOverview(self):
        return self.getTabsPanel() != None

    def isPrivateTabsEmpty(self, baseElem=None):
        try:
            privateButton = self.getNavPrivateTabsButton(baseElem)
            if self.isPlatform("android"):
                if privateButton.get_attribute('selected') != 'true':
                    privateButton.click()
                    self.log("Clicked on the Private Button.")
            elif self.isPlatform("ios"):
                if privateButton.get_attribute('value') == "Off":
                    privateButton.click()
                    self.log("Clicked on the Private Button.")
        except Exception as e:
            self.log(e)
            raise TabsOverviewFailure("Error Finding Private Tabs Button.")
        try:
            self.getPrivateTabsEmpty()
            return True
        except Exception as e:
            try:
                self.log(e)
                self.getPrivateTabsText()
                return True
            except Exception as e:
                self.log(e)
                return False

    def getTabData(self, tabElem):
        tabData = {}

    def closeAllTabs(self):
        privateButton = self.getNavPrivateTabsButton(baseElem=None)
        try:
            if self.settings.platform_name == 'android':
                self.getElement('tabsPanel', 'header_normalTabs').click()
                self.getElement('tabsPanel', 'header_tabsMenu').click()
                self.getElement('tabsPanel', 'header_closeAllTabsOrDoneButton').click()
            elif self.settings.platform_name == 'ios':
                if privateButton.get_attribute('value') == 'On':
                    self.longPress(self.getElement("tabsPanel", 'header_closeAllTabsOrDoneButton'))
                    try:
                        self.getElement("tabsPanel", 'header_closeAllTabsConfirmation').click()
                    except:
                        self.longPress(self.getElement("tabsPanel", 'header_closeAllTabsOrDoneButton'))
                        self.getElement("tabsPanel", 'header_closeAllTabsConfirmation').click()
                    sleep(1)
                    privateButton.click()
                self.longPress(self.getElement("tabsPanel", 'header_closeAllTabsOrDoneButton'))
                try:
                    self.getElement("tabsPanel", 'header_closeAllTabsConfirmation').click()
                except:
                    self.longPress(self.getElement("tabsPanel", 'header_closeAllTabsOrDoneButton'))
                    self.getElement("tabsPanel", 'header_closeAllTabsConfirmation').click()
                self.sleep(1)
        except Exception as e:
            self.log(e)
            raise TabsOverviewFailure("Error Closing All Tabs.")

    def goToSettings(self):
        if self.isPlatform("android"): raise TabsOverviewFailure("Cannot go to Settings from TabsOverview for Android.")
        try:
            #self.clickElemCenter(self.getSettingsButton(), pressTime=500)
            self.getSettingsButton().click()
        except Exception as e:
            self.log(e)
            raise TabsOverviewFailure("Settings Button is not Present.")

    def goBackFromTabsOverview(self):
        try:
            if self.isPlatform("android"):
                self.getTabsButton().click()
            else:
                self.getDoneButton().click()
        except Exception as e:
            self.log(e)
            raise TabsOverviewFailure("Error Going back from Tabs Overview")