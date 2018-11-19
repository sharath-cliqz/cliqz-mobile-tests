import unittest
from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageSettings import Settings
from pages.pageTabsOverview import TabsOverview

class TestSettingsMenu:

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                         "test02_001_DefaultSettings_General Test Case will run only when it is Debug Mode.")
    def test02_001_DefaultSettings_Search(self):
        '''
        :Test Cases:
        - Check if you can open the Settings Menu.
        - Check Default Setting for Search Results For.
        - Check Default Setting for Block Explicit Content.
        - Check Default Setting for Human Web.
        - Check Default Setting for Enable Autocompletion.
        - Check Default Setting for Quick Search.
        - Check Default Setting for Complementary Search.
        :return:
        '''
        self.log("Check 'Default Settings'.", "testsuite")
        PFT = FreshTab(self.settings)
        PSM = Settings(self.settings)
        PFT.disableAddressBar()
        if self.isPlatform('ios'):
            PFT.enableAddressBar()
        PFT.goToSettings()
        self.assertIsEqual(PSM.isSettingsMenu(), True, "Check if you can open the Settings Menu.")
        if self.isPlatform('android'): PSM.openOrClickSetting("general")
        self.sleep(1)
        self.assertIsIn(PSM.getStatusValueForSetting('searchResultsFor')['summary'],
                        PSM.getDefaultForSetting('searchResultsFor'),
                        "Check Default Setting for Search Results For.")
        self.assertIsEqual(PSM.getStatusValueForSetting('blockExplicitContent')['switch'],
                         PSM.getDefaultForSetting('blockExplicitContent'),
                         "Check Default Setting for Block Explicit Content.")
        if self.isPlatform('ios'):
            self.assertIsEqual(PSM.getStatusValueForSetting('humanWeb')['summary'],
                             PSM.getDefaultForSetting('humanWeb'), "Check Default Setting for Human Web.")
        else:
            self.assertIsEqual(PSM.getStatusValueForSetting('enableAutocompletion')['switch'],
                             PSM.getDefaultForSetting('enableAutocompletion'),
                             "Check Default Setting for Enable Autocompletion.")
        self.assertIsEqual(PSM.getStatusValueForSetting('quickSearch')['switch'], PSM.getDefaultForSetting('quickSearch'),
                         "Check Default Setting for Quick Search.")
        self.assertIsEqual(PSM.getStatusValueForSetting('complementarySearch')['summary'],
                         PSM.getDefaultForSetting('complementarySearch'),
                         "Check Default Setting for Complementary Search.",
                         skipIf="android", skipMessage="No Default Complementary Search for Android.")
        PSM.goOutOfSettings()

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                         "test02_002_DefaultSettings_StartTab Test Case will run only when it is Debug Mode.")
    def test02_002_DefaultSettings_StartTab(self):
        '''
        :Test Cases:
        - Check Default Setting for Background Image.
        - Check Default Setting for Most Visited Websites.
        - Check Default Setting for News.
        :return:
        '''
        self.log("Check 'Default Settings'.", "testsuite")
        PFT = FreshTab(self.settings)
        PSM = Settings(self.settings)
        PTO = TabsOverview(self.settings)
        PFT.disableAddressBar()
        PFT.goToSettings()
        if self.isPlatform('android'): PSM.openOrClickSetting("general")
        self.sleep(1)
        if self.isPlatform('android'):
            self.assertIsEqual(PSM.getStatusValueForSetting('backgroundImage')['switch'],
                               PSM.getDefaultForSetting('backgroundImage'), "Check Default Setting for Background Image.")
        self.assertIsEqual(PSM.getStatusValueForSetting('mostVisitedWebsites')['switch'],
                           PSM.getDefaultForSetting('mostVisitedWebsites'),
                           "Check Default Setting for Most Visited Websites.")
        self.assertIsEqual(PSM.getStatusValueForSetting('news')['switch'],
                           PSM.getDefaultForSetting('news'),
                           "Check Default Setting for News.")
        PSM.goOutOfSettings()
        if self.isPlatform("android"):
            PFT.openTabsOverview()
            PTO.closeAllTabs()