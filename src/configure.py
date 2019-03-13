import os
from ast import literal_eval
from argparse import Namespace


class Configure(Namespace):

    def __init__(self, config):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        with open(scriptDir+"/configs/driver.config", "r") as fp:
            driverConfigs = literal_eval(fp.read())
        Namespace.__init__(self, **driverConfigs)
        with open(scriptDir+"/configs/"+config, "r") as fp:
            appConfigs = literal_eval(fp.read())
        Namespace.__init__(self, **appConfigs)
        self.platformName = self.desiredCaps['platformName']