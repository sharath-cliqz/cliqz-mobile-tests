#!/usr/bin/env bash

# *** IMPORTANT ***    (But this can also be set in Environment Variables, and will not reset it, if already set)
if [ "${platformName}" == "" ]; then
    # ** IMPORTANT **  SET THE PLATFORN NAME HERE !!  ios or android (all lower case)
    export platformName=""
else
    echo "Platform Name is already set."
    echo "Platform Name: ${platformName}"
fi

# Check if Platform Name is set.
if [ "${platformName}" == "" ]; then
    echo "\n\n\nPlatform Name is not Set !! \nPlease set it in scripts/envs.sh\n\n"
    exit 1
fi

# Common variables for iOS and Android:

echo "Setting Common Env-Variables..."
export MODULE="testCompleteSuite"
echo "Test Module: ${MODULE}"
export TEST="CompleteSuite"
echo "Test File: ${TEST}"
export TEST_TYPE="smoke"
echo "Test Type: ${TEST_TYPE}"

if [ "$platformName" == "ios" ]; then

    echo "\n*** IMPORTANT ***  Make Sure that the App is already installed in the Simulator. \n"

    # iOS:
    echo "Platform Name: ${platformName}"

    # Bundle ID of the App
    export bundleID="com.cliqz.ios.newCliqz"
    echo "Bundle ID: ${bundleID}"
    
    # UDID of the device or simulator
    export udid=""
    if [ "${udid}" == "" ]; then
        export udid=$(xcrun simctl list | grep -m1 "Booted" | tr -s ' ' | cut -d ' ' -f 4 | sed 's/[()]//g')
    fi
    echo "Device UDID: ${udid}"

    # iPhone 6, iPhone X, etc.
    export deviceName=""
    if [ "${deviceName}" == "" ]; then
        export deviceName=$(xcrun simctl list | grep -m1 "Booted" | tr -s ' ' | cut -d ' ' -f 2 -f 3)
    fi
    echo "Device Name: ${deviceName}"

    # 10.3, 11.0, 10.3.1, etc.
    export platformVersion="11.0"
    echo "Platform Version: ${platformVersion}"

    if [ "${deviceName}" == "" ]; then
        echo "\n\n\nDevice Name is not Set And/OR No device is booted !! \nPlease set it in scripts/envs.sh\n\n"
        exit 1
    fi
    if [ "${udid}" == "" ]; then
        echo "\n\n\nUDID is not Set And/OR No device is booted !! \nPlease set it in scripts/envs.sh\n\n"
        exit 1
    fi
fi


if [ "$platformName" == "android" ]; then

    # Android:
    echo "Platform Name: ${platformName}"

    # Full path of the apk.
    export app="$PWD/referenceApp/referenceApp.apk"
    echo "APK Path: ${app}"

    # com.cliqz.browser, etc.
    export appPackage="com.ghostery.android.ghostery"
    echo "App Package: ${appPackage}"

    # com.cliqz.browser.main.MainActivity, etc
    export appActivity="org.mozilla.gecko.LauncherActivity"
    echo "App Activity: ${appActivity}"

    # Nexus 5, Samsung Galaxy S6, etc
    export deviceName="Booted Device"
    echo "Device Name: ${deviceName}"

fi