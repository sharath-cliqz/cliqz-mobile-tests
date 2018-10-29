import unittest
from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from common import testDataAndRequirements as TDR

class TestUserTabFeatures:

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test04_001_ReaderMode Test Case will not run as it is Debug Mode.")
    def test04_001_ReaderMode(self):
        '''
        :Test Cases:
        - The Reader Mode Button is visible for the webpage
        - Get into Reader Mode
        - Get out of Reader Mode
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        self.log("Check 'Reader Mode'.", "testsuite")
        PFT.openWebpage(TDR.readerModeLink)
        self.assertIsEqual(PFT.getReaderModeStatus(), True,
                           "The Reader Mode Button is visible for the webpage")
        PFT.getReaderModeButton().click()
        self.sleep(3)
        self.assertIsEqual(PFT.getReaderModeStatus(), False,
                           "Get into Reader Mode")
        PFT.getReaderModeButton().click()
        self.sleep(3)
        self.assertIsEqual(PFT.getReaderModeStatus(), True,
                           "Get out of Reader Mode", noException=True)
        PFT.openTabsOverview()
        PTO.closeAllTabs()