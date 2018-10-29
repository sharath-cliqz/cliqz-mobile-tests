class AppUtils:

    def minimizeKeyboard(self):
        try:
            self.settings.driver.hide_keyboard()
            self.log("Keyboard Minimized.")
            return True
        except:
            self.log("Keyboard was already minimized.")
            return False

    def androidBackKey(self, count=1):
        for i in range(0, count):
            self.settings.driver.press_keycode(4)
            self.sleep(0.25)