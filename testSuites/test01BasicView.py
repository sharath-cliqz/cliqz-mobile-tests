from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from pages.pageOnboarding import Onboarding
import unittest
from common import testDataAndRequirements as TDR

class TestBasicView:

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test01_001_Onboarding Test Case will not run as it is Debug Mode.")
    def test01_001_Onboarding(self):
        '''
        :Test Cases:
        - Check if the Onboarding Intro Text is correct.
        - Check if there is a Checkbox/Switch for Human Web on Onboarding Intro page.
        - Check if there is a Checkbox/Switch is Default Checked/Enabled.
        - Check if the Checkbox/Switch Changes status on Click.
        - Check if the 2nd Onboarding is Anti-Tracking.
        - Check if there are 3 Buttons for Default Tracking.
        - Check if Recommended is selected by default.
        - Check if clicking on an option selects it.
        - Check if the 3rd Onboarding is Quick Search.
        - Check if the 4th Onboarding is Ghostery/Cliqz Tab.
        :return:
        '''
        POB = Onboarding(self.settings)
        self.assertIsIn(POB.getOnboardingIntro().text, TDR.onBoardingPage1,
                           "Check if the Onboarding Intro Text is correct.")
        switch = POB.getOnboardingIntroCheckBox()
        self.assertNotEqual(switch, None,
                            "Check if there is a Checkbox/Switch for Human Web on Onboarding Intro page.")
        attrib = "value" if self.isPlatform("ios") else "checked"
        self.assertIsEqual(self.convertToBool(switch.get_attribute(attrib)), False if self.isPlatform('android') else True,
                               "Check if there is a Checkbox/Switch is Default Checked/Enabled.")
        switch.click()
        self.sleep(1)
        self.assertIsEqual(self.convertToBool(switch.get_attribute(attrib)),
                           True if self.isPlatform('android') else None,
                           "Check if the Checkbox/Switch Changes status on Click.")
        switch.click()
        self.mobileScroll(direction="left")
        self.assertIsEqual(POB.getOnboardingAntiTrackerADBlocker().text, TDR.onBoardingPage2,
                           "Check if the 2nd Onboarding is Anti-Tracking.")
        buttonData = POB.getAllTrackerButtonsData(POB.getOnboardingTrackerOptionListElem())
        self.assertIsEqual(len(buttonData), 3, "Check if there are 3 Buttons for Default Tracking.")
        defaultSelected = {}
        for button in buttonData:
            if self.convertToBool(button['status']) == True:
                defaultSelected = button
                break
        self.assertIsIn("Recommended", defaultSelected['name'], "Check if Recommended is selected by default.")
        selection = True
        for button in buttonData:
            button['elem'].click()
            self.sleep(1)
            if self.convertToBool(POB.getTrackerButtonData(button['elem'])['status']) != True:
                selection = False
                break
        self.assertIsEqual(selection, True, "Check if clicking on an option selects it.")
        defaultSelected['elem'].click()
        self.mobileScroll(direction="left")
        self.assertIsEqual(POB.getOnboardingQuickSearch().text, TDR.onBoardingPage3,
                           "Check if the 3rd Onboarding is Quick Search.")
        self.mobileScroll(direction="left")
        self.assertIsIn(POB.getOnboardingFreshTab().text, TDR.onBoardingPage4,
                           "Check if the 4th Onboarding is Ghostery/Cliqz Tab.")
        POB.startBrowsing()

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test01_002_FirstLaunch Test Case will not run as it is Debug Mode.")
    def test01_002_FirstLaunch(self):
        '''
        :Test Cases:
        - Check if App Starts with Address Bar.
        - Check if URL Bar exists.
        - Check if Address Bar does not exist.
        - Check that Keyboard is already Minimized.
        - Check if Address Bar exists.
        :return:
        '''
        self.log("Check 'First Launch'.", "testsuite")
        PFT = FreshTab(self.settings)
        Onboarding(self.settings).startBrowsing()
        self.assertNotEqual(PFT.getAddressBar(), None, "Check if App Starts with Address Bar.")
        PFT.disableAddressBar()
        self.assertIsEqual(PFT.getAddressBar(), None, "Check if Address Bar does not exist.")
        urlBar = PFT.getURLBar()
        self.assertNotEqual(urlBar, None, "Check if URL Bar exists.")
        self.assertIsEqual(self.minimizeKeyboard(), False, "Check that Keyboard is already Minimized.",
                           noException=True)
        urlBar.click()
        self.assertNotEqual(PFT.getAddressBar(), None, "Check if Address Bar exists.")

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test01_002_CheckAddressBar Test Case will not run as it is Debug Mode.")
    def test01_003_CheckAddressBar(self):
        '''
        :Test Cases:
        - Check if Address Bar exists.
        - Check Address Bar Pretext.
        - Check Address Bar updates correctly.
        - Check Address Bar updates correctly again.
        - Check URL Bar exists and has Pretext.
        - Check if Reader Mode is on FreshTab.
        :return:
        '''
        self.log("Check 'Address Bar Functionality'.", "testsuite")
        PFT = FreshTab(self.settings)
        addressBar = PFT.enableAddressBar()
        self.assertNotEqual(addressBar, None, "Check if Address Bar exists.")
        self.assertIsEqual(addressBar.text, "Search or enter address", "Check Address Bar Pretext.")
        addressBar.set_value("www.google.de")
        self.assertIsEqual(addressBar.text, "www.google.de", "Check Address Bar updates correctly.")
        addressBar.clear()
        addressBar.set_value("www.google.de")
        self.assertIsEqual(addressBar.text, "www.google.de", "Check Address Bar updates correctly again.")
        PFT.clearAndCancelAddressBar()
        self.assertIsEqual(PFT.getURLBar().text, "Search or enter address", "Check URL Bar exists and has Pretext.")
        self.assertIsEqual(PFT.getReaderModeButton(), None,
                           "Check if Reader Mode is on FreshTab.")

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test01_003_TabsOverview Test Case will not run as it is Debug Mode.")
    def test01_004_TabsOverview(self):
        '''
        :Test Cases:
        - Check if only 1 Tab exists in the list.
        - Check Address Bar is not present.
        - Check Tabs Panel Element is present.
        - Check Tabs Panel has a Header Bar.
        - Check Tabs Panel Header Bar has a Tabs Button.
        - Check Tabs Panel Header Bar has a Private Button.
        - Check Tabs Panel Header Bar has a Add Tab Button.
        - Check Tabs Panel Header Bar has a Menu Button.
        - Check if the tabs count is as per the number of tabs.
        - Check if Private Tabs List is Empty.
        - Check if FreshTab is opened after removing all tabs.
        :return:
        '''
        self.log("Check 'Tabs Overview'.", "testsuite")
        PFT = FreshTab(self.settings)
        tabsCount = PFT.getTabsCount()
        self.assertIsEqual(tabsCount, 1, "Check if only 1 Tab exists in the list.",
                           skipIf="ios", skipMessage="Tabs Counter is not present for iOS.")
        PFT.openTabsOverview()
        PTO = TabsOverview(self.settings)
        self.assertIsEqual(PFT.getAddressBar(), None, "Check Address Bar is not present.")
        tabsPanel = PTO.getTabsPanel()
        self.assertNotEqual(tabsPanel, None, "Check Tabs Panel Element is present.")
        tabsPanelHeaderBar = PTO.getHeaderBar(tabsPanel)
        self.assertNotEqual(tabsPanelHeaderBar, None, "Check Tabs Panel has a Header Bar.")
        self.assertNotEqual(PTO.getTabsButton(tabsPanelHeaderBar), None,
                            "Check Tabs Panel Header Bar has a Tabs Button.",
                            skipIf="ios", skipMessage="No Back Button for iOS.")
        self.assertNotEqual(PTO.getNavNormalTabsButton(), None,
                            "Check Tabs Panel Header Bar has a Tabs Button.",
                            skipIf="ios", skipMessage="No Tabs Button for iOS.")
        self.assertNotEqual(PTO.getNavPrivateTabsButton(), None,
                            "Check Tabs Panel Header Bar has a Private Button.")
        self.assertNotEqual(PTO.getNavAddTabButton(tabsPanelHeaderBar), None,
                            "Check Tabs Panel Header Bar has a Add Tab Button.")
        self.assertNotEqual(PTO.getNavTabsMenuButton(tabsPanelHeaderBar), None,
                            "Check Tabs Panel Header Bar has a Menu Button.",
                            skipIf="ios", skipMessage="No Menu Button for iOS.")
        self.assertIsEqual(len(PTO.getTabsList(tabsPanel)), tabsCount,
                           "Check if the tabs count is as per the number of tabs.",
                           skipIf="ios", skipMessage="Tabs Counter is not present for iOS.")
        self.assertIsEqual(PTO.isPrivateTabsEmpty(tabsPanel), True,
                           "Check if Private Tabs List is Empty.", noException=True)
        PTO.closeAllTabs()
        self.assertIsEqual(PFT.disableAddressBar().text, "Search or enter address",
                           "Check if FreshTab is opened after removing all tabs.")

    @unittest.skipIf(TestUtils().isRequiredPlatform("ios"),
                     "test01_005_HomeScreenOnboarding Test Case will not run for IOS.")
    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test01_005_HomeScreenOnboarding Test Case will not run as it is Debug Mode.")
    def test01_005_HomeScreenOnboarding(self):
        '''
        :Test Cases:
        - Check if Add to Home Screen Onboarding Appears.
        - Check if Add to Home Screen Button appears.
        - Check if the Add to Home Screen Link is correct.
        - Check if Action Button is present.
        - Check if Cancel Button is present.
        - Check if Clicking Cancel removes the Add to Home Screen Panel.
        :return:
        '''
        self.log("Check 'Web Page Load'.", "testsuite")
        PFT = FreshTab(self.settings)
        continueToWebsiteButton = PFT.openHomeScreenOnboardingPopup()
        self.assertNotEqual(continueToWebsiteButton, None, "Check if Add to Home Screen Onboarding Appears.")
        self.sleep(1)
        continueToWebsiteButton.click()
        addToHomeScreenButton = PFT.getAddToHomeScreenButton()
        self.assertNotEqual(addToHomeScreenButton, None, "Check if Add to Home Screen Button appears.")
        addToHomeScreenButton.click()
        addToHomeScreenLink = PFT.getAddToHomeScreenLink()
        addToHomeScreenActionButton = PFT.getAddToHomeScreenActionButton()
        addToHomeScreenCancelButton = PFT.getAddToHomeScreenCancelButton()
        self.assertIsIn(TDR.homeScreenButtonOnboardingLink, addToHomeScreenLink.text,
                           "Check if the Add to Home Screen Link is correct.")
        self.assertNotEqual(addToHomeScreenActionButton, None, "Check if Action Button is present.")
        self.assertNotEqual(addToHomeScreenCancelButton, None, "Check if Cancel Button is present.")
        addToHomeScreenCancelButton.click()
        self.sleep(1)
        self.assertIsEqual(PFT.getAddToHomeScreenRootPanel(), None,
                           "Check if Clicking Cancel removes the Add to Home Screen Panel.")
        PFT.openTabsOverview()
        TabsOverview(self.settings).closeAllTabs()
