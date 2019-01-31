import unittest
from utils.testUtils import TestUtils
from pages.pageFreshTab import FreshTab
from pages.pageTabsOverview import TabsOverview
from pages.pageGhosteryCC import GhosteryCC
from pages.pageSettings import Settings
from pages.pageGeckoView import GeckoView
from common.testDataAndRequirements import askLink, defaultSettings, adBlockLink

class TestGhosteryControlCenter:

    @unittest.skipIf(TestUtils().isTestScriptDebug(),
                     "test05_001_GhosteryCCBasicView Test Case will not run as it is NOT Debug Mode.")
    def test05_001_GhosteryCCBasicView(self):
        '''
        :Test Cases:
        - Check if Ghosty Icon is present.
        - Check if the Value below the Ghosty Icon is an Integer.
        - Check if Ghostery CC Appears on clicking Ghosty.
        - Check if Ghostery CC has Overview Button.
        - Check if Ghostery CC has Site Trackers Button.
        - Check if Ghostery CC has All Trackers Button.
        - Check if Ghostery CC Overview Button is selected by Default.
        - Check if Ghostery CC has A Donut.
        - Check if Clicking on Site Trackers Changes the Selection.
        - Check if Clicking on All Trackers Changes the Selection.
        - Check if Ghostery CC Disappears on clicking Ghosty.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        self.log("Check 'Ghostery Control Center' Basic View.", "testsuite")
        PFT.openWebpage(askLink, loadTimeout=5)
        ghosty = PFT.getGhostyButton()
        self.assertNotEqual(ghosty, None, "Check if Ghosty Icon is present.")
        ghostyText = ghosty.tag_name if self.isPlatform("android") else ghosty.text
        self.log("Ghosty Text: " + ghostyText)
        self.assertIsEqual((ghostyText.isdigit() or ghostyText.lower() == "hello"),
                           True, "Check if the Value below the Ghosty Icon is an Integer.")
        ghosty.click()
        PGCC = GhosteryCC(self.settings)
        ghosteryCC = PGCC.getGhosteryCC()
        self.assertNotEqual(ghosteryCC, None, "Check if Ghostery CC Appears on clicking Ghosty.")
        tabsController = PGCC.getGhosteryTabsController(ghosteryCC) if self.isPlatform("ios") else None
        overviewButton = PGCC.getGhosteryOverviewButton(tabsController)
        siteTrackersButton = PGCC.getGhosterySiteTrackersButton(tabsController)
        allTrackersButton = PGCC.getGhosteryAllTrackersButton(tabsController)
        self.assertNotEqual(overviewButton, None, "Check if Ghostery CC has Overview Button.")
        self.assertNotEqual(siteTrackersButton, None, "Check if Ghostery CC has Site Trackers Button.")
        self.assertNotEqual(allTrackersButton, None, "Check if Ghostery CC has All Trackers Button.")
        overviewStatus = self.convertToBool(
            overviewButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        siteTrackersStatus = self.convertToBool(
            siteTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        allTrackersStatus = self.convertToBool(
            allTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        self.log(str(overviewStatus) + " " + str(siteTrackersStatus) + " " + str(allTrackersStatus))
        self.assertIsEqual(overviewStatus and not(siteTrackersStatus and allTrackersStatus),
                           True, "Check if Ghostery CC Overview Button is selected by Default.", noException=True)
        siteTrackersButton.click()
        self.sleep(5)
        overviewButton = PGCC.getGhosteryOverviewButton(tabsController)
        siteTrackersButton = PGCC.getGhosterySiteTrackersButton(tabsController)
        allTrackersButton = PGCC.getGhosteryAllTrackersButton(tabsController)
        overviewStatus = self.convertToBool(
            overviewButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        siteTrackersStatus = self.convertToBool(
            siteTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        allTrackersStatus = self.convertToBool(
            allTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        self.log(str(overviewStatus) + " " + str(siteTrackersStatus) + " " + str(allTrackersStatus))
        self.assertIsEqual(siteTrackersStatus and not (overviewStatus and allTrackersStatus),
                           True, "Check if Clicking on Site Trackers Changes the Selection.", noException=True)
        allTrackersButton.click()
        self.sleep(5)
        overviewButton = PGCC.getGhosteryOverviewButton(tabsController)
        siteTrackersButton = PGCC.getGhosterySiteTrackersButton(tabsController)
        allTrackersButton = PGCC.getGhosteryAllTrackersButton(tabsController)
        overviewStatus = self.convertToBool(
            overviewButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        siteTrackersStatus = self.convertToBool(
            siteTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        allTrackersStatus = self.convertToBool(
            allTrackersButton.get_attribute("value" if self.isPlatform("ios") else "selected"))
        self.log(str(overviewStatus) + " " + str(siteTrackersStatus) + " " + str(allTrackersStatus))
        self.assertIsEqual(allTrackersStatus and not (siteTrackersStatus and overviewStatus),
                           True, "Check if Clicking on All Trackers Changes the Selection.", noException=True)
        overviewButton.click()
        self.sleep(5)
        self.assertNotEqual(PGCC.getGhosteryDonut(), None, "Check if Ghostery CC has A Donut.")
        notch = PGCC.getGhosteryNotch(ghosteryCC)
        self.assertNotEqual(notch, None, "Check if Enhanced Options section or Notch is present.")
        ghosty.click()
        self.assertIsEqual(PGCC.getGhosteryCC(), None, "Check if Ghostery CC Disappears on clicking Ghosty.")
        PFT.openTabsOverview()
        PTO.closeAllTabs()

    @unittest.skipIf(TestUtils().isRequiredPlatform("ios"),
                         "test05_002_GhosteryCCAdBlocking Test Case will not run for IOS.")
    @unittest.skipUnless(TestUtils().isTestScriptDebug(),
                         "test05_002_GhosteryCCAdBlocking Test Case will not run until Tests are fixed.")
    def test05_002_GhosteryCCAdBlocking(self):
        '''
        :Test Cases:
        - Check if Enhanced Options can be Expanded.
        - Check if Enhanced Options can be Collapsed.
        - Check if the AdBlocker Checkbox/Switch is Default Checked/Enabled.
        - Check if the Checkbox/Switch Changes status on Click.
        - Check if AD Block Status is as per the setting of the Feature.
        - Check if AD Block Status is as per the setting of the Feature after it is Changed.
        :return:
        '''
        PFT = FreshTab(self.settings)
        PTO = TabsOverview(self.settings)
        self.log("Check 'Ghostery Control Center - AD Blocking' Feature.", "testsuite")
        # Check USB Debugging. Enable If not already Enabled.
        PFT.disableAddressBar()
        PFT.goToSettings()
        PSM = Settings(self.settings)
        PSM.openOrClickSetting("advanced")
        self.sleep(1)
        if PSM.getStatusValueForSetting('enableRemoteDebugging')['switch'] == False:
            PSM.openOrClickSetting("enableRemoteDebugging")
            self.sleep(1)
        PSM.goOutOfSettings()
        # Verified / Enabled USB Debugging.
        PFT.openWebpage(adBlockLink, loadTimeout=7)
        PGV = GeckoView(self.settings)
        blockStatus = PGV.isADBlocked()
        ghosty = PFT.getGhostyButton()
        ghosty.click()
        PGCC = GhosteryCC(self.settings)
        ghosteryCC = PGCC.getGhosteryCC()
        notch = PGCC.getGhosteryNotch(ghosteryCC)
        PGCC.expandEnhancedOptions(notch)
        self.assertIsEqual(PGCC.isEnhancedOptionsExpanded(), True, "Check if Enhanced Options can be Expanded.")
        PGCC.collapseEnhancedOptions()
        self.assertIsEqual(PGCC.isEnhancedOptionsExpanded(), False, "Check if Enhanced Options can be Collapsed.")
        PGCC.expandEnhancedOptions()
        switch = PGCC.getGhosteryAdBlockerSwitch()
        attrib = "value" if self.isPlatform("ios") else "checked"
        featureStatus = self.convertToBool(switch.get_attribute(attrib))
        self.assertIsEqual(blockStatus, featureStatus, "Check if AD Block Status is as per the setting of the Feature.")
        self.assertIsEqual(featureStatus, defaultSettings['AdBlocking'],
                           "Check if the AdBlocker Checkbox/Switch is Default Checked/Enabled.")
        switch.click()
        self.sleep(1)
        featureStatus = self.convertToBool(switch.get_attribute(attrib))
        self.sleep(1)
        self.assertIsEqual(featureStatus, not defaultSettings['AdBlocking'],
                           "Check if the Checkbox/Switch Changes status on Click.")
        ghosty.click()
        PFT.openWebpage(adBlockLink, loadTimeout=7)
        blockStatus = PGV.isADBlocked()
        self.assertIsEqual(blockStatus, featureStatus,
                           "Check if AD Block Status is as per the setting of the Feature after it is Changed.")
        PFT.openTabsOverview()
        PTO.closeAllTabs()
