import socket, json, subprocess, time, os
from pages.shared.alertBox import AlertBox
from geckoBy import GeckoBy
from common.exceptionList import *

class GeckoElement:
    def __init__(self, geckoDriver, locatorStrategy, locatorVariable, listIndex=None):
        self.strategy = locatorStrategy #TBD. For now only ID and CLASS_NAME works.
        self.variable = locatorVariable
        self.driver = geckoDriver
        self.index = listIndex

    def click(self):
        return self.driver.clickEvent(self.strategy, self.variable, self.index)

    def getText(self):
        return self.driver.getTextEvent(self.strategy, self.variable, self.index)

    def getAttribute(self, attrib):
        return self.driver.getAttributeValueEvent(attrib, self.strategy, self.variable, self.index)



class GeckoDriver:
    '''
        This is the driver which can be used to communicate with the GeckoView of the Android Browser.
    '''
    def __init__(self, settings):
        self.timeout = 1
        appPackage = os.environ.get('appPackage') or "org.mozilla.fennec_"
        try:
            subprocess.Popen(
                ["adb", "forward", "tcp:6000", "localfilesystem:/data/data/"+appPackage+"/firefox-debugger-socket"],
                stdout=subprocess.PIPE)
            settings.logger.info(subprocess.check_output(["adb", "forward", "--list"]))
        except Exception as e:
            settings.logger.warning(e)
            settings.logger.warning("Error with Port Forwarding for Firefox Debugger Socket.")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 6000))
        time.sleep(1)
        AlertBox(settings).acceptDegbugger()
        # Get ACK
        self.receivePackets()
        # Get Actors
        self.consoleActor = None
        parsedData = self.communicate('{"to":"root","type":"getProcess"}')
        for data in parsedData:
            if "form" in data and "consoleActor" in data["form"]:
                self.consoleActor = parsedData[0]["form"]["consoleActor"]
        if self.consoleActor == None: raise GeckoFailure("Console Actor Not Found !!")

    def sendData(self, data):
        if data != None:
            data = str(len(data)) + ":" + data
            self.sock.send(data)

    def receivePackets(self):
        self.sock.setblocking(0)
        totalData = []
        start = time.time()
        while 1:
            if totalData and time.time() - start > self.timeout:
                break
            elif time.time() - start > self.timeout*2:
                break
            try:
                data = self.sock.recv(8096)
                if data:
                    totalData.append(data)
                    start = time.time()
                else:
                    time.sleep(0.1)
            except:
                pass
        return ''.join(totalData)

    def dataParser(self, dataSet):
        result = []
        while dataSet != "":
            temp = dataSet.split(":", 1)
            num = int(temp[0])
            result.append(json.loads(temp[1][:num]))
            dataSet = temp[1][num:]
        return result

    def communicate(self, data):
        self.sendData(data)
        return self.dataParser(self.receivePackets())

    def prettyPrint(self, parsedData):
        if isinstance(parsedData, list):
            for data in parsedData:
                print json.dumps(data, indent=4, sort_keys=True)
        else:
            print json.dumps(parsedData, indent=4, sort_keys=True)

    def getElementById(self, id):
        elementFound = False
        sendData = '{"to":"' + self.consoleActor + '",' \
                   '"type":"evaluateJSAsync",' \
                   '"text":"BrowserApp.selectedTab.browser.contentDocument.'+GeckoBy.ID+'(\''+id+'\').text",' \
                   '"frameActor":null,"selectedNodeActor":null}'
        parsedData = self.communicate(sendData)
        for data in parsedData:
            if "exception" in data and data["exception"]==None:
                elementFound = True
                return GeckoElement(self, GeckoBy.ID, id)
        if elementFound == False:
            raise GeckoFailure("Element Not Found !")

    def getElements(self, locatorStrategy, locatorValue):
        elementData = []
        if locatorStrategy == GeckoBy.ID:
            elementData.append(self.getElementById(locatorValue))
        else:
            sendData = '{"to":"' + self.consoleActor + '",' \
                       '"type":"evaluateJSAsync",' \
                       '"text":"BrowserApp.selectedTab.browser.contentDocument.'+locatorStrategy + \
                       '(\''+locatorValue+'\')","frameActor":null,"selectedNodeActor":null}'
            parsedData = self.communicate(sendData)
            actor = parsedData[1]["result"]["actor"]
            sendData = '{"to":"' + actor + '","type":"enumProperties","options":{"ignoreNonIndexedProperties":true}}'
            parsedData = self.communicate(sendData)
            sendData = '{"to":"' + parsedData[0]["iterator"]["actor"] + '","type":"slice","start":0,"count":' + str(
                parsedData[0]["iterator"]["count"]) + '}'
            parsedData = self.communicate(sendData)
            if "ownProperties" in parsedData[0]:
                for key in parsedData[0]["ownProperties"]:
                    if key != "length":
                        elementData.append(GeckoElement(self, locatorStrategy, locatorValue, int(key)))
            else:
                raise GeckoFailure(parsedData[0]["exception"] if "exception" in parsedData[0] else self.prettyPrint(parsedData))
        return elementData

    def clickEvent(self, locatorStrategy, locatorVariable, listIndex=None):
        locator = locatorStrategy+'(\'' + locatorVariable +'\')'
        if listIndex != None:
            locator = locator + '['+str(listIndex)+']'
        sendData = '{"to":"' + self.consoleActor + '",' \
            '"type":"evaluateJSAsync",' \
            '"text":"BrowserApp.selectedTab.browser.contentDocument.'+locator+\
            '.click()","frameActor":null,"selectedNodeActor":null}'
        parsedData = self.communicate(sendData)
        for data in parsedData:
            if "exception" in data and data["exception"] == None:
                return True
        return False

    def getTextEvent(self, locatorStrategy, locatorVariable, listIndex=None):
        text = ""
        locator = locatorStrategy + '(\'' + locatorVariable + '\')'
        if listIndex != None:
            locator = locator + '[' + str(listIndex) + ']'
        sendData = '{"to":"' + self.consoleActor + '",' \
           '"type":"evaluateJSAsync",' \
           '"text":"BrowserApp.selectedTab.browser.contentDocument.'+locator+\
           '.innerText","frameActor":null,"selectedNodeActor":null}'
        parsedData = self.communicate(sendData)
        for data in parsedData:
            if "exception" in data and data["exception"] == None and "result" in data:
                text = data["result"]
        return text

    def getAttributeValueEvent(self, attrib, locatorStrategy, locatorVariable, listIndex=None):
        value = ""
        locator = locatorStrategy + '(\'' + locatorVariable + '\')'
        if listIndex != None:
            locator = locator + '[' + str(listIndex) + ']'
        sendData = '{"to":"' + self.consoleActor + '",' \
                                                   '"type":"evaluateJSAsync",' \
                                                   '"text":"BrowserApp.selectedTab.browser.contentDocument.' + locator + \
                   '.getAttribute(\''+ attrib +'\')","frameActor":null,"selectedNodeActor":null}'
        parsedData = self.communicate(sendData)
        for data in parsedData:
            if "exception" in data and data["exception"] == None and "result" in data:
                value = data["result"]
        return value