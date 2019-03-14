echo "*** Azure Script - Closing Appium and Emulator/Simulator ***"
platform=$1
echo "*** Copying Logs ***"
mkdir logs
cp -r *.log logs/
echo "*** DONE ***"
echo "*** Stopping Appium ***"
kill $(cat appium.pid)
sleep 5
echo "*** DONE ***"
echo "*** Stopping Emulator/Simulator ***"
if [ $platform == 'ios' ]; then
    xcrun simctl shutdown $DEV_UDID
    xcrun simctl delete $DEV_UDID
elif [ $platform == 'android' ]; then
    adb kill-server
    kill -9 $(cat emu.pid)
else
    echo "ERROR"
    exit 1
fi
echo "*** DONE ***"