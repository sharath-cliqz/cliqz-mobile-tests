#!/bin/bash

##
## Work in progress! The dependency installations need to be done to the
## container so that we don't need to install them here.
##


# Name of the test file
TEST=${TEST:="testRunner.py"}

#Test Location/Type
export TEST_LOCATION="BitBar"

##### Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip -o tests.zip

echo "Installing pip for python"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py

echo "Installing Appium Python Client 0.26 and xmlrunner 1.7.7"
chmod 0755 requirements.txt
sudo pip install -r requirements.txt

echo "Starting Appium ..."

appium-1.8 --log-no-colors --log-timestamp

ps -ef|grep appium
##### Cloud testrun dependencies end.

export TESTDROID_APP=$PWD/application.apk #App file is at current working folder

## Desired capabilities:

export TESTDROID_URL="http://localhost:4723/wd/hub" # Local & Cloud
export TESTDROID_DEVICE="Local Device"
export TESTDROID_PLATFORM="android"
export TESTDROID_BUNDLE_ID="com.ghostery.android.ghostery"
export TESTDROID_MAIN_ACTIVITY="org.mozilla.gecko.LauncherActivity"
export platformName="android"

APILEVEL=$(adb shell getprop ro.build.version.sdk)
APILEVEL="${APILEVEL//[$'\t\r\n']}"
echo "API level is: ${APILEVEL}"

## APPIUM_AUTOMATION
if [ "$APILEVEL" -gt "16" ]; then
  echo "Setting APPIUM_AUTOMATION=UiAutomator2"
  export TESTDROID_AUTOMATION="UiAutomator2"
else
  echo "Setting APPIUM_AUTOMATION=selendroid"
  export TESTDROID_AUTOMATION="Selendroid"
fi


# Reset APP:
#adb shell pm clear com.cliqz.browser

# Set Device Details in ENV
export deviceType=$(adb shell getprop ro.build.characteristics)
export realDeviceName=$(adb shell getprop ro.product.model)
export deviceOSVer=$(adb shell getprop ro.build.version.release)

# Set Test Details in ENV
export MODULE="testCompleteSuite"
export TEST="CompleteSuite"
export TEST_TYPE="smoke"


## Run the test:
echo "Running test ${TEST}"
rm -rf screenshots
python testRunner.py
mv test-reports/*.xml TEST-all.xml