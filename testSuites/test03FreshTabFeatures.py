import unittest
from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from pages.pageSettings import Settings
from common.testDataAndRequirements import askLink

class TestFreshTabFeatures:

    @unittest.skipIf(TestUtils().isTestScriptDebug(), "test03_001_News Test Case will not run as it is Debug Mode.")
    def test03_001_News(self):
        '''
        :Test Cases:
        - Check if News Section Loads.
        - Check if News section is already Expanded.
        - Check that there are only 2/3 News displayed.
        - Check if Clicking on More News increases the news count.
        - Check if clicking on a news navigates to the correct news page.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        self.log("Check 'News' Feature on Fresh Tab.", "testsuite")
        self.assertNotEqual(PFT.getNewsSection(), None,
                              "Check if News Section Loads.")
        newsCount = PFT.getNewsCount()
        self.assertIsEqual(PFT.isNewsExpandedOrCollapsed(newsCount), "expanded",
                           "Check if News section is already Expanded.", noException=True)
        self.assertGreaterThan(newsCount, PFT.getDefaultNewsCount(),
                           "Check that there are only 2/3 News displayed.", noException=True)
        PFT.expandCollapseNews()
        if self.isPlatform("android"): newsCount = PFT.getNewsCount()
        self.assertIsEqual(newsCount, PFT.getDefaultNewsCount(),
                           "Check if Clicking on More News increases the news count.", noException=True)
        newsDomain = PFT.clickOnNews()
        # Extract only the main Domain Name.
        newsDomain = newsDomain.split(".")[:-1]
        self.sleep(3)
        self.assertIsIn(newsDomain[-1], PFT.getURLBar().text,
                        "Check if clicking on a news navigates to the correct news page.")
        PFT.openTabsOverview()
        PTO.closeAllTabs()

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                         "test03_002_HistoryList Test Case will run only when it is Debug Mode.")
    def test03_002_HistoryList(self):
        '''
        :Test Cases:
        - Check if only 1 History entry is generated.
        - Check if the URL is correctly generated in History.
        - Check if the History is Empty.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        self.log("Check 'History' Feature on Fresh Tab.", "testsuite")
        PFT.getHistoryButton().click()
        self.sleep(2)
        initialList = PFT.getHistoryList()
        PFT.getTopSitesButton().click()
        webpage = PFT.openWebpage()
        self.log(webpage)
        PFT.openTabsOverview()
        PTO.closeAllTabs()
        self.sleep(2)
        PFT.getHistoryButton().click()
        newHistory = self.listDiff(initialList, PFT.getHistoryList())
        self.assertIsEqual(len(newHistory), 1, "Check if only 1 History entry is generated.")
        self.assertIsIn(webpage, newHistory[0]['url'], "Check if the URL is correctly generated in History.")
        if self.isPlatform("ios"):
            PFT.goToSettings()
            PSM = Settings(self.settings)
            PSM.openOrClickSetting("clearPrivateData")
            PSM.clearData("browsingHistory")
            PSM.goOutOfSettings()
        else:
            PFT.quickClearHistory()
            self.sleep(3)
            PFT.getFavoritesButton().click()
        PFT.getHistoryButton().click()
        self.sleep(3)
        finalList = PFT.getHistoryList()
        self.assertIsEqual(finalList, [], "Check if the History is Empty.")
        PFT.getTopSitesButton().click()

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test03_003_TopSites Test Case will run only when it is Debug Mode.")
    def test03_003_TopSites(self):
        '''
        :Test Cases:
        - Check for Top Sites Section.
        - Visit Test Webpage and Check if TopSite is added.
        - Check if the Domain of the Test Webpage is correct.
        - Visit Ask.com and Check if TopSite is added.
        - Check if the Domain of Ask.com is correct.
        - Check if a TopSite can be removed.
        - Check if only the correct TopSite is removed and the other remains.
        - Check if Clearing History removes the TopSites as well.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        PSM = Settings(self.settings)
        PFT.disableAddressBar()
        PFT.goToSettings()
        if self.isPlatform('android'): PSM.openOrClickSetting("general")
        self.sleep(1)
        if PSM.getStatusValueForSetting('mostVisitedWebsites')['switch'] != True:
            PSM.changeSettingStatus("mostVisitedWebsites", True)
            self.sleep(1)
        if self.isPlatform("ios"):
            PSM.openOrClickSetting("clearPrivateData")
            PSM.clearData("browsingHistory")
            PSM.goOutOfSettings()
        else:
            PSM.goOutOfSettings()
            PFT.getHistoryButton().click()
            PFT.quickClearHistory()
            self.sleep(3)
            PFT.getFavoritesButton().click()
            PFT.getTopSitesButton().click()
        initialData = PFT.getTopSitesData()
        for count in range(0, 4):
            PFT.openWebpage()
        PFT.openTabsOverview()
        PTO.closeAllTabs()
        self.assertNotEqual(PFT.getTopSitesSection(), None, "Check for Top Sites Section.")
        intermediateData = PFT.getTopSitesData()
        newTopSite = self.listDiff(initialData, intermediateData)
        self.assertIsEqual(len(newTopSite), 1, "Visit Test Webpage and Check if TopSite is added.")
        self.assertIsIn("test" if self.isPlatform("android") else "cliqz", newTopSite[0].lower(),
                        "Check if the Domain of the Test Webpage is correct.")
        for count in range(0, 4):
            PFT.openWebpage(askLink)
        PFT.openTabsOverview()
        PTO.closeAllTabs()
        finalData = PFT.getTopSitesData()
        newTopSite = self.listDiff(intermediateData, finalData)
        self.assertIsEqual(len(newTopSite), 1, "Visit Ask.com and Check if TopSite is added.")
        self.assertIsIn("ask", " ".join(finalData).lower(), "Check if the Domain of Ask.com is correct.")
        if self.isPlatform("ios"):
            PFT.deleteTopSite(PFT.getAllTopSites()[0])
            self.sleep(3)
            tempData = PFT.getTopSitesData()
            self.log("Final Data: "+str(finalData)+"["+str(len(finalData))+"]")
            self.log("Temp Data: " + str(tempData) + "[" + str(len(tempData)) + "]")
            self.assertIsEqual(len(finalData)-len(tempData), 1, "Check if a TopSite can be removed.")
            self.assertIsEqual(tempData[0], finalData[1],
                               "Check if only the correct TopSite is removed and the other remains.")
            PFT.goToSettings()
            PSM = Settings(self.settings)
            PSM.openOrClickSetting("clearPrivateData")
            PSM.clearData("browsingHistory")
            PSM.goOutOfSettings()
        else:
            PFT.getHistoryButton().click()
            PFT.quickClearHistory()
            PFT.quickClearHistory()
            self.sleep(3)
            PFT.getFavoritesButton().click()
            PFT.getTopSitesButton().click()
        PFT.openTabsOverview()
        PTO.closeAllTabs()
        self.assertIsEqual(PFT.isTopSitesEmpty(), True, "Check if Clearing History removes the TopSites as well.")