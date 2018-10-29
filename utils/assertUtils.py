class AssertUtils:
    def assertIsEqual(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") == (" + str(b) + ") ?")
            self.log(msg, "pass" if a == b else "fail", noException=noException, benchScore=benchScore)

    def assertNotEqual(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") != (" + str(b) + ") ?")
            self.log(msg, "pass" if a != b else "fail", noException=noException, benchScore=benchScore)

    def assertIsIn(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") IN (" + str(b) + ") ?")
            self.log(msg, "pass" if a in b else "fail", noException=noException, benchScore=benchScore)

    def assertNotIn(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") NOT-IN (" + str(b) + ") ?")
            self.log(msg, "pass" if a not in b else "fail", noException=noException, benchScore=benchScore)

    def assertLessThan(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") < (" + str(b) + ") ?")
            self.log(msg, "pass" if a < b else "fail", noException=noException, benchScore=benchScore)

    def assertGreaterThan(self, a, b, msg, noException=False, skipIf=None, skipMessage="", benchScore=None):
        if self.isPlatform(skipIf):
            self.log(msg, "skip")
            self.log(skipMessage)
        else:
            self.log("TEST :: (" + str(a) + ") > (" + str(b) + ") ?")
            self.log(msg, "pass" if a > b else "fail", noException=noException, benchScore=benchScore)