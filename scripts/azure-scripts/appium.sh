echo "*** Azure Script - Appium ***"
appium &
echo $! >> appium.pid
sleep 15
echo "*** DONE ***"