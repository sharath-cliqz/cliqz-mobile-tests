'''
This is a page which has all the data about different locators in the application.
Try and make the buttons on Android and iOS come under the same dictionary as much as possible
'''

from appium.webdriver.common.mobileby import MobileBy as MB
from gecko.geckoBy import GeckoBy as GB
from os import environ as OSE
TBD = None
appPackage = OSE.get("appPackage") or OSE.get("TESTDROID_BUNDLE_ID") or ""

class Locators:
    ####################################################################################################################
    #Initial Launch / FreshTab
    ####################################################################################################################
    startBrowsingButton = {
        'android': (MB.ID, appPackage+":id/start_browsing"),
        'ios': (MB.ACCESSIBILITY_ID, "IntroViewController.startBrowsingButton")
    }

    introPager = "//android.support.v4.view.ViewPager[@resource-id='" + appPackage + ":id/cliqz_intro_pager']"
    contentContainer = introPager + "/android.widget.LinearLayout" + \
                       "/android.widget.LinearLayout[@resource-id='" + appPackage + ":id/content_container']"
    onboarding = {}
    onboarding['intro'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Introducing ")]'),
        'android': (MB.XPATH, contentContainer + "/android.widget.TextView")
    }
    onboarding['introCheckbox'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Human Web data ")]'
                          '/../XCUIElementTypeButton'),
        'android': (MB.ID, appPackage + ':id/collect_data_cb')
    }
    onboarding['antiTrackingAdblock'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Ad & Tracker ")]'),
        'android': (MB.XPATH, contentContainer + "/android.widget.TextView")
    }
    onboarding['quickSearch'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[@name="Ghost Search"]'),
        'android': (MB.XPATH, contentContainer + "/android.widget.TextView")
    }
    onboarding['freshTab'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[@name="Start Tab"]'),
        'android': (MB.XPATH, contentContainer + "/android.widget.TextView")
    }
    onboarding['trackerOptionList'] = {
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Ad & Tracker ")]/../XCUIElementTypeOther'),
        'android': (MB.XPATH, contentContainer + "/android.widget.RadioGroup")
    }
    onboarding['trackerButton'] = {
        'ios': (MB.XPATH, './XCUIElementTypeButton'),
        'android': (MB.XPATH, ".//android.widget.RadioButton")
    }

    homeScreenOnboarding = {
        'android': (MB.ID, appPackage + ':id/pwa_onboarding_dismiss')
    }

    addToHomeScreen = {}
    addToHomeScreen['button'] = {
        'android': (MB.ID, appPackage + ':id/page_action_layout')
    }
    addToHomeScreen['rootPanel'] = {
        'android': (MB.ID, appPackage + ':id/pwa_confirm_root')
    }
    addToHomeScreen['link'] = {
        'android': (MB.ID, appPackage + ':id/pwa_confirm_url')
    }
    addToHomeScreen['actionButton'] = {
        'android': (MB.ID, appPackage + ':id/pwa_confirm_action')
    }
    addToHomeScreen['cancelButton'] = {
        'android': (MB.ID, appPackage + ':id/pwa_confirm_cancel')
    }

    topToolBar = {
        'android': (MB.ID, "browser_toolbar"),
        'ios': TBD
    }

    urlBar = {
        'android': (MB.ID, "url_bar_title"),
        'ios': (MB.ACCESSIBILITY_ID, "url")
    }

    urlBarCancel = {
        'android': (MB.ID, appPackage + ':id/edit_cancel'),
        'ios': (MB.ACCESSIBILITY_ID, "urlBar-cancel")
    }

    addressBar = {
        'android': (MB.ID, "url_edit_text"),
        'ios': (MB.ACCESSIBILITY_ID, "address")
    }

    addressBarCancel = {
        'android': (MB.ID, "edit_cancel"),
        'ios': (MB.ACCESSIBILITY_ID, "Cancel")
    }
    addressBarReload = {
        'android': (MB.ID, "reload"),
        'ios': TBD
    }

    pageLoadProgress = {
        'android': (MB.ID, appPackage + ':id/page_progress'),
        'ios': (MB.XPATH, "//XCUIElementTypeProgressIndicator[@name='Progress']")
    }

    siteSecurity = {
        'android': (MB.ID, "site_security"),
        'ios': TBD
    }

    readerViewButton = {
        'android' : (MB.XPATH, "//android.widget.ImageButton[contains(@content-desc, 'Reader View')]"),
        'ios' : (MB.ACCESSIBILITY_ID, "TabLocationView.readerModeButton")
    }

    stopLoadingButton = {
        'android': (MB.ID, "stop"),
        'ios': TBD
    }


    tabsButton = {}
    tabsButton['complete'] = {
        'android': (MB.ID, "tabs_counter"),
        'ios': (MB.ACCESSIBILITY_ID, "TabToolbar.tabsButton")
    }
    tabsButton['counter'] = {
        'android': (MB.ID, "counter_text"),
        'ios': (MB.ACCESSIBILITY_ID, "TabToolbar.tabsButton")
    }

    actionButton = {
        'android' : TBD,
        'ios' : (MB.ACCESSIBILITY_ID, "TabToolbar.menuButton")
    }
    threeDotsButton = {
        'android' : (MB.ID, 'menu'),
        'ios': (MB.ACCESSIBILITY_ID, "UrlBar.pageOptionsButton")
    }

    ####################################################################################################################
    # Tabs Panel
    ####################################################################################################################
    tabsPanel = {}
    tabsPanel['complete'] = {
        'android': (MB.ID, "tabs_panel"),
        'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='Tabs Tray']")
    }
    tabsPanel['header'] = {
        'android': (MB.ID, "tabs_panel_header"),
        'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='Tabs Tray']/XCUIElementTypeOther")
    }
    tabsPanel['header_tabsButton'] = {
        'android': (MB.ID, appPackage + ':id/counter_text'),
        'ios': TBD
    }

    tabsPanel['header_normalTabs'] = {
        'android': (MB.ID, appPackage + ':id/tabs_normal'),
        'ios': TBD
    }
    tabsPanel['header_privateTabs'] = {
        'android': (MB.ID, appPackage + ':id/tabs_private'),
        'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.forgetModeButton")
    }
    tabsPanel['header_addTab'] = {
        'android': (MB.ID, "add_tab"),
        'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.addTabButton")
    }
    tabsPanel['header_tabsMenu'] = {
        'android': (MB.ID, "tabs_menu"),
        'ios': TBD
    }
    tabsPanel['header_closeAllTabsOrDoneButton'] = {
        'android': (MB.XPATH, "//android.widget.TextView[contains(@text, 'Close All Tabs')]"),
        'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.doneButton")
    }
    tabsPanel['header_closeAllTabsConfirmation'] = {
        'android': TBD,
        'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.deleteButton.closeAll")
    }
    tabsPanel['header_closeAllTabsCancel'] = {
        'android': TBD,
        'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Cancel']")
    }
    tabsPanel['tabs_complete'] = {
        'android': (MB.ID, "info"),
        'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='Tabs Tray']/XCUIElementTypeCollectionView/XCUIElementTypeCell")
    }
    tabsPanel['privateTabsEmpty'] = {
        'android': (MB.ID, "private_tabs_empty"),
        'ios': (MB.ACCESSIBILITY_ID, "largePrivateMask")
    }
    tabsPanel['privateTabsText'] = {
        'android': (MB.XPATH, "//android.widget.TextView[contains(@text, 'Private Browsing')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='Tabs Tray']/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]")
    }

    ####################################################################################################################
    # 3 Dots Menu
    ####################################################################################################################
    threeDotsMenu = {}
    threeDotsMenu['complete'] = {'android': (MB.ID, "menu_panel")}
    threeDotsMenu['bookmark'] = {'android': (MB.ID, "bookmark")}
    threeDotsMenu['share'] = {'android': (MB.ID, "share")}
    threeDotsMenu['settings'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Settings']")}
    threeDotsMenu['clearHistory'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Clear browsing history']")}
    threeDotsMenu['openInNewTab'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Open in New Tab']")}
    threeDotsMenu['openInGhostTab'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Open in Ghost Tab']")}
    threeDotsMenu['pinSite'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Pin Site']")}
    threeDotsMenu['addPageShortcut'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Add Page Shortcut']")}
    threeDotsMenu['delete'] = {'android': (MB.XPATH, "//android.widget.TextView[@text='Delete']")}

    ####################################################################################################################
    # Action Menu
    ####################################################################################################################
    actionMenu = {}
    actionMenu['complete'] = {'ios': (MB.ACCESSIBILITY_ID, "ActivityListView")}
    actionMenu['TopSites'] = {'ios': (MB.ACCESSIBILITY_ID, "Top Sites")}
    actionMenu['Bookmarks'] = {'ios': (MB.ACCESSIBILITY_ID, "Bookmarks")}
    actionMenu['readingList'] = {'ios': (MB.ACCESSIBILITY_ID, "Reading List")}
    actionMenu['history'] = {'ios': (MB.ACCESSIBILITY_ID, "History")}
    actionMenu['settings'] = {'ios': (MB.ACCESSIBILITY_ID, "Settings")}
    actionMenu['hideImages'] = {'ios': (MB.ACCESSIBILITY_ID, "Hide Images")}
    actionMenu['nightMode'] = {'ios': (MB.ACCESSIBILITY_ID, "Night Mode")}
    actionMenu['cancel'] = {'ios': (MB.ACCESSIBILITY_ID, "Cancel")}

    ####################################################################################################################
    # Fresh Tab :: Top Sites
    ####################################################################################################################
    topSites = {}
    topSites['complete'] = {
        'android': (MB.XPATH, "//android.support.v4.view.ViewPager[@resource-id='"+appPackage+":id/topsites_pager']"),
        'ios': (MB.XPATH, "//XCUIElementTypeCollectionView[@name='topSites']")
    }
    topSites['site'] = {
        'android': (MB.XPATH, ".//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout"),
        'ios': (MB.XPATH, "./XCUIElementTypeCell/XCUIElementTypeOther")
    }
    topSites['icon'] = {
        'android': (MB.XPATH, ".//android.widget.ImageView"),
        'ios': (MB.XPATH, "./XCUIElementTypeOther/XCUIElementTypeImage")
    }
    topSites['text'] = {
        'android': (MB.XPATH, ".//android.widget.TextView"),
        'ios': (MB.XPATH, "./XCUIElementTypeStaticText")
    }
    topSites['delete'] = {
        'ios': (MB.XPATH, "./XCUIElementTypeButton[@name='removeTopsite']")
    }


    ####################################################################################################################
    # Fresh Tab :: News Section
    ####################################################################################################################
    newsTitle = {
        'android' : (MB.ID, 'news_title'),
        'ios': (MB.XPATH, '//XCUIElementTypeStaticText[@name="NEWS"]')
    }
    moreNews = {
        'android': (MB.ID, 'news_title'),
        'ios': (MB.ACCESSIBILITY_ID, 'Show More')
    }
    lessNews = {
        'android': (MB.ID, 'news_title'),
        'ios': (MB.ACCESSIBILITY_ID, 'Show Less')
    }
    newsSection = {
        'android': (MB.ID, 'news_recyclerview'),
        'ios': (MB.XPATH, '//XCUIElementTypeTable[@name="topNews"]')
    }
    newsArticle = {
        'android': (MB.ID, 'title_view'),
        'ios': (MB.XPATH, '//XCUIElementTypeTable[@name="topNews"]/XCUIElementTypeCell')
    }
    newsURL = {
        'android': (MB.ID, 'url_view'),
        'ios': (MB.XPATH, '//XCUIElementTypeTable[@name="topNews"]/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
    }

    ####################################################################################################################
    # Fresh Tab Panel
    ####################################################################################################################
    freshTabPanel = {}
    freshTabPanel['topSites'] = {
        'android': (MB.ID, appPackage+":drawable/ic_home_cliqz"),
        'ios': (MB.ACCESSIBILITY_ID, "panelIconFreshtab")
    }
    freshTabPanel['favorites'] = {
        'android': (MB.ID, appPackage+":drawable/ic_star_white"),
        'ios': (MB.ACCESSIBILITY_ID, "panelIconFavorite")
    }
    freshTabPanel['history'] = {
        'android': (MB.ID, appPackage+":drawable/ic_history_white"),
        'ios': (MB.ACCESSIBILITY_ID, "panelIconCliqzHistory")
    }
    freshTabPanel['offerz'] = {
        'android': (MB.ID, appPackage+":drawable/ic_offrz_white"),
        'ios': (MB.ACCESSIBILITY_ID, "panelIconOffrz")
    }

    ####################################################################################################################
    # Fresh Tab :: History View
    ####################################################################################################################
    historyEmpty = {
        'android': (MB.ID, "home_history_empty_view")
    }
    historyComplete = {
        #'android': (MB.ID, "combined_recycler_view"),
        'android': (MB.XPATH, "//android.support.v7.widget.RecyclerView"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable[@name='History List']")
    }
    historyItem = {
        'android': (MB.XPATH,
                    "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/"
                    "android.widget.LinearLayout[./android.widget.TextView[@resource-id='"+
                    appPackage+":id/url']]"),
        'ios': (MB.XPATH, "./XCUIElementTypeCell")
    }
    historyText = {
        'android': (MB.CLASS_NAME, "android.widget.TextView"),
        'ios': (MB.XPATH, "./XCUIElementTypeStaticText")
    }
    clearHistory = {}
    clearHistory["button"] = {
        'android': (MB.ID, appPackage+":id/history_panel_footer_button")
    }
    clearHistory['buttonPanel'] = {
        'android': (MB.ID, "android:id/button")
    }
    clearHistory['accept'] = {
        'android': (MB.ID, "android:id/button1")
    }
    clearHistory['cancel'] = {
        'android': (MB.ID, "android:id/button2")
    }

    ####################################################################################################################
    # Settings Menu
    ####################################################################################################################
    settingsDoneButton = {
        'android': (MB.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
        'ios': (MB.ACCESSIBILITY_ID, "AppSettingsTableViewController.navigationItem.leftBarButtonItem")
    }
    settingsBackToMenu = {
        'android': (MB.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
        'ios': (MB.ACCESSIBILITY_ID, "Settings")
    }
    settingsContentMenu = {
        'android': (MB.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']")
    }
    settingsMenu = {}
    settingsMenu['settingsPrefsFrame'] = {
        'android': (MB.ID, "android:id/prefs_frame"),
        'ios': (MB.XPATH, "//XCUIElementTypeNavigationBar[@name='Settings']")
    }
    settingsMenu['settingsSubMenu'] = {
        'android': (MB.XPATH, "//android.view.View[@resource-id='"+appPackage+":id/action_bar']/android.widget.TextView")
    }
    settingsMenu["complete"] = {
        'android': (MB.ID, "android:id/list"),
        'ios': (MB.ACCESSIBILITY_ID, "AppSettingsTableViewController.tableView")
    }
    settingsMenu['general'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='General']")
    }
    settingsMenu['privacy'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='Privacy']")
    }
    settingsMenu['advanced'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='Advanced']")
    }
    settingsMenu['checkbox'] = {
        'android': (MB.XPATH, ".//android.widget.LinearLayout[@resource-id='android:id/widget_frame']/"
                              "android.widget.CheckBox")
    }
    settingsMenu['switch'] = {
        'android': (MB.XPATH, ".//android.widget.LinearLayout[@resource-id='android:id/widget_frame']/"
                              "android.widget.Switch"),
        'ios': (MB.XPATH, "./XCUIElementTypeSwitch")
    }
    settingsMenu['settingSummary'] = {
        'android': (MB.XPATH, ".//android.widget.RelativeLayout/android.widget.TextView[@resource-id='android:id/summary']"),
        'ios': (MB.XPATH, "./XCUIElementTypeStaticText[2]")
    }

    settingsMenu['searchResultsFor'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Search results for']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Search Results for']]")
    }
    settingsMenu['blockExplicitContent'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Block explicit content']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Block Explicit Content']]")
    }
    settingsMenu['humanWeb'] = {
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Human Web']]")
    }
    settingsMenu['enableAutocompletion'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Enable Autocompletion']]")
    }
    settingsMenu['quickSearch'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Enable Ghost Search']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Quick Search']]")
    }
    settingsMenu['complementarySearch'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Complementary search engine']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Complementary Search']]")
    }
    settingsMenu['backgroundImage'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Show background image']]")
    }
    settingsMenu['mostVisitedWebsites'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Show most visited websites']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Show most visited websites']]")
    }
    settingsMenu['news'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Show News']]"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell["
                          "./XCUIElementTypeStaticText[@name='Show News']]")
    }

    settingsMenu['enableRemoteDebugging'] = {
        'android': (MB.XPATH, "//android.widget.LinearLayout["
                              "./android.widget.RelativeLayout/android.widget.TextView["
                              "@resource-id='android:id/title' and @text='Remote debugging via USB']]")
    }

    settingsMenu['clearPrivateData'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='Clear private data']"),
        'ios': (MB.ACCESSIBILITY_ID, "ClearPrivateData")
    }

    searchResultsForList = {}
    searchResultsForList['cancel'] = {
        'android': (MB.XPATH, "//android.widget.Button[@text='Cancel']")
    }
    searchResultsForList['Germany'] = {
        'android': (MB.XPATH, "//android.widget.ListView/android.widget.CheckedTextView[@text='Germany']"),
        'ios': (MB.XPATH, "	//XCUIElementTypeStaticText[@name='Germany']")
    }
    searchResultsForList['France'] = {
        'android': (MB.XPATH, "//android.widget.ListView/android.widget.CheckedTextView[@text='France']"),
        'ios': (MB.XPATH, "	//XCUIElementTypeStaticText[@name='France']")
    }
    searchResultsForList['United States'] = {
        'android': (MB.XPATH, "//android.widget.ListView/android.widget.CheckedTextView[@text='United States']"),
        'ios': (MB.XPATH, "	//XCUIElementTypeStaticText[@name='United States']")
    }

    complementarySearchList = {}
    complementarySearchList['set'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']"
                              "/android.widget.TextView[contains(@text, 'Set')]")
    }
    complementarySearchList['google'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Google')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'Google')]")
    }
    complementarySearchList['amazon'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Amazon')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'Amazon')]")
    }
    complementarySearchList['duckduckgo'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'DuckDuckGo')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'DuckDuckGo')]")
    }
    complementarySearchList['bing'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Bing')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'Bing')]")
    }
    complementarySearchList['twitter'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Twitter')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'Twitter')]")
    }
    complementarySearchList['wikipedia'] = {
        'android': (MB.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout"
                              "/android.widget.LinearLayout/android.widget.TextView[contains(@text, 'Wikipedia')]"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell"
                          "/XCUIElementTypeStaticText[contains(@name, 'Wikipedia')]")
    }

    clearPrivateDataList = {}
    clearPrivateDataList['cancel'] = {
        'android': (MB.XPATH, "//android.widget.Button[@text='Cancel']")
    }
    clearPrivateDataList['clearData'] = {
        'android': (MB.XPATH, "//android.widget.Button[@text='Clear data']"),
        'ios': (MB.XPATH, "//XCUIElementTypeStaticText[@name='Clear Private Data']")
    }
    clearPrivateDataList['confirmationAccept'] = {
        'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='OK']")
    }
    clearPrivateDataList['confirmationCancel'] = {
        'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Cancel']")
    }
    clearPrivateDataList['browsingHistory'] = {
        'android': (MB.XPATH, "//android.widget.CheckedTextView[@text='History']"),
        'ios': (MB.XPATH, "//XCUIElementTypeSwitch[@name='Browsing History']")
    }

    ####################################################################################################################
    #Gecko Driver Connection Alert
    ####################################################################################################################
    geckoConnAlert = {}
    geckoConnAlert['title'] = {
        'android': (MB.ID, "alertTitle"),
        'ios': TBD
    }
    geckoConnAlert['message'] = {
        'android': (MB.ID, "message"),
        'ios': TBD
    }
    geckoConnAlert['deny'] = {
        'android': (MB.XPATH, "//android.widget.Button[contains(@text,'Deny')]"),
        'ios': TBD
    }
    geckoConnAlert['allow'] = {
        'android': (MB.XPATH, "//android.widget.Button[contains(@text,'Allow')]"),
        'ios': TBD
    }

    ####################################################################################################################
    #Gecko Elements
    ####################################################################################################################
    testWikiLangElem = {
        'android': (GB.CLASS_NAME, "central-featured-lang")
    }
    testEnBox = {
        'android': (GB.ID, "js-link-box-en")
    }
    adBlockElems = {}
    adBlockElems['allGood'] = {
        'android': (GB.ID, "all-good")
    }
    adBlockElems['noBlocking'] = {
        'android': (GB.ID, "no-blocking")
    }

    ####################################################################################################################
    # Debug Elements (Works only if Automation Flag is set for iOS while building the APP)
    ####################################################################################################################
    debugElem = {}
    debugElem['settingsButton'] = {
        'ios': (MB.ACCESSIBILITY_ID, "SettingsButton")
    }

    ####################################################################################################################
    # Performance/Benchmarks Related Locators
    ####################################################################################################################
    googleChrome = {}
    googleChrome['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Search or type URL']")}
    googleChrome['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='Address']")}

    mozillaFirefox = {}
    mozillaFirefox['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='url']")}
    mozillaFirefox['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='url']")}

    appleSafari = {}
    appleSafari['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='URL']")}
    appleSafari['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='URL']")}

    jetStream = {}
    jetStream['startTest'] = {'ios': (MB.XPATH, "//XCUIElementTypeLink[@name='Start Test']")}
    jetStream['testAgain'] = {'ios': (MB.XPATH, "//XCUIElementTypeLink[@name='Test Again']")}
    jetStream['scoreMainElem'] = {'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='Score']/..")}
    jetStream['scoreElems'] = {'ios': (MB.XPATH, "./XCUIElementTypeStaticText")}

    speedometer = {}
    speedometer['startTest'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Start Test']")}
    speedometer['testAgain'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Test Again']")}
    speedometer['scoreMainElem'] = {'ios': (MB.XPATH, "//XCUIElementTypeOther[@name='main']")}
    speedometer['scoreElems'] = {'ios': (MB.XPATH, "./XCUIElementTypeOther/XCUIElementTypeStaticText")}

    javaScript = {}
    javaScript['beginTest'] = {'ios': (MB.XPATH, "//XCUIElementTypeLink[@name='Begin']")}
    javaScript['runAgain'] = {'ios': (MB.XPATH, "//XCUIElementTypeLink[@name='Run Again']")}
    javaScript['score'] = {'ios': (MB.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Total: ')]")}

    basemark = {}
    basemark['startTest'] = {'ios': (MB.XPATH, "//XCUIElementTypeLink[@name='Start']")}
    basemark['breakdown'] = {'ios': (MB.XPATH, "//XCUIElementTypeStaticText[@name='score:']")}
    basemark['score'] = {'ios': (MB.XPATH,
                                 "//XCUIElementTypeOther[@name='Basemark Web 3.0 | Main page']/XCUIElementTypeOther[5]/XCUIElementTypeStaticText")}

    ares = {}
    ares['startTest'] = {'ios': (MB.XPATH,
                                 "//XCUIElementTypeOther[@name='banner']/XCUIElementTypeButton[@name='START']")}
    ares['restart'] = {'ios': (MB.XPATH,
                               "//XCUIElementTypeOther[@name='banner']/XCUIElementTypeButton[@name='RESTART']")}
    ares['score'] = {'ios': (MB.XPATH,
                             "//XCUIElementTypeOther[@name='main']/XCUIElementTypeOther[3]/XCUIElementTypeStaticText")}

    motionMark = {}
    motionMark['runBench'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Run Benchmark']")}
    motionMark['testAgain'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Test Again']")}
    motionMark['score'] = {'ios': (MB.XPATH,
                             "//XCUIElementTypeOther[@name='main']/XCUIElementTypeOther[2]/XCUIElementTypeStaticText")}

    ####################################################################################################################
    # Ghostery Control Center
    ####################################################################################################################
    ghostyButton = {
        'android': (MB.ID, appPackage+":id/ghosty"),
        'ios': (MB.ACCESSIBILITY_ID, "ghosty")
    }

    ghosteryControlCenter = {}
    ghosteryControlCenter['complete'] = {
        'android': (MB.ID, appPackage + ":id/control_center_container"),
        'ios': (MB.XPATH, "//XCUIElementTypeSegmentedControl/../..")
    }
    ghosteryControlCenter['tabsController'] = {
        'android': (MB.ID, appPackage + ":id/conrol_center_tab_layout"),
        'ios': (MB.XPATH, "*/XCUIElementTypeSegmentedControl")
    }
    ghosteryControlCenter['overview'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='OVERVIEW']"),
        'ios': (MB.XPATH, "/*/XCUIElementTypeButton[@name='Overview']")
    }
    ghosteryControlCenter['siteTrackers'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='SITE TRACKERS']"),
        'ios': (MB.XPATH, "/*/XCUIElementTypeButton[@name='Trackers']")
    }
    ghosteryControlCenter['allTrackers'] = {
        'android': (MB.XPATH, "//android.widget.TextView[@text='ALL TRACKERS']"),
        'ios': (MB.XPATH, "/*/XCUIElementTypeButton[@name='All Trackers']")
    }
    ghosteryControlCenter['donut'] = {
        'android': (MB.ID, appPackage+":id/cc_donut"),
        'ios': (MB.ACCESSIBILITY_ID, "donut")
    }
    ghosteryControlCenter['notch'] = {
        'android': (MB.ID, appPackage+":id/cc_notch_title"),
        'ios': (MB.ACCESSIBILITY_ID, "notch")
    }
    ghosteryControlCenter['enhancedOptionsView'] = {
        'android': (MB.ID, appPackage + ":id/cc_overview_view"),
        'ios': (MB.ACCESSIBILITY_ID, "adblocking")
    }
    ghosteryControlCenter['adBlockerSwitch'] = {
        'android': (MB.ID, appPackage + ":id/cc_enhanced_blocking_switch"),
        'ios': (MB.XPATH, "//XCUIElementTypeImage[@name='adblocking']/../XCUIElementTypeSwitch")
    }
    ghosteryControlCenter['trackerList'] = {
        'android': (MB.ID, appPackage + ":id/trackers_list"),
        'ios': (MB.XPATH, "//XCUIElementTypeTable")
    }
    ghosteryControlCenter['trackerCategory'] = {
        'android': (MB.ID, appPackage + ":id/main_layout"),
        'ios': (MB.XPATH, "./XCUIElementTypeOther")
    }
    ghosteryControlCenter['trackerCategoryName'] = {
        'android': (MB.ID, appPackage + ":id/category_name"),
        'ios': (MB.XPATH, "./XCUIElementTypeStaticText")
    }
    ghosteryControlCenter['totalTrackersElem'] = {
        'android': (MB.ID, appPackage + ":id/total_trackers")
    }
    ghosteryControlCenter['blockedTrackersElem'] = {
        'android': (MB.ID, appPackage + ":id/blocked_trackers")
    }
    ghosteryControlCenter['trackersCountElem'] = {
        'ios': (MB.XPATH, "*/XCUIElementTypeStaticText[contains(@name, 'Blocked')]")
    }
    ghosteryControlCenter['trackerName'] = {
        'android': (MB.ID, appPackage + ":id/tracker_name"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell/XCUIElementTypeStaticText[@name!='Swipe']")
    }
    ghosteryControlCenter['trackerBlockStatus'] = {
        'android': (MB.ID, appPackage + ":id/cb_block_tracker"),
        'ios': (MB.XPATH, "//XCUIElementTypeCell/XCUIElementTypeImage")
    }
    ghosteryControlCenter['expandCollapseCategory'] = {
        'ios': (MB.XPATH, "./XCUIElementTypeStaticText[@name='On this site']")
    }