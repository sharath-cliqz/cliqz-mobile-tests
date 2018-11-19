from common.exceptionList import *
from common import testDataAndRequirements as TDR
from action3DotsMenu import Action3DotsMenu

class TopBar(Action3DotsMenu):
    def getURLBar(self):
        try:
            return self.getElement("urlBar", timeout=3, absNoScr=True)
        except:
            return None

    def urlBarCancel(self):
        try:
            return self.getElement("urlBarCancel", timeout=3, absNoScr=True)
        except:
            return None

    def getAddressBar(self):
        try:
            return self.getElement("addressBar", timeout=1, absNoScr=True)
        except:
            return None

    def getAddressBarCancel(self):
        try:
            return self.getElement("addressBarCancel", timeout=1, absNoScr=True)
        except:
            return None

    def getPageLoadBar(self, noLog=False):
        try:
            return self.getElement("pageLoadProgress", timeout=1, absNoScr=True, noLog=noLog)
        except:
            return None

    def getTabsButton(self):
        try:
            return self.getElement("tabsButton", "complete", timeout=1, absNoScr=True)
        except:
            raise TopBarFailure("Tabs Button is not Present.")

    def getGhostyButton(self):
        try:
            return self.getElement("ghostyButton", timeout=1, absNoScr=True)
        except:
            return None

    def getStopLoadingButton(self):
        try:
            return self.getElement("stopLoadingButton", timeout=1, absNoScr=True)
        except:
            return None

    def enableAddressBar(self):
        try:
            addressBar = self.getElement("addressBar", timeout=3, absNoScr=True)
            addressBar.click()
            return addressBar
        except Exception as e:
            try:
                self.log(e)
                self.getElement("urlBar", timeout=1, absNoScr=True).click()
                return self.getElement("addressBar", timeout=1, absNoScr=True)
            except Exception as e:
                self.log(e)
                raise TopBarFailure("Address Bar could not be Enabled/Does not Exist.")

    def disableAddressBar(self):
        try:
            try:
                self.minimizeKeyboard()
            except:
                self.log("Looks like Keyboard is already Minimized.")
            try:
                self.urlBarCancel().click()
            except:
                self.log("Probably URL Bar is already present.")
            return self.getURLBar()
        except Exception as e:
            self.log(e)
            raise TopBarFailure("URL Bar could not be Enabled/Does not Exist.")

    def clearAndCancelAddressBar(self):
        try:
            self.getElement("addressBarCancel", timeout=1, absNoScr=True).click()
        except Exception as e:
                self.log(e)
                raise TopBarFailure("Address Bar could not be Cleared/Clear Button does not Exist.")

    def getTabsCount(self):
        if self.isPlatform("ios"):
            return 0
        else:
            try:
                return int(self.getElement("tabsButton", "counter", timeout=1, absNoScr=True).text)
            except:
                raise TopBarFailure("Looks like Tabs Button is not Present to get the count.")

    def openTabsOverview(self):
        try:
            try:
                self.minimizeKeyboard()
                self.getAddressBarCancel().click()
            except Exception as e:
                self.log(e)
            finally:
                self.getTabsButton().click()
        except Exception as e:
            self.log(e)
            raise TopBarFailure("Cannot open Tabs Overview.")

    def getReaderModeButton(self):
        try:
            return self.getElement('readerViewButton', timeout=5)
        except:
            try:
                self.getElement('stopLoadingButton', timeout=2).click()
                return self.getElement('readerViewButton', timeout=3)
            except:
                self.log('ReaderModeButton is not there')
                return None

    def getReaderModeStatus(self):
        button = self.getReaderModeButton()
        if button == None: raise TopBarFailure("Reader Mode Button not Found.")
        if self.isPlatform("ios"):
            if button.get_attribute('value') == '1':
                return False
            else: return True
        elif self.isPlatform("android"):
            if button.tag_name == 'Enter Reader View':
                return True
            elif button.tag_name == 'Close Reader View':
                return False

    def getURLString(self):
        try:
            self.getURLBar().click()
            if self.isPlatform("ios"):
                url = self.getURLBar().text
            else:
                url = self.getAddressBar().text
            self.sleep(2)
            try:
                self.getAddressBarCancel().click()
            except:
                self.androidBackKey(2)
            return url
        except:
            return None

    def openWebpage(self, link=TDR.defaultWebLink, loadTimeout=3):
        if self.isPlatform("ios"):
            self.enableAddressBar().set_value(link + "\n")
        else:
            self.enableAddressBar().set_value(link)
            self.settings.driver.press_keycode(66)
        '''startTime = presentTime = datetime.datetime.now().replace(microsecond=0)
        loadComplete = False
        while ((presentTime - startTime).seconds <= loadTimeout) and loadComplete == False:
            if self.getPageLoadBar(noLog=True) == None:
                loadComplete = True
            presentTime = datetime.datetime.now().replace(microsecond=0)'''
        self.sleep(loadTimeout)
        return self.getURLBar().text

    def getAutoCompletedValue(self, string, timeout=1):
        addressBar = self.enableAddressBar()
        addressBar.set_value(string)
        self.sleep(timeout)
        return addressBar.text

    def get3DotButton(self):
        if self.isPlatform("ios"):
            self.disableAddressBar()
        return self.getElement("threeDotsButton", timeout=2)

    def getAddToHomeScreenButton(self):
        try:
            return self.getElement("addToHomeScreen", "button", timeout=2, absNoScr=True)
        except Exception as e:
            self.log(e)
            try:
                if self.isPlatform("android"):
                    self.get3DotButton().click()
                    try:
                        self.getElement('stopLoadingButton', timeout=2).click()
                    except Exception as e:
                        self.log(e)
                    finally:
                        self.androidBackKey()
                        self.sleep(1)
                else:
                    self.getElement('stopLoadingButton', timeout=2).click()
                return self.getElement("addToHomeScreen", "button", timeout=2, absNoScr=True)
            except Exception as e:
                self.log(e)
                raise TopBarFailure("Add to Home Screen Button was not Found.")

    def getAddToHomeScreenActionButton(self):
        try:
            return self.getElement("addToHomeScreen", "actionButton", timeout=3, absNoScr=True)
        except Exception as e:
            self.log(e)
            return None

    def getAddToHomeScreenCancelButton(self):
        try:
            return self.getElement("addToHomeScreen", "cancelButton", timeout=3, absNoScr=True)
        except Exception as e:
            self.log(e)
            return None

    def getAddToHomeScreenLink(self):
        try:
            return self.getElement("addToHomeScreen", "link", timeout=3, absNoScr=True)
        except Exception as e:
            self.log(e)
            return None

    def getAddToHomeScreenRootPanel(self):
        try:
            return self.getElement("addToHomeScreen", "rootPanel", timeout=1, absNoScr=True)
        except Exception as e:
            self.log(e)
            return None