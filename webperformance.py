import datetime
from src.driver import Driver


class WebPerformance(Driver):

    browserName = None
    onboardingComplete = False
    weblist = [
        "http://www.spiegel.de",
        "http://time.com",
        "http://independent.co.uk",
        "http://timesnownews.com",
        "http://nytimes.com",
        "http://sueddeutsche.de"
    ]

    def webPerformance(self):
        errorTime = datetime.datetime.now() - datetime.datetime.now()
        result = {}
        for i in range(1,self.repeatCount+1):
            if self.getBrowserName() == "Cliqz":
                self.skipOnboarding()
                reloadButton = self.stopReloadButton()
            self.log("*** Run Number: {} ***".format(i))
            for link in self.weblist:
                if self.getBrowserName() == "Cliqz":
                    addressBar = self.findAddressBar()
                    s = datetime.datetime.now()
                    addressBar.set_value(link + "\n")
                    errorTime = self.waitForReloadButton(reloadButton)
                else:
                    s = datetime.datetime.now()
                    self.driver.get(link)
                e = datetime.datetime.now()
                resultTime = e-s-errorTime
                self.log(link + " ::: " + resultTime.__str__())
                if i == 1:
                    result[link] = {self.getBrowserName(): resultTime}
                elif i == self.repeatCount:
                    oldValue = result[link][self.getBrowserName()]
                    avgResult = (oldValue + resultTime)/self.repeatCount
                    result[link] = {self.getBrowserName(): avgResult.__str__()}
                else:
                    oldValue = result[link][self.getBrowserName()]
                    resultTime += oldValue
                    result[link] = {self.getBrowserName(): resultTime}
            if self.getBrowserName() == "Cliqz":
                self.openTabsOverview()
                self.closeAllTabs()
            self.resetBrowser()
            if i == self.repeatCount:
                self.log("*** Run Complete ***")
        with open(self.getBrowserName()+".txt", "w") as fp:
            fp.write(str(result))

    def main(self):
        self.startDriver()
        self.webPerformance()
        self.quitDriver()


if __name__ == "__main__":
    WebPerformance().main()