import datetime


class Browser:

    def getBrowserName(self):
        if self.browserName != None:
            return self.browserName
        else:
            if 'browserName' in self.desiredCaps:
                bID = self.desiredCaps['browserName']
            else:
                bID = self.desiredCaps['bundleId']
            bName = ["Chrome", "Mozilla", "Cliqz", "Safari"]
            for name in bName:
                if (name in bID) or (name.lower() in bID):
                    self.browserName = name
                    return name

    def enableAddressBar(self):
        try:
            addressBar = self.getElement("addressBar", timeout=3)
            addressBar.click()
            return addressBar
        except Exception as e:
            try:
                self.log(e)
                self.getElement("urlBar", timeout=1).click()
                return self.getElement("addressBar", timeout=1)
            except Exception as e:
                self.log(e)
                raise Exception("Address Bar could not be Enabled/Does not Exist.")

    def findAddressBar(self):
        browser = self.getBrowserName()
        if browser == "Cliqz":
            self.skipOnboarding()
            return self.enableAddressBar()
        elif browser in ["Chrome", "Safari"]:
            self.getElement(browser.lower(), "urlBar", timeout=10, absNoScr=True).click()
            return self.getElement(browser.lower(), "addressBar", timeout=10)
        else:
            return self.getElement(browser.lower(), "addressBar", timeout=10)

    def waitForReloadButton(self, button=None):
        button = self.stopReloadButton() if button == None else button
        error = datetime.datetime.now()
        while (not button.text == "Reload") and ((datetime.datetime.now() - error).seconds < 60):
            error = datetime.datetime.now()
            self.sleep(0.25)
        return datetime.datetime.now() - error

    def stopReloadButton(self):
        return self.getElement("stopReloadButton", timeout=1)

    def skipOnboarding(self):
        if not self.onboardingComplete:
            try:
                self.getElement("startBrowsingButton", timeout=3).click()
                self.log("Skipped Onboarding.")
            except Exception as e:
                self.log(e)
                self.log("Seems like Onboarding did not appear.")
            self.onboardingComplete = True
        else:
            self.log("Onboarding already Skipped.")

    def resetBrowser(self):
        self.driver.reset()
        self.onboardingComplete = False
        self.sleep(2)

    def closeAllTabs(self):
        self.longPress(self.getElement("doneButton"))
        try:
            self.getElement("closeAllTabsConfirmation").click()
        except:
            self.longPress(self.getElement("doneButton"))
            self.getElement("closeAllTabsConfirmation").click()
        self.sleep(3)

    def openTabsOverview(self):
        self.getElement("tabsButton", timeout=1).click()