echo "*** Azure Script - Launch Emulator (Also Install App for iOS) ***"
platform=$1
if [ $platform == 'ios' ]; then
	export DEV_NAME="Test-iPhone6s"
	export DEV_UDID=$(xcrun simctl create ${DEV_NAME} com.apple.CoreSimulator.SimDeviceType.iPhone-6s com.apple.CoreSimulator.SimRuntime.iOS-11-4)
	echo "DEV_NAME=${DEV_NAME}"
	echo "DEV_UDID=${DEV_UDID}"
	xcrun simctl boot $DEV_UDID
	sleep 10
	sudo mkdir -p $HOME/Library/Developer/CoreSimulator/Devices/$DEV_UDID/data/Containers/Bundle/Application/
	unzip -d $HOME/Library/Developer/CoreSimulator/Devices/$DEV_UDID/data/Containers/Bundle/Application/ referenceApp/referenceApp_ios.zip
	xcrun simctl shutdown $DEV_UDID
	sleep 5
	xcrun simctl boot $DEV_UDID
	sleep 15
elif [ $platform == 'android' ]; then
	export DEV_NAME="Nexus5Emu"
	echo "DEV_NAME=${DEV_NAME}"
	$ANDROID_HOME/tools/bin/avdmanager create avd --device "Nexus 5" --package "${IMG_NAME}" --abi google_apis/x86 --name "${DEV_NAME}"
	$ANDROID_HOME/emulator/emulator -avd $DEV_NAME &
	echo $! >> emu.pid
	echo "Started Emu"
	emuStatus="$(adb shell getprop sys.boot_completed)"
	while [ $emuStatus != "1" ]; do
		echo $emuStatus
		emuStatus="$(adb shell getprop sys.boot_completed)"
	done
else
	echo "ERROR"
	exit 1
fi