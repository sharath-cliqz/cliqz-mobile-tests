from appium.webdriver.common.mobileby import MobileBy as MB


class Locators:

    startBrowsingButton = {'ios': (MB.ACCESSIBILITY_ID, "IntroViewController.skipIntroButton")}
    tabsButton = {'ios': (MB.ACCESSIBILITY_ID, "TabToolbar.tabsButton")}
    doneButton = {'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.doneButton")}
    closeAllTabsConfirmation = {'ios': (MB.ACCESSIBILITY_ID, "TabTrayController.deleteButton.closeAll")}

    urlBar = {'ios': (MB.ACCESSIBILITY_ID, "url")}

    addressBar = {'ios': (MB.ACCESSIBILITY_ID, "address")}

    stopReloadButton = {'ios': (MB.ACCESSIBILITY_ID, "TabToolbar.stopReloadButton")}

    chrome = {}
    chrome['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='Search or type URL']")}
    chrome['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='Address']")}

    mozilla = {}
    mozilla['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='url']")}
    mozilla['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='url']")}

    safari = {}
    safari['urlBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='URL']")}
    safari['addressBar'] = {'ios': (MB.XPATH, "//XCUIElementTypeTextField[@name='URL']")}
    safari['stop'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='StopButton']")}
    safari['reload'] = {'ios': (MB.XPATH, "//XCUIElementTypeButton[@name='ReloadButton']")}