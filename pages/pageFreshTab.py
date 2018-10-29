from utils import AllUtils
from pages.shared.topBar import TopBar
from common.exceptionList import FreshTabFailure
from common import testDataAndRequirements as TDR

class FreshTab(TopBar, AllUtils):

    def __init__(self, settings):
        self.settings = settings

    ###############################
    # News Section
    ###############################
    def getNewsSection(self):
        try:
            return self.getElement("newsSection")
        except:
            raise FreshTabFailure("News Section did not Load within 10 seconds.")

    def getDefaultNewsCount(self):
        return TDR.defaultNewsCount[self.settings.platform_name]

    def getNewsCount(self):
        count = len(self.getElements("newsArticle"))
        self.log("News Count: "+str(count))
        return count

    def expandCollapseNews(self):
        try:
            self.clickElemCenter(self.getElement('moreNews', timeout=2))
        except:
            try:
                self.clickElemCenter(self.getElement('lessNews', timeout=2))
            except:
                raise FreshTabFailure("News Section cannot be Expanded or Collapsed.")
        self.sleep(1)

    def isNewsExpandedOrCollapsed(self, newsCount=None):
        if newsCount == None:
            if self.isPlatform("android"):
                newsCount = self.getNewsCount()
                return "expanded" if newsCount > self.getDefaultNewsCount() else "collapsed"
            elif self.isPlatform("ios"):
                try:
                    self.getElement('moreNews', timeout=2)
                    return "collapsed"
                except:
                    try:
                        self.getElement('lessNews', timeout=3)
                        return "expanded"
                    except:
                        raise FreshTabFailure("News Section either cannot be found or cannot be Expanded or Collapsed.")
        else:
            return "expanded" if newsCount > self.getDefaultNewsCount() else "collapsed"

    def clickOnNews(self):
        newsDomain = self.getElement('newsURL').text
        self.getElement('newsArticle').click()
        return newsDomain

    ###############################
    # Fresh Tab Panel
    ###############################
    def getTopSitesButton(self):
        return self.getElement("freshTabPanel", "topSites", timeout=3)

    def getFavoritesButton(self):
        return self.getElement("freshTabPanel", "favorites", timeout=3)

    def getHistoryButton(self):
        return self.getElement("freshTabPanel", "history", timeout=3)

    def getOfferzButton(self):
        return self.getElement("freshTabPanel", "offerz", timeout=3)

    ###############################
    # Fresh Tab :: Top Site View
    ###############################
    def getTopSitesSection(self):
        try:
            return self.getElement("topSites", "complete", timeout=2)
        except:
            try:
                self.enableAddressBar()
                self.disableAddressBar()
                return self.getElement("topSites", "complete", timeout=2)
            except:
                return None

    def getAllTopSites(self, topSitesSection=None):
        if topSitesSection == None:
            topSitesSection = self.getTopSitesSection()
        try:
            assert topSitesSection != None
            return self.getElements("topSites", "site", topSitesSection, timeout=3)
        except Exception as e:
            self.log(e)
            FreshTabFailure("Error in getting Top Sites.")

    def getTopSiteText(self, siteElem):
        try:
            elem = self.getElement("topSites", "text", siteElem, timeout=1)
            return elem.text
        except Exception as e:
            self.log(e)
            FreshTabFailure("Error getting Text of the TopSite Element.")

    def getTopSiteDeleteElem(self, topSiteElem):
        try:
            if self.isPlatform("ios"):
                return self.getElement("topSites", "delete", topSiteElem, timeout=1)
            else:
                return self.getButtonInMenu("delete", isPopup=True)
        except Exception as e:
            self.log(e)
            raise FreshTabFailure("Top Site Delete button cannot be found.")

    def isTopSitesEmpty(self):
        if self.isPlatform("android"):
            return True if self.getTopSitesSection() == None else False
        else:
            isEmpty = True
            for site in self.getAllTopSites():
                if self.getTopSiteText(site) != (None or ''):
                    isEmpty = False
                    break
            return isEmpty

    def getTopSitesData(self):
        dataList = []
        try:
            for site in self.getAllTopSites():
                siteText = self.getTopSiteText(site)
                if siteText != (None or ''):
                        dataList.append(siteText)
        except:
            self.log("Error in getting Top Sites Data(for all all top sites).")
        return dataList

    def deleteTopSite(self, topSiteElem):
        self.longPress(topSiteElem)
        self.getTopSiteDeleteElem(topSiteElem).click()
        self.sleep(1)
        self.getHistoryButton().click()
        self.getTopSitesButton().click()


    ###############################
    # Fresh Tab :: History View
    ###############################
    def getClearHistoryButton(self):
        return self.getElement("threeDotsMenu", "clearHistory", timeout=3)

    def getClearHistoryButtonPanel(self):
        return self.getElement("clearHistory", "buttonPanel", timeout=5)

    def getClearHistoryAcceptButton(self, baseElem=None):
        return self.getElement("clearHistory", "accept", baseElement=baseElem, timeout=3)

    def getClearHistoryCancelButton(self, baseElem=None):
        return self.getElement("clearHistory", "cancel", baseElement=baseElem, timeout=3)

    def isHistoryEmpty(self):
        if self.isPlatform("android"):
            return True if self.getElements("historyEmpty", timeout=1) != [] else False
        else:
            return True if self.getHistoryList() == None else False

    def getHistoryList(self):
        parsedList = []
        if self.isPlatform("android") and self.isHistoryEmpty():
            self.log("History is Empty.")
            return []
        else:
            histComplete = self.getElement("historyComplete", timeout=2)
            historyList = self.getElements("historyItem", baseElement=histComplete, timeout=1)
            if historyList == []:
                self.log("History is Empty.")
                return []
            else:
                for elem in historyList:
                    historyItem = {}
                    for textElem in self.getElements("historyText", baseElement=elem, timeout=1):
                        text = textElem.text
                        if 'news' not in historyItem:
                            historyItem['news'] = text
                        else:
                            historyItem['url'] = text
                        self.log(text)
                    parsedList.append(historyItem)
                return parsedList

    def quickClearHistory(self):
        try:
            self.get3DotButton().click()
            self.getClearHistoryButton().click()
            self.getClearHistoryAcceptButton().click()
        except Exception as e:
            self.log(e)
            raise FreshTabFailure("Error Clearing History from Fresh Tab :: History Panel")

    ###############################
    # Home Screen Onboarding Popup
    ###############################
    def getContinueToWebsiteButton(self):
        try:
            return self.getElement("homeScreenOnboarding")
        except:
            try:
                self.getStopLoadingButton().click()
                return self.getElement("homeScreenOnboarding", timeout=3)
            except Exception as e:
                self.log(e)
                try:
                    self.get3DotButton().click()
                    self.getStopLoadingButton().click()
                    return self.getElement("homeScreenOnboarding", timeout=3)
                except Exception as e:
                    self.log(e)
                    raise FreshTabFailure("Home Screen Onboarding Popup did not Load within 10 seconds.")

    def openHomeScreenOnboardingPopup(self):
        try:
            self.openWebpage(TDR.homeScreenButtonOnboardingLink)
            self.sleep(3)
            return self.getContinueToWebsiteButton()
        except Exception as e:
            self.log(e)
            return None