from test01BasicView import TestBasicView
from test02SettingsMenu import TestSettingsMenu
from test03FreshTabFeatures import TestFreshTabFeatures
from test04UserTabFeatures import TestUserTabFeatures
from test05GhosteryControlCenter import TestGhosteryControlCenter
from test06SearchFeatures import TestSearchFeatures

class CompleteSuite(
    TestBasicView,
    TestSettingsMenu,
    TestFreshTabFeatures,
    TestUserTabFeatures,
    TestGhosteryControlCenter,
    TestSearchFeatures
):
    def ignore(self):
        pass
