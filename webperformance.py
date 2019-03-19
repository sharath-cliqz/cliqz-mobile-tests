import datetime
from src.driver import Driver
from src.getlist import getLinksFromFile


class WebPerformance(Driver):

    browserName = None
    onboardingComplete = False
    weblist = getLinksFromFile()

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
                    result[link] = {}
                    result[link][self.getBrowserName()] = {i: resultTime}
                elif i == self.repeatCount:
                    total = resultTime
                    for value in result[link][self.getBrowserName()].values():
                        total += value
                    result[link][self.getBrowserName()][i] = resultTime
                    result[link][self.getBrowserName()]["avg"] = total/self.repeatCount
                else:
                    result[link][self.getBrowserName()][i] = resultTime
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