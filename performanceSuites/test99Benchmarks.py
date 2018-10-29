class Benchmarks:

    # Test Defaults
    benchTimeout = 1800
    webElemTimeout = 60

    # Benchmark Links
    jetStreamTestLink = "https://browserbench.org/JetStream/"
    speedometerTestLink = "https://browserbench.org/Speedometer2.0/"
    javaScriptTestLink = "https://krakenbenchmark.mozilla.org/"
    basemarkTestLink = "https://web.basemark.com/"
    aresTestLink = "https://browserbench.org/ARES-6/"
    motionMarkTestLink = "https://browserbench.org/MotionMark/"

    def getBrowserName(self):
        bID = self.settings.desired_caps_ios['bundleId']
        if "chrome" in bID:
            return "GoogleChrome"
        elif "mozilla" in bID:
            return "MozillaFirefox"
        elif "cliqz" in bID:
            return "Cliqz"
        elif "safari" in bID:
            return "AppleSafari"

    def findAddressBar(self):
        bID = self.settings.desired_caps_ios['bundleId']
        if "chrome" in bID:
            self.getElement("googleChrome", "urlBar", timeout=10, absNoScr=True).click()
            return self.getElement("googleChrome", "addressBar", timeout=10)
        elif "mozilla" in bID:
            return self.getElement("mozillaFirefox", "addressBar", timeout=10)
        elif "safari" in bID:
            self.getElement("appleSafari", "urlBar", timeout=10, absNoScr=True).click()
            return self.getElement("appleSafari", "addressBar", timeout=10)
        elif "cliqz" in bID:
            try:
                self.getElement("startBrowsingButton", timeout=3, absNoScr=True).click()
            except:
                pass
            self.getElement("urlBar", timeout=3, absNoScr=True).click()
            return self.getElement("addressBar", timeout=10)

    def test99_001_BenchJetStream(self):
        '''
        :Test Cases:
        - Jetstream Benchmark.
        :return:
        '''
        addressBar = self.findAddressBar()
        addressBar.set_value(self.jetStreamTestLink + "\n")
        self.getElement("jetStream", "startTest", timeout=self.webElemTimeout).click()
        self.getElement("jetStream", "testAgain", timeout=self.benchTimeout)
        self.screenshot("Benchmark-Jetstream-"+self.getBrowserName(), override=True)
        scoreMainElem = self.getElement("jetStream", "scoreMainElem", timeout=self.webElemTimeout)
        scores = self.getElements("jetStream", "scoreElems", baseElement=scoreMainElem, timeout=self.webElemTimeout)
        finalScore = ""
        for score in scores:
            if "Score" not in score.text:
                finalScore += score.text
        self.log("Score: " + finalScore)
        self.assertNotEqual(finalScore, " ", "Jetstream Benchmark.", benchScore=finalScore)

    def test99_002_BenchJavaScript(self):
        '''
        :Test Cases:
        - JavaScript Benchmark.
        :return:
        '''
        addressBar = self.findAddressBar()
        addressBar.set_value(self.javaScriptTestLink + "\n")
        self.getElement("javaScript", "beginTest", timeout=self.webElemTimeout).click()
        self.getElement("javaScript", "runAgain", timeout=self.benchTimeout)
        self.screenshot("Benchmark-JavaScript-"+self.getBrowserName(), override=True)
        finalScore = self.getElement("javaScript", "score", timeout=self.webElemTimeout).text
        finalScore = finalScore.replace("Total: ", "")
        finalScore = finalScore.replace(" ", "")
        self.log("Score: "+finalScore)
        self.assertNotEqual(finalScore, "", "JavaScript Benchmark.", benchScore=finalScore)

    def test99_003_BenchAres(self):
        '''
        :Test Cases:
        - Ares6 Benchmark.
        :return:
        '''
        addressBar = self.findAddressBar()
        addressBar.set_value(self.aresTestLink + "\n")
        self.getElement("ares", "startTest", timeout=self.webElemTimeout).click()
        self.getElement("ares", "restart", timeout=self.benchTimeout)
        for x in range(1, 6):
            self.mobileScroll(direction="up")
            self.screenshot("Benchmark-Ares6-Pt"+str(x)+"-"+self.getBrowserName(), override=True)
        finalScore = self.getElement("ares", "score", timeout=self.webElemTimeout).text
        self.log("Score: "+finalScore)
        self.assertNotEqual(finalScore, "", "Ares6 Benchmark.", benchScore=finalScore)
        self.mobileScroll(direction="down", count=5)

    def test99_004_BenchMotionMark(self):
        '''
        :Test Cases:
        - Motion Mark Benchmark.
        :return:
        '''
        addressBar = self.findAddressBar()
        self.changeOrientation("LANDSCAPE")
        addressBar.set_value(self.motionMarkTestLink + "\n")
        self.mobileScroll(direction="up", count=3)
        self.getElement("motionMark", "runBench", timeout=self.webElemTimeout).click()
        self.getElement("motionMark", "testAgain", timeout=self.benchTimeout)
        self.changeOrientation("PORTRAIT")
        self.screenshot("Benchmark-MotionMark-"+self.getBrowserName(), override=True)
        finalScore = self.getElement("motionMark", "score", timeout=self.webElemTimeout).text
        self.log("Score: "+finalScore)
        self.assertNotEqual(finalScore, "", "Motion Mark Benchmark.", benchScore=finalScore)

    def test99_005_BenchSpeedometer(self):
        '''
        :Test Cases:
        - Speedometer 2.0 Benchmark.
        :return:
        '''
        self.changeOrientation("PORTRAIT")
        addressBar = self.findAddressBar()
        addressBar.set_value(self.speedometerTestLink + "\n")
        self.getElement("speedometer", "startTest", timeout=self.webElemTimeout).click()
        self.getElement("speedometer", "testAgain", timeout=self.benchTimeout)
        self.screenshot("Benchmark-Speedometer-"+self.getBrowserName(), override=True)
        scoreMainElem = self.getElement("speedometer", "scoreMainElem", timeout=self.webElemTimeout)
        scores = self.getElements("speedometer", "scoreElems", baseElement=scoreMainElem, timeout=self.webElemTimeout)
        finalScore = ""
        for score in scores:
            if "Runs" not in score.text:
                finalScore += score.text
        self.log("Score: " + finalScore)
        self.assertNotEqual(finalScore, "", "Speedometer 2.0 Benchmark.", benchScore=finalScore)

    def test99_006_BenchBaseMark(self):
        '''
        :Test Cases:
        - BaseMark Benchmark.
        :return:
        '''
        addressBar = self.findAddressBar()
        addressBar.set_value(self.basemarkTestLink + "\n")
        self.getElement("basemark", "startTest", timeout=self.webElemTimeout).click()
        self.getElement("basemark", "breakdown", timeout=self.benchTimeout*2)
        self.screenshot("Benchmark-BaseMark-Pt1-"+self.getBrowserName(), override=True)
        finalScore = self.getElement("basemark", "score", timeout=self.webElemTimeout).text
        self.mobileScroll(direction="up", count=3)
        self.screenshot("Benchmark-BaseMark-Pt2-"+self.getBrowserName(), override=True)
        self.log("Score: "+finalScore)
        self.assertNotEqual(finalScore, "", "BaseMark Benchmark.", benchScore=finalScore)