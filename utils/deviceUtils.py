import json
from appium.webdriver.common.touch_action import TouchAction as TA
from common.exceptionList import ScriptFailure

class DeviceUtils:

    def isPlatform(self, platform):
        return self.settings.platform_name == str(platform).lower()

    def onScreenSwipe(self, start, dirOrEnd):
        '''
        This is a method to swipe on the screen in the direction passed as the parameter starting from the start parameter
        :param start: This is the co-ordinates or element for the initial tap
        :param dir: This is the direction in which the tapped location is to be dragged. Accepted dir: "left", "right", "up", "down" or it should be a Dict as {"x": value, "y": value}
        :return: 
        :Use: This will be mainly used to swipe delete elements or close tabs.
        '''
        if type(dirOrEnd) is str:
            end = {
                'x': None,
                'y': None
            }
            #max = self.driver.get_window_size()
            if dirOrEnd.lower() == "left":
                end['x'] = -100 #if start['x']>100 else 1
                end['y'] = 0
            elif dirOrEnd.lower() == "right":
                end['x'] = 100 #if start['x']<max['width']-100 else max['width']-1
                end['y'] = 0
            elif dirOrEnd.lower() == "up":
                end['x'] = 0
                end['y'] = -100#start['y']-100 if start['y']>100 else 1
            elif dirOrEnd.lower() == "down":
                end['x'] = 0
                end['y'] = 100 #if start['y']<max['height']-100 else max['height']-1
            self.log("Swiping towards the given Direction.")
            self.settings.driver.swipe(start['x'], start['y'], end['x'], end['y'])
        elif type(dirOrEnd) is dict and ("x" and "y") in dirOrEnd.keys():
            self.log("Swiping with an End Location.")
            self.settings.driver.swipe(start['x'], start['y'], dirOrEnd['x'], dirOrEnd['y'])
        else:
            self.log("The second Parameter should be Either a Direction as String or an End Location as a Dict.")

    def centerLocation(self, element):
        '''
        This is a method to find the center of the element pased as the parameter
        :param element: Pass the instance of an element found by the driver.
        :return: Returns the Center of the element as a dictionary {'x': center_x, 'y': center_y}
        '''
        startXY = element.location
        sizeXY = element.size
        center_x = startXY['x'] + (sizeXY['width']/2)
        center_y = startXY['y'] + (sizeXY['height']/2)
        return {'x': int(center_x), 'y': int(center_y)}

    def getTelemetryLogs(self):
        if self.settings.platform_name == 'ios':
            logtype='syslog'
            marker='[Telemetry]'
            replaceChars = "\"; \t\n:{}\\"
        else:
            logtype='logcat'
            marker='TELEMETRY_DEBUG'
            replaceChars = "\"; \t\n{}\\"
        log = self.driver.get_log(logtype)
        flag = False
        events = []
        tempEvent = {}
        if self.settings.platform_name=='ios':
            for item in log:
                self.settings.fullLog.append(item)
                if '\t}' in item['message'] and flag == True:
                    flag = False
                elif flag == True:
                    eventData = self.parseEventData(item['message'], replaceChars)
                    tempEvent[eventData[0]] = eventData[1]
                elif marker in item['message']:
                    if tempEvent != {}:
                        if tempEvent not in self.settings.eventsList:
                            events.append(tempEvent)
                            self.settings.eventsList.append(tempEvent)
                        tempEvent = {}
                    flag = True
        else:
            for item in log:
                self.settings.fullLog.append(item)
                if marker in item['message']:
                    #tempEvent={}
                    data=item['message'].split(marker+": ")[1]
                    tempEvent = json.loads(data)
                    '''data=data.split(",")
                    for d in data:
                        eventData = self.parseEventData(d, replaceChars)
                        tempEvent[eventData[0]] = eventData[1]
                    events.append(tempEvent)'''
                    if tempEvent not in self.settings.eventsList:
                        events.append(tempEvent)
                        self.settings.eventsList.append(tempEvent)
        return events

    def parseEventData(self, data, replaceChars):
        if data=="":
            print "Empty String"
            return None
        else:
            data = data.replace("\\n", "")
            for c in replaceChars:
                data = data.replace(c, "")
            if self.settings.platform_name=='ios': data = data.split("=")
            else:
                data=data.split(":")
            if len(data)<2:
                if data[0]=="": data[0] = "*Empty*"
                data.append("*Empty*")
            return data

    def prettyPrintEvents(self, event, telemetryFile=None):
        string = ""
        if "Test Method" in event:
            string += "\n\n***"+str(event['Test Method'])+"***\n"
        else:
            string += "\n** Event **\n"
            for eventData in event.keys():
                string += str(eventData) + ": " + str(event[eventData]) + "\n"
        if telemetryFile==None:
            print string
        else:
            telemetryFile.write(string)

    def longPress(self, elem):
        loc = self.centerLocation(elem)
        TA(self.settings.driver).long_press(x=loc['x'], y=loc['y']).release().perform()

    def clickElemCenter(self, elem, pressTime=100):
        loc = self.centerLocation(elem)
        TA(self.settings.driver).press(x=loc['x'], y=loc['y']).wait(pressTime).release().perform()

    def tapOnLoc(self, loc, pressTime=100):
        TA(self.settings.driver).press(x=loc['x'], y=loc['y']).wait(pressTime).release().perform()

    def getScreenSize(self):
        return self.settings.driver.get_window_size()

    def mobileScroll(self, start=None, end=None, direction="", count=1):
        if start == None:
            screenSize = self.getScreenSize()
            start = {'x': screenSize['width']/2, 'y': screenSize['height']/2}
        offset = 150 if self.settings.device_type != "default" else 50
        if end == None and direction == "":
            raise ScriptFailure("Enter End Point or a Direction.")
        elif end == None and direction != "":
            if direction.lower() == "up":
                end = {
                    'x': start['x'],
                    'y': start['y'] - offset if self.isPlatform("ios") else offset
                }
            elif direction.lower() == "down":
                end = {
                    'x': start['x'],
                    'y': start['y'] + offset
                }
            elif direction.lower() == "left":
                start = {'x': screenSize['width'] - 1, 'y': screenSize['height'] / 2}
                end = {
                    'x': 1,
                    'y': start['y']
                }
            elif direction.lower() == "right":
                start = {'x': 1, 'y': screenSize['height'] / 2}
                end = {
                    'x': screenSize['width'] - 1,
                    'y': start['y']
                }
        elif end != None and direction != "":
            self.log("End Point will take preference and the direction will be ignored.")
        for i in range(0, count):
            self.log(str(start) + " to " + str(end))
            TA(self.settings.driver)\
                .press(x=start['x'], y=start['y']).wait(150)\
                .move_to(x=end['x'], y=end['y']).wait(150)\
                .release().perform()

    def changeOrientation(self, setOrientation=None):
        if setOrientation == None:
            orientation = str(self.settings.driver.orientation)
            if orientation == "LANDSCAPE":
                self.settings.driver.orientation = "PORTRAIT"
            elif orientation == "PORTRAIT":
                self.settings.driver.orientation = "LANDSCAPE"
        else:
            self.settings.driver.orientation = setOrientation.upper()