#!/usr/bin/env bash

########################################################################################################################
# This script uploads the App file to the Cloud, zips the Test Scripts and then Initiates the Server side Testing
########################################################################################################################

echo "Initiating the TestDroid Appium Serverside Testing....."


########################################################################################################################
# Variables to be used in this script
########################################################################################################################
OS=$1       # IOS or Android
BUILD=$2    # Local Build Location
OUT_ZIP="tests.zip"
PROJ_ID="${PROJECT_ID}"
API_LINK="https://cloud.bitbar.com/api/v2/me/projects"
API_KEY="${API_KEY}"
DVG_ID="${DVG_ID}"   # Test Droid Device Group ID

# Create/Sign the Build (APK/IPA) (Wont be required if to be run from Jenkins.
BUILD_A="latest.apk"
BUILD_I="latest.ipa"


########################################################################################################################
# Zip the test cases dependent on iOS or Android
########################################################################################################################
if [ $OS = "ios" ]
then
    BUILD=$BUILD_I
    cp run-tests-i.sh run-tests.sh
    if [ -f "${OUT_ZIP}" ]; then
        rm -f "${OUT_ZIP}"
    fi
    zip -rq "${OUT_ZIP}" run-tests.sh common gecko pages performanceSuites testSuites utils requirements.txt testRunner.py
    rm -f run-tests.sh
else
    BUILD=$BUILD_A
    cp run-tests-a.sh run-tests.sh
    if [ -f "${OUT_ZIP}" ]; then
        rm -f "${OUT_ZIP}"
    fi
    zip -rq "${OUT_ZIP}" run-tests.sh common gecko pages performanceSuites testSuites utils requirements.txt testRunner.py
    rm -f run-tests.sh
fi


########################################################################################################################
# Upload Build and Tests Zip
########################################################################################################################
#echo "Creating new Project..."
#PROJ_ID="$(curl -s -H "Accept: application/json" -u ${API_KEY}: -X POST "${API_LINK}?name=testProject&type=APPIUM_ANDROID_SERVER_SIDE&appCrawlerRun=false" | python -m json.tool | sed -n -e '/"id":/ s/^.* \(.*\),.*/\1/p')"
echo "Uploading App......"
BUILD_ID="$(curl -H "Accept: application/json" -u ${API_KEY}: -X POST -F "file=@${BUILD}" "${API_LINK}/${PROJ_ID}/files/application" | python -m json.tool | sed -n -e '/"id":/ s/^.* \(.*\),.*/\1/p')"
echo " Uploading Test Scripts....."
TEST_ID="$(curl -H "Accept: application/json" -u ${API_KEY}: -X POST -F "file=@${OUT_ZIP}" "${API_LINK}/${PROJ_ID}/files/test")"
rm "${OUT_ZIP}"
echo "Launching tests in Testdroid!"
TESTRUN_ID="$(curl -s -H "Accept: application/json" -u ${API_KEY}: -X POST "${API_LINK}/${PROJ_ID}/runs?usedDeviceGroupId=${DVG_ID}" | python -m json.tool | sed -n -e '/"id":/ s/^.* \(.*\),.*/\1/p')"
TEST_RUN_LINK="${API_LINK}/${PROJ_ID}/${TESTRUN_ID}"
if [ -z ${TESTRUN_ID} ] ; then
    echo "TESTRUN_ID not received, the test probably wasn't launched properly.. Quitting."
    exit
else
    #curl -s -H "Accept: application/json" -u ${API_KEY}: "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}"
    echo "Testrun ID: ${TESTRUN_ID}"
    DATE="$(date +"%D")"
    TIME="$(date +"%T")"
    TEST_NAME="${DATE}+${TIME}"
    A="$(curl -s -H "Accept: application/json" -u ${API_KEY}: -X POST "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}?displayName=${TEST_NAME}")"
    echo "WAITING: "
    TEST_STATE="WAITING\c"
    WAITING=".."
    while [ ${TEST_STATE} != "\"FINISHED\"" ] ; do
        TEST_STATE="$(curl -s -H "Accept: application/json" -u ${API_KEY}: "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}" | python -m json.tool | sed -n -e '/"state":/ s/^.* \(.*\),.*/\1/p')"
        echo ".\c"
        sleep 10
    done
    echo "${TEST_STATE}"
    echo ""
    echo "Test Run Link:  ${TEST_RUN_LINK}"
    echo ""
    TEST_SUCCESS_RATIO="$(curl -s -H "Accept: application/json" -u ${API_KEY}: "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}" | python -m json.tool | sed -n -e '/"successRatio":/ s/^.* \(.*\),.*/\1/p')"
    echo "Success % :  ${TEST_SUCCESS_RATIO}"
    echo ""
fi

########################################################################################################################
# Generate Reports
########################################################################################################################
mkdir reports
cd reports
echo $(curl -s -H "Accept: application/json" -u ${API_KEY}: -X GET "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}/device-runs" | python -m json.tool | sed -n -e '/"deviceRunId":/ s/^.* \(.*\),.*/\1/p') > device-runs.txt
########################################################################################################################
# Download XML reports
########################################################################################################################
mkdir xml
echo "Downloading JUnit XML Files"
IFS=" " read -r -a ids <<< "$(cat device-runs.txt)"
for i in ${ids[@]}; do
    curl -s -H "Accept: application/json" -u ${API_KEY}: -X GET "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}/device-runs/${i}/junit.xml" > xml/$i.xml
done
########################################################################################################################
# Download Screenshots
########################################################################################################################
mkdir screenshots
for i in ${ids[@]}; do
    DEVICE_NAME="$(curl -s -H "Accept: application/json" -u ${API_KEY}: -X POST "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}/device-runs/${i}/" | python -m json.tool | sed -n -e '/"imagePrefix":/ s/^.* \(.*\),.*/\1/p')"
    mkdir -p screenshots/$DEVICE_NAME
    echo $(curl -s -H "Accept: application/json" -u ${API_KEY}: -X GET "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}/device-runs/${i}/screenshots" | python -m json.tool | sed -n -e '/"id":/ s/^.* \(.*\),.*/\1/p') > screenshots/$DEVICE_NAME/screenshots.txt
    IFS=" " read -r -a scids <<< "$(cat screenshots/${DEVICE_NAME}/screenshots.txt)"
    for j in ${scids[@]}; do
        curl -s -H "Accept: application/json" -u ${API_KEY}: -X GET "${API_LINK}/${PROJ_ID}/runs/${TESTRUN_ID}/device-runs/${i}/screenshots/${j}" > screenshots/$DEVICE_NAME/$j.png
    done
done
echo $(echo "${TEST_SUCCESS_RATIO//.}" | cut -c1-3) > success_ratio.txt
