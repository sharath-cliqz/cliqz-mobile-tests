from common.exceptionList import GhosteryCCFailure
from utils import AllUtils
from appium.webdriver.common.touch_action import TouchAction as TA

class GhosteryCC(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def getGhosteryCC(self):
        try:
            return self.getElement("ghosteryControlCenter", "complete", timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryTabsController(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "tabsController", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryOverviewButton(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "overview", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosterySiteTrackersButton(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "siteTrackers", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryAllTrackersButton(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "allTrackers", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryDonut(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "donut", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryNotch(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "notch", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getGhosteryAdBlockerSwitch(self, baseElem=None):
        try:
            return self.getElement("ghosteryControlCenter", "adBlockerSwitch", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getEnhancedOptionsViewElem(self):
        try:
            return self.getElement("ghosteryControlCenter", "enhancedOptionsView", timeout=2, absNoScr=True)
        except:
            return None

    def expandEnhancedOptions(self, notchElem=None):
        if notchElem == None: notchElem = self.getGhosteryNotch()
        start = self.centerLocation(notchElem)
        end = {'x': start['x'], 'y': 50}
        notchElem.click()
        TA(self.settings.driver).long_press(x=start['x'], y=start['y'], duration=1)\
            .move_to(x=end['x'], y=end['y'])\
            .release().perform()

    def collapseEnhancedOptions(self, notchElem=None):
        if notchElem == None: notchElem = self.getGhosteryNotch()
        start = self.centerLocation(notchElem)
        end = {'x': start['x'], 'y': self.getScreenSize()['height']-25}
        notchElem.click()
        TA(self.settings.driver).long_press(x=start['x'], y=start['y'], duration=1) \
            .move_to(x=end['x'], y=end['y']) \
            .release().perform()

    def getTrackerListElem(self):
        try:
            return self.getElement("ghosteryControlCenter", "trackerList", timeout=3, absNoScr=True)
        except:
            return None

    def getTrackerCategoryElem(self, baseElem=None):
        if baseElem==None:
            baseElem = self.getTrackerListElem()
        try:
            return self.getElement("ghosteryControlCenter", "trackerCategory", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return None

    def getAllTotalTrackerElems(self, baseElem=None):
        try:
            return self.getElements("ghosteryControlCenter", "totalTrackersElem", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return []

    def getAllTrackerCountElems(self):
        baseElem = self.getTrackerListElem()
        try:
            return self.getElements("ghosteryControlCenter", "trackersCountElem", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return []

    def getAllBlockedTrackerElems(self, baseElem=None):
        try:
            return self.getElements("ghosteryControlCenter", "blockedTrackersElem", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return []

    def getAllTrackerCategoriesElems(self):
        baseElem = self.getTrackerListElem()
        try:
            return self.getElements("ghosteryControlCenter", "trackerCategory", baseElement=baseElem, timeout=3, absNoScr=True)
        except:
            return []

    def getTrackerCategoryName(self, baseElem):
        try:
            return self.getElement("ghosteryControlCenter", "trackerCategoryName", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getTrackerNames(self):
        try:
            return self.getElements("ghosteryControlCenter", "trackerName", timeout=1, absNoScr=True)
        except:
            return []

    def getTrackerBlockStatuses(self):
        try:
            return self.getElements("ghosteryControlCenter", "trackerBlockStatus", timeout=1, absNoScr=True)
        except:
            return []

    def getExpandCollapseCategory(self, baseElem):
        try:
            return self.getElement("ghosteryControlCenter", "expandCollapseCategory", baseElement=baseElem, timeout=1, absNoScr=True)
        except:
            return None

    def getTrackerData(self, tab="site"):
        # Each key is the 'Category Name' with value as: {'elem': None, 'trackers': [{'tracker': "", }]}
        # A final Key with "count" has the full Tracker Found and Blocked as a Dict
        fullTrackerData = {}
        tabController = self.getGhosteryTabsController(self.getGhosteryCC())
        if tab.lower() == "site":
            self.getGhosterySiteTrackersButton(tabController).click()
        elif tab.lower() == "all":
            self.getGhosteryAllTrackersButton(tabController).click()
        tempElems = self.getAllTrackerCategoriesElems()
        for i in range(len(tempElems)-1, -1, -1):
            elem = tempElems[i]
            try:
                if self.isPlatform('android'):
                    temp = self.getTrackerCategoryName(elem)
                else:
                    temp = elem
                categoryName = temp.get_attribute("name") if self.isPlatform('ios') else temp.text
                if categoryName != None and (categoryName not in fullTrackerData):
                    if tab == "site":
                        tempLoc = self.centerLocation(temp)
                        self.tapOnLoc(tempLoc)
                        tempTrackList = {
                            'names': self.getTrackerNames(),
                            'statuses': self.getTrackerBlockStatuses()
                        }
                        trackerList = []
                        attrib = "name" if self.isPlatform('ios') else "checked"
                        if len(tempTrackList['names']) == len(tempTrackList['statuses']):
                            for i in range(0, len(tempTrackList['names'])):
                                trackerList.append({
                                    'name': tempTrackList['names'][i].get_attribute("name") if self.isPlatform('ios')
                                        else tempTrackList['names'][i].text,
                                    'status': self.convertToBool(tempTrackList['statuses'][i].get_attribute(attrib))
                                })
                        self.tapOnLoc(tempLoc)
                        self.sleep(1)
                        fullTrackerData[categoryName] = {'elem': temp, 'trackers': trackerList}
            except Exception as e:
                self.log(e)
        trackerCount = {'found': 0, 'blocked': 0}
        if self.isPlatform('ios'):
            tempElems = self.getAllTrackerCountElems()
            for elem in tempElems:
                trackerCount['found'] += int(elem.text.split(' ')[0])
                trackerCount['blocked'] += int(elem.text.split(' ')[2])
        else:
            tempElems = self.getAllTotalTrackerElems()
            for elem in tempElems:
                trackerCount['found'] += int(elem.text.split(' ')[0])
            tempElems = self.getAllBlockedTrackerElems()
            for elem in tempElems:
                trackerCount['blocked'] += int(elem.text.split(' ')[0])
        fullTrackerData['count'] = trackerCount
        return fullTrackerData

    def getTrackerCount(self, blocked=True):
        '''
        Request for Found and Blocked Tracker Counts.
        :return:
        Returns a Dict with 'found' and 'blocked' Counts.
        '''
        trackers = {'found': 0, 'blocked': 0}
        if self.isPlatform('ios'):
            tabController = self.getGhosteryTabsController(self.getGhosteryCC())
            self.getGhosteryOverviewButton(tabController).click()
            trackers['found'] = int(self.getGhosteryDonut().text)
            if blocked == True:
                self.getGhosterySiteTrackersButton(tabController).click()
                tempElems = self.getAllTrackerCountElems()
                for elem in tempElems:
                    trackers['blocked'] += int(elem.text.split(' ')[2])
        else:
            self.getGhosterySiteTrackersButton().click()
            tempElems = self.getAllTotalTrackerElems()
            for elem in tempElems:
                trackers['found'] += int(elem.text.split(' ')[0])
            if blocked == True:
                tempElems = self.getAllBlockedTrackerElems()
                for elem in tempElems:
                    trackers['blocked'] += int(elem.text.split(' ')[0])
        return trackers

    def isEnhancedOptionsExpanded(self):
        if self.isPlatform("ios"):
            return self.getEnhancedOptionsViewElem().is_displayed()
        else:
            return False if self.getEnhancedOptionsViewElem() == None else True