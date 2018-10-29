#!/bin/bash

# Default ENVs for running Performance Tests.
echo "Setting Environment Variables...."
export MODULE="test99Benchmarks"
export TEST="Benchmarks"
export platformName="ios"
export TEST_TYPE="performance"

# Device Details. Please change according to the Device.
echo "Setting Device Details..."
export deviceName="iPhone 6s"
export platformVersion="11.0.3"
export udid="fbfa440d49106615c8a6f0f61d93fedbc947f314"

echo ""
echo ""
echo "*** MAKE SURE all the required browsers are installed in the Device ***"
echo ""
echo ""

# Declaration of an Array of Browser Bundle IDs to run the Benchmark against.
declare -a bundleIDs=("org.mozilla.ios.Firefox" "com.apple.mobilesafari" "com.google.chrome.ios" "com.cliqz.ios.newCliqz")
# declare -a bundleIDs=("com.cliqz.ios.newCliqz")

# Loop through the BundleIds and run the tests again.
for id in "${bundleIDs[@]}"
do
    echo ""
    echo "Performing Benchmarks for:  $id"
    echo ""
    export bundleID="$id"
    export reportFile="testreport-$id.log"
    python testRunner.py
done