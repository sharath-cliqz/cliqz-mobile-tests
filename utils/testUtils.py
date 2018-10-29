from os import environ as ENV

class TestUtils:
    def isRegression(self):
        return ENV.get('TEST_TYPE') == "regression"

    def isTestScriptDebug(self):
        return ENV.get('TEST_TYPE') == "debug"

    def isRequiredPlatform(self, platform):
        return ENV.get('platformName') == platform