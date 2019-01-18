'''
This is a python file to store all test Data and Requirements which will be used in all the Test Suites.
'''

########################################################################################################################
# Default Settings Data
########################################################################################################################
defaultWebLink = "https://cdn.cliqz.com/mobile/browser/tests/testHome.html"
humanWebLink = "https://cliqz.com/en/whycliqz/human-web"
tipsLink = "https://cliqz.com/en/tips-android"
reportWebsiteLink = "https://cliqz.com/en/report-url"
imprintLink = "https://cliqz.com/en/legal"
imprintLink2 = "https://cliqz.com/legal"
readerModeLink = "https://cdn.cliqz.com/mobile/browser/tests/readermodetest.html"
redditLink = "https://www.reddit.com"
instagramLink = "https://www.instagram.com/"
flashscoreLink = "http://www.flashscore.mobi/"
askLink = "https://www.ask.com/"
adBlockLink = "https://blockads.fivefilters.org/"
defaultNewsCount = {
    'android': 3,
    'ios': 2
}

########################################################################################################################
# Default Settings Data
########################################################################################################################
defaultSettings = {}

defaultSettings['searchResultsFor'] = ["Germany", "United States"]  #List of Strings
defaultSettings['blockExplicitContent'] = True  #Boolean: True or False
defaultSettings['humanWeb'] = "On"
defaultSettings['enableAutocompletion'] = True
defaultSettings['quickSearch'] = True
defaultSettings['complementarySearch'] = "DuckDuckGo"

defaultSettings['backgroundImage'] = True
defaultSettings['mostVisitedWebsites'] = True
defaultSettings['news'] = True

defaultSettings['SearchQuerySuggestions'] = True
defaultSettings['NewsNotifications'] = True
defaultSettings['BlockPopupWindows'] = True  #Boolean: True or False
defaultSettings['AdBlocking'] = True  #Boolean: True(ON) or False(OFF)
defaultSettings['Anti-Tracking'] = True
defaultSettings['LocationAccess'] = False
defaultSettings['EnableCookies'] = True
defaultSettings['SavePasswords'] = True
defaultSettings['ClearCacheOnExit'] = False
defaultSettings['ClearHistoryOnExit'] = False
defaultSettings['ClearCookiesOnExit'] = False
defaultSettings['ClearDataOnExit'] = False
defaultSettings['ClearDataOnExitList'] = {
    'Tabs': False,
    'cache': False,
    'history': False,
    'cookies': False
}


########################################################################################################################
# Onboarding
########################################################################################################################
onBoardingWebpage = ["time.com", "spiegel.de", "cleartrip.com", "economist.com", "booking.com"]
onBoardingVideoWebpage = "https://m.youtube.com/watch?v=iAuP33O1nDE"
homeScreenButtonOnboardingLink = instagramLink
onBoardingPage1 = ["Introducing Cliqz", "Welcome"]
onBoardingPage2 = "Ad & Tracker Blocking"
onBoardingPage3 = "Ghost Search"
onBoardingPage4 = ["Start Tab", "Cliqz Tab"]


########################################################################################################################
# Test Data for Search Results For
########################################################################################################################
searchResultsFor = {}
searchResultsFor['Germany'] = {'google': 'google.de', 'amazon': 'amazon.de'}
searchResultsFor['France'] = {'sport': 'sports.fr', 'amazon': 'amazon.fr'}
searchResultsFor['United States'] = {'google': 'google.com', 'amazon': 'amazon.com'}


########################################################################################################################
# Test Data for Explicit Content
########################################################################################################################
explicitContent = {
    'pornhub': "pornhub.com",
    'youporn': "youporn.com"
}


########################################################################################################################
# Test Data for Complementary Search
########################################################################################################################
comSearch = ['duckduckgo', 'google', 'bing', 'amazon', 'twitter', 'wikipedia']

########################################################################################################################
# Test Data for Pop-up Test
########################################################################################################################
popupTest = "https://cdn.cliqz.com/mobile/browser/tests/popup_test.html"
imageTest = "https://cdn.cliqz.com/mobile/browser/tests/single_image.html"


########################################################################################################################
# Test Data for AutoCompletion
########################################################################################################################
autoCompleteContent = {
    'cliq': "cliqz.",
    'clicker': "clickerheroes."
}


########################################################################################################################
# Test Data for Native History
########################################################################################################################
nativeHistoryList = [
    {
        'query': "blahblahblah"
    },
    {
        'url': "www.joindota.com"
    },
    {
        'url': "maps.google.com"
    },
    {
        'query': "panama papers wikipedia"
    },
    {
        'url': "wikipedia.org"
    },
    {
        'query': "AMD Zen+ release date"
    }
]