#!/bin/bash

##
## Work in progress! The dependency installations need to be done to the
## container so that we don't need to install them here.
##
export JAVA_HOME=$(/usr/libexec/java_home)

# Name of the test file
TEST=${TEST:="testRunner.py"}

#Test Location/Type
export TEST_LOCATION="BitBarServer"

##### Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip tests.zip

echo "Installing pip for python"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py

echo "Installing Appium Python Client 0.24 and xmlrunner 1.7.7"
chmod 0755 requirements.txt
sudo pip install -r requirements.txt
tar zxvf selenium-3.3.1.tar.gz
cd selenium-3.3.1
sudo python setup.py install
pip show selenium
cd ..

echo "Setting UDID..."
echo $UDID
UDID="${echo $UDID}"
echo "UDID set to ${UDID}"

echo "Starting Appium ..."
appium-1.6 -U ${UDID}  --log-no-colors --log-timestamp --show-ios-log --command-timeout 120

ps -ef|grep appium
##### Cloud testrun dependencies end.
#theapp=find . -iname *.apk

export TESTDROID_APP=$PWD/application.ipa #App is at current working folder

## Desired capabilities:

export TESTDROID_URL="http://localhost:4723/wd/hub" # Local & Cloud
export TESTDROID_DEVICE="Local Device"
export TESTDROID_PLATFORM="IOS"
export TESTDROID_AUTOMATION="XCUITest"
export TESTDROID_BUNDLE_ID="cliqz.ios.CliqzBeta"
#PACK="${cliqz.ios.CliqzBeta}"


#Resetting App Data
#ideviceinstaller --udid ${UDID} -- uninstall ${PACK}

## Run the test:
echo "Running test ${TEST}"
rm -rf screenshots

python ${TEST}

mv test-reports/*.xml TEST-all.xml