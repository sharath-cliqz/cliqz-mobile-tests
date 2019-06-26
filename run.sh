#!/bin/bash

echo ""
echo ""
echo "*** MAKE SURE all the required browsers are installed in the Device ***"
echo ""
echo ""
echo "*** Starting Appium ***"
echo ""
source venv3.7/bin/activate
#rm -rf *.txt
#appium &
#appium_pid=$!
#sleep 5

echo ""
echo "*** Starting Web Performance Test !! ***"
echo ""
# Declaration of an Array of Browser Bundle IDs to run the Benchmark against.
declare -a configs=("lumen.config" "lumen1.config")
mkdir reports
# Loop through the BundleIds and run the tests again.
for id in "${configs[@]}"
do
    export CONFIG_FILE="$id"
    echo ""
    echo "Performing Benchmarks with config:  $CONFIG_FILE"
    echo ""
    python3 webperformance.py
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo "********        RUN COMPLETE        ********"
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    sleep 60
done

echo ""
echo "*** Tests Complete !! ***"
echo ""
echo ""
echo "*** Killing Appium ***"
echo ""
#sleep 5
#kill $appium_pid

echo ""
echo "*** Results ***"
echo ""
deactivate
pip install xlwt
python src/parse.py
#cat reports/performance.txt
echo ""
echo "*** Done ***"
echo ""