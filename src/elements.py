import datetime
from src.locators import Locators
from appium.webdriver.common.touch_action import TouchAction as TA


class Elements:

    def getElements(self, elementName, subName=None, baseElement=None, timeout=None):
        s = datetime.datetime.now().replace(microsecond=0)
        self.driver.implicitly_wait(0)
        tempElemList = []
        tries = timer = 0
        if baseElement == None:
            baseElement = self.driver
            baseElemName = self.driver.name if self.driver.name != "" else "WebDriver"
        else:
            baseElemName = baseElement.get_attribute('name')
        if timeout == None:
            timeout = self.implicitWaitTime
        while tempElemList == []:
            if timer >= timeout: break
            if subName == None:
                tempElemList = baseElement.find_elements(*getattr(Locators, elementName)[self.platformName.lower()])
            else:
                tempElemList = baseElement.find_elements(*getattr(Locators, elementName)[subName][self.platformName.lower()])
            self.sleep(0.1)
            timer = (datetime.datetime.now().replace(microsecond=0) - s).seconds
            tries += 1
        if tempElemList == []:
            self.log("*** TEST CASE PROBABLE FAIL *** Element Not Found ! [Tries: {}, Time: {}] BaseElement: {}, ElementName: {}, SubName: {}".format(
                tries, timeout, baseElemName, elementName, subName))
        else:
            self.log("Element Found ! [Tries: {}, Time: {}] BaseElement: {}, ElementName: {}, SubName: {}".format(
                tries, timer, baseElemName, elementName, subName))
        return tempElemList

    def getElement(self, elementName, subName=None, baseElement=None, timeout=None):
        tempElemList = self.getElements(elementName, subName, baseElement, timeout)
        try:
            return tempElemList[0]
        except:
            element = elementName if subName==None else "'{}.{}'".format(elementName, subName)
            raise Exception("Element Not Found: {}".format(element))

    def longPress(self, elem):
        loc = self.centerLocation(elem)
        TA(self.driver).long_press(x=loc['x'], y=loc['y']).release().perform()

    def centerLocation(self, element):
        startXY = element.location
        sizeXY = element.size
        center_x = startXY['x'] + (sizeXY['width']/2)
        center_y = startXY['y'] + (sizeXY['height']/2)
        return {'x': int(center_x), 'y': int(center_y)}
