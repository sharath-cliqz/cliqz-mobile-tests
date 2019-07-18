from os.path import dirname
from os.path import join
from datetime import datetime
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class BasePage:

    # ===============
    # Class Variables
    # ===============
    driver = None
    logger = None
    config = {}

    # ============
    # Time Methods
    # ============
    @classmethod
    def timestamp(cls, microseconds=False):
        return datetime.now() if microseconds else datetime.now().replace(microsecond=0)

    @classmethod
    def quick_wait(cls, seconds=0.1):
        sleep(seconds)

    # ============
    # File Methods
    # ============
    @classmethod
    def file_data(cls, filename, directory=""):
        relative_path = join(directory, filename)
        absolute_path = join(dirname(__file__), relative_path)
        with open(absolute_path) as file:
            return file.read()

    # ============
    # Driver Methods
    # ============
    @classmethod
    def platform(cls):
        try:
            return cls.config['desiredCaps']['platformName'].lower()
        except Exception as e:
            cls.logger.error(e)
            return ""

    @classmethod
    def is_ios(cls):
        return cls.platform() == "ios"

    @classmethod
    def is_android(cls):
        return cls.platform() == "android"

    # ===================
    # Get Element Methods
    # ===================
    def get_elements(self, locator, base_elem=None, timeout=None):
        s = self.timestamp()
        self.driver.implicitly_wait(0)
        temp_elem_list = []
        tries = timer = 0
        if not base_elem:
            base_elem = self.driver
            base_elem_name = "WebDriver"
        else:
            base_elem_name = base_elem.tag_name
        if not timeout:
            timeout = self.config['implicitWaitTime']
        while not temp_elem_list:
            if timer >= timeout:
                break
            temp_elem_list = base_elem.find_elements(
                *locator[self.platform()] if type(locator) == dict else locator
            )
            self.quick_wait()
            timer = (self.timestamp() - s).seconds
            tries += 1
        if not temp_elem_list:
            self.logger.warning(
                "*** TEST CASE PROBABLE FAIL *** Element Not Found ! [Tries: {}, Time: {}] "
                "BaseElement: {}, LocatorStategy: {}, LocatorString: {}".format(
                    tries, timeout, base_elem_name,
                    *locator[self.platform()] if type(locator) == dict else locator))
        else:
            self.logger.info(
                "Element Found ! [Tries: {}, Time: {}] BaseElement: {}, LocatorStrategy: {}, LocatorString: {}".format(
                    tries, timer, base_elem_name,
                    *locator[self.platform()] if type(locator) == dict else locator))
        return temp_elem_list

    def get_element(self, locator, base_elem=None, timeout=None):
        temp_elem_list = self.get_elements(locator, base_elem, timeout)
        try:
            return temp_elem_list[0]
        except IndexError as ie:
            self.logger.error(ie)
            raise Exception("Element Not Found: {}, {}".format(
                *locator[self.platform()] if type(locator) == dict else locator))

    def long_press(self, elem):
        loc = self.center_location(elem)
        TouchAction(self.driver).long_press(x=loc['x'], y=loc['y']).release().perform()

    @classmethod
    def center_location(cls, element):
        elem_start_loc = element.location
        elem_size = element.size
        center_x = elem_start_loc['x'] + (elem_size['width'] / 2)
        center_y = elem_start_loc['y'] + (elem_size['height'] / 2)
        return {
            'x': int(center_x),
            'y': int(center_y)
        }

    def get_screen_size(self):
        return self.driver.get_window_size()

    def mobile_scroll(self, direction, count=1):
        screen_size = self.get_screen_size()
        start = {'x': screen_size['width'] / 2, 'y': screen_size['height'] / 2}
        end = {}
        offset = 50
        if direction.lower() == "up":
            end = {
                'x': start['x'],
                'y': start['y'] - offset if self.is_ios() else offset
            }
        elif direction.lower() == "down":
            end = {
                'x': start['x'],
                'y': start['y'] + offset
            }
        elif direction.lower() == "left":
            start = {'x': screen_size['width'] - 1, 'y': screen_size['height'] / 2}
            end = {
                'x': 1,
                'y': start['y']
            }
        elif direction.lower() == "right":
            start = {'x': 1, 'y': screen_size['height'] / 2}
            end = {
                'x': screen_size['width'] - 1,
                'y': start['y']
            }
        for i in range(0, count):
            self.logger.info("Swiping from: {}, to: {}.".format(start, end))
            TouchAction(self.driver) \
                .press(x=start['x'], y=start['y']).wait(150) \
                .move_to(x=end['x'], y=end['y']).wait(150) \
                .release().perform()
