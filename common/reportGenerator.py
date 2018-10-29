import testSuites, inspect, pkgutil, performanceSuites, os

class ReportGenerator:
    def __init__(self):
        self.testSuiteData = {}

    def isTestMethod(self, modname, line):
        '''
        This checks if the line is a Test Case Defenition.
        :param modname: Passed from the inspect modname.
        :param line: Passed from the inspect line.
        :return: The Test Case Method Name or False
        '''
        if "def test" in line and "(self):" in line:
            return line.strip().replace("def ", "").replace("(self):", "")
        else:
            return False

    def generator(self):
        package = performanceSuites if os.environ.get('TEST_TYPE') == "performance" else testSuites
        testName = ""
        testCaseListStatus = False
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            lines = inspect.getsourcelines(importer.find_module(modname).load_module(modname))
            self.testSuiteData[modname] = {}
            for line in lines[0]:
                data = self.isTestMethod(modname, line)
                if data != False:
                    testName = data
                    self.testSuiteData[modname][testName] = {}
                if line.strip() == ":Test Cases:":
                    testCaseListStatus = True
                elif line.strip() == ":return:":
                    testCaseListStatus = False
                elif testCaseListStatus == True:
                    self.testSuiteData[modname][testName][line.strip()[2:]] = " -NR- "
        return self.testSuiteData