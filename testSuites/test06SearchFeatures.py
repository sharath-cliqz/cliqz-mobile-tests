import unittest
from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from pages.pageSettings import Settings

class TestSearchFeatures:

    @unittest.skipIf(TestUtils().isRequiredPlatform("ios"),
                     "test06_001_SearchResultsFor Test Case will not run for IOS until the feature is fixed.")
    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test06_001_SearchResultsFor Test Case will not run as it is NOT Debug Mode.")
    def test06_001_SearchResultsFor(self):
        '''
        :Test Cases:
        - Check Backend for Germany.
        - Check Backend for France.
        - Check Backend for United States.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        PSM = Settings(self.settings)
        self.log("Check 'Search Results For' Feature.", "testsuite")
        testData = PSM.getSearchResultsForTestData()
        for country in testData:
            testPassStatus = None
            PFT.disableAddressBar()
            PFT.goToSettings()
            if self.isPlatform('android'): PSM.openOrClickSetting("general")
            PSM.openOrClickSetting("searchResultsFor")
            PSM.setSearchResultsFor(country)
            PSM.goOutOfSettings()
            for key, value in testData[country].iteritems():
                result = PFT.getAutoCompletedValue(key, timeout=2)
                self.log("(" + value + ") in (" + result + ")")
                testPassStatus = True if value in result else False
                PFT.clearAndCancelAddressBar()
            self.assertIsEqual(testPassStatus, True, "Check Backend for "+country+".")
            PFT.openTabsOverview()
            PTO.closeAllTabs()

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test06_002_ComplementarySearch Test Case will not run as it is NOT Debug Mode.")
    def test06_002_ComplementarySearch(self):
        '''
        :Test Cases:
        - Check `google` provider.
        - Check `bing` provider.
        - Check `duckduckgo` provider.
        - Check `amazon` provider.
        - Check `twitter` provider.
        - Check `wikipedia` provider.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        PSM = Settings(self.settings)
        self.log("Check 'Complementary Search' Feature.", "testsuite")
        testData = PSM.getComplementarySearchEngines()
        for engine in testData:
            self.log("Testing Engine: "+engine)
            PFT.disableAddressBar()
            PFT.goToSettings()
            if self.isPlatform('android'): PSM.openOrClickSetting("general")
            PSM.openOrClickSetting("complementarySearch")
            PSM.setComplementarySearchEngine(engine)
            PSM.goOutOfSettings()
            link = PFT.openWebpage(self.generateRandomString())
            self.assertIsIn(engine, link, "Check `"+engine+"` provider.")
            PFT.openTabsOverview()
            PTO.closeAllTabs()
