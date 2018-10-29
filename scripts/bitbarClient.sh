#!/usr/bin/env bash
set -e
set -x

########################################################################################################################
# This script uploads the App file to the Cloud, zips the Test Scripts and then Initiates the Server side Testing
########################################################################################################################

echo "Initiating the TestDroid Appium ClientSide Testing....."


########################################################################################################################
# Variables to be used in this script also set to Environment Variables
########################################################################################################################
export TEST_LOCATION="BitBar"
export TESTDROID_APIKEY="${API_KEY}"
export TESTDROID_PROJECT="TestAndroid"
export TESTDROID_TESTRUN="$(date +'%d-%m-%Y--%R')"
#export TESTDROID_APP="application.apk"
export TESTDROID_APP_PACKAGE="com.cliqz.browser.debug"
export TESTDROID_MAIN_ACTIVITY="com.cliqz.browser.main.MainActivity"
export API_LINK="https://cloud.testdroid.com/api/v2/me/projects"
export PROJ_ID="${PROJECT_ID}"
export TESTDROID_PLATFORM="android"
export TESTDROID_DEVICE_GROUP="${DVG_ID}"
rm -rf latest.apk
wget "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/latest.apk"
########################################################################################################################
# Upload Build
########################################################################################################################
#A="$(curl -s -H "Accept: application/json" -u ${TESTDROID_APIKEY}: -X POST -F "file=@${APK}" "${API_LINK}/${PROJ_ID}/files/application")"
export TESTDROID_APP=$(python common/upload.py -k ${TESTDROID_APIKEY} -a latest.apk)

########################################################################################################################
# Run Tests
########################################################################################################################
python testRunner.py