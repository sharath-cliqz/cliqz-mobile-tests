import time, random, string, inspect, datetime
from common.locators import Locators
from common.exceptionList import *

class ScriptUtils:

    def getElements(self, elementName, subName=None, baseElement=None, timeout=None, absNoScr=True, noLog=False):
        s = datetime.datetime.now().replace(microsecond=0)
        self.settings.driver.implicitly_wait(0)
        tries = timer = 0
        if baseElement == None: baseElement = self.settings.driver
        tempElemList = []
        if timeout == None or self.settings.BitBar == True: timeout = self.settings.implicitWaitTime
        while tempElemList == []:
            if timer >= timeout: break
            if subName == None:
                tempElemList = baseElement.find_elements(*getattr(Locators, elementName)[self.settings.platform_name])
            else:
                tempElemList = baseElement.find_elements(*getattr(Locators, elementName)[subName][self.settings.platform_name])
            timer = (datetime.datetime.now().replace(microsecond=0) - s).seconds
            tries += 1
        if noLog == False:
            if tempElemList == []:
                self.log("*** TEST CASE PROBABLE FAIL *** Element Not Found ! [Tries: " + str(tries) + ", Time: " + str(
                    timeout) + "]BaseElement: " + str(baseElement) + ", ElementName: " + str(
                    elementName) + ", SubName: " + str(subName), absNoScr=absNoScr)
            else:
                self.log("Element Found ! [Tries: " + str(tries) + ", Time: " + str(timer) + "]BaseElement: " + str(
                    baseElement) + ", ElementName: " + str(elementName) + ", SubName: " + str(subName))
        return tempElemList

    def getElement(self, elementName, subName=None, baseElement=None, timeout=None, absNoScr=False, noLog=False):
        tempElemList = self.getElements(elementName, subName, baseElement, timeout, absNoScr, noLog=noLog)
        try:
            return tempElemList[0]
        except:
            element = elementName if subName==None else "'"+elementName+"."+subName+"'"
            raise ScriptFailure("Element Not Found: "+element)

    def getGeckoElements(self, elementName, subName=None, timeout=None, absNoScr=True, noLog=False):
        s = datetime.datetime.now().replace(microsecond=0)
        tries = timer = 0
        tempElemList = []
        if timeout == None: timeout = 10
        while tempElemList == []:
            if timer >= timeout: break
            if subName == None:
                tempElemList = self.settings.getGeckoDriver().getElements(*getattr(Locators, elementName)[self.settings.platform_name])
            else:
                tempElemList = self.settings.getGeckoDriver().getElements(
                    *getattr(Locators, elementName)[subName][self.settings.platform_name])
            timer = (datetime.datetime.now().replace(microsecond=0) - s).seconds
            tries += 1
        if noLog == False:
            if tempElemList == []:
                self.log("*** TEST CASE PROBABLE FAIL *** Element Not Found ! [Tries: " + str(tries) + ", Time: " + str(
                    timeout) + "]ElementName: " + str(elementName) + ", SubName: " + str(subName), absNoScr=absNoScr)
            else:
                self.log("Element Found ! [Tries: " + str(tries) + ", Time: " + str(timer) + "]ElementName: " + str(
                    elementName) + ", SubName: " + str(subName))
        return tempElemList

    def getGeckoElement(self, elementName, subName=None, timeout=None, absNoScr=False, noLog=False):
        tempElemList = self.getGeckoElements(elementName, subName, timeout, absNoScr, noLog=noLog)
        try:
            return tempElemList[0]
        except:
            element = elementName if subName==None else "'"+elementName+"."+subName+"'"
            raise GeckoFailure("Element Not Found: "+element)

    def screenshot(self, name, override=False, absNoScr=False):
        try:
            testName = str(self.id()).split(".")[-1]+"_"
        except:
            testName = "Unknown_"
        app_brand = self.settings.app_brand.replace("-", "_")
        if absNoScr == False:
            if self.settings.takeScreenshot == True or override == True:
                timer = time.strftime("%H-%M-%S")
                for ch in ['\\', '`', '*', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'', '/', ' ']:
                    if ch in name:
                        name = name.replace(ch, "")
                screenshot_name = app_brand + testName + str(self.settings.screenshot_count) + "_" + name + "_" + timer + ".png"
                self.log("Taking screenshot: " + screenshot_name)
                self.settings.driver.save_screenshot(self.screenshot_dir + "/" + screenshot_name)
                self.settings.screenshot_count += 1
                return screenshot_name

    def log(self, msg, testStatus=None, absNoScr=False, noException=False, benchScore=None):
        msg = str(msg)
        func = inspect.currentframe().f_back.f_code
        timer = time.strftime("%H:%M:%S")
        if self.settings.recordLogs == True:
            if testStatus == None:
                self.settings.logger.info("%s :: [INFO] :: %s(%s)[%i] :: %s" %
                                          (timer, func.co_name, func.co_filename.split('/')[-1], func.co_firstlineno, msg))
            elif testStatus.lower() == 'fail':
                scr_name = self.screenshot("FAIL_" + msg, override=True, absNoScr=absNoScr)
                self.settings.logger.error("%s :: [ERROR] :: %s(%s)[%i] :: TEST CASE FAILED :: %s :: Screenshot: %s" %
                                           (timer, func.co_name, func.co_filename.split('/')[-1], func.co_firstlineno, msg, scr_name))
                for k, v in self.settings.fullReport.iteritems():
                    if self._testMethodName[:6] in k:
                        testSuite = k
                if msg in self.settings.fullReport[testSuite][self._testMethodName]:
                    self.settings.fullReport[testSuite][self._testMethodName][msg] = "xFAILx"
                self.settings.featureTestCount['total']+=1
                self.settings.featureTestCount['fail']+=1
                if noException == False: raise TestFailure(msg)
            elif testStatus.lower() == 'pass':
                self.settings.logger.info("%s :: [INFO] :: %s(%s)[%i] :: TEST CASE PASSED :: %s" %
                                          (timer, func.co_name, func.co_filename.split('/')[-1], func.co_firstlineno, msg))
                for k, v in self.settings.fullReport.iteritems():
                    if self._testMethodName[:6] in k:
                        testSuite = k
                if msg in self.settings.fullReport[testSuite][self._testMethodName]:
                    if benchScore == None:
                        self.settings.fullReport[testSuite][self._testMethodName][msg] = " PASS "
                    else:
                        self.settings.fullReport[testSuite][self._testMethodName][msg] = " ["+benchScore+"] "
                self.settings.featureTestCount['total'] += 1
                self.settings.featureTestCount['pass'] += 1
            elif testStatus.lower() == 'skip':
                self.settings.logger.info("%s :: [INFO] :: %s(%s)[%i] :: TEST CASE SKIPPED :: %s" %
                                          (timer, func.co_name, func.co_filename.split('/')[-1], func.co_firstlineno, msg))
                for k, v in self.settings.fullReport.iteritems():
                    if self._testMethodName[:6] in k:
                        testSuite = k
                if msg in self.settings.fullReport[testSuite][self._testMethodName]:
                    self.settings.fullReport[testSuite][self._testMethodName][msg] = "{SKIP}"
                self.settings.featureTestCount['total'] += 1
                self.settings.featureTestCount['skip'] += 1
            elif testStatus.lower() == 'testsuite':
                self.settings.logger.info("%s :: [INFO] :: *** TEST SUITE: %s ***" % (timer, msg))
                self.settings.fullLog.append({"message": "\n\n\n\n*** TEST SUITE: " + msg + " ***\n\n"})
                self.settings.eventsList.append({"Test Method": "*** TEST SUITE: "+msg+" ***"})

    def generateRandomString(self, l=10, spchar=False):
        '''
        This method can be used to create a random string of a particular length.
        :param l: This is the length of string which will be generated. Default is 10.
        :return: Returns a string generated randomly.
        '''
        if spchar==True:
            return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#+-") for _ in range(l))
        else:
            return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(l))

    def listDiff(self, a, b):
        newList = []
        for x in a:
            if x not in b:
                newList.append(x)
        for x in b:
            if x not in a:
                newList.append(x)
        return newList

    def convertToBool(self, x):
        trueList = [1, "1", "true", "True", "TRUE", True, "on", "ON", "On"]
        falseList = [0, "0", "false", "False", "FALSE", False, "off", "OFF", "Off"]
        if x in trueList:
            return True
        elif x in falseList:
            return False