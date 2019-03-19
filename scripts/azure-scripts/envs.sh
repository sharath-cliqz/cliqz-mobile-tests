echo "*** Azure Script - Exporting Environment Variables ***"
platform=$1
brand=$2
export platformName=$1
echo "platformName=${platformName}"
if [ $platform == 'android' ]; then
	if [ $brand == 'cliqz' ]; then
		echo "*** Exporting Cliqz Envs ***"
		export app="$(cat referenceApp/referenceApp_cliqz.link)"
		echo "app=${app}"
		export appPackage='com.cliqz.browser'
		echo "appPackage=${appPackage}"
	elif [ $brand == 'ghostery' ]; then
		echo "*** Exporting Ghostery Envs ***"
		export app="$(cat referenceApp/referenceApp_ghostery.link)"
		echo "app=${app}"
		export appPackage='com.ghostery.android.ghostery'
		echo "appPackage=${appPackage}"
	else
		echo "ERROR"
		exit 1
	fi
	echo "*** Exporting Device Envs ***"
	export deviceName="${DEV_NAME}"
	echo "deviceName=${deviceName}"
	export appActivity="org.mozilla.gecko.LauncherActivity"
	echo "appActivity=${appActivity}"
	export deviceType="$(adb shell getprop ro.build.characteristics)"
	echo "deviceType=${deviceType}"
	export realDeviceName="$(adb shell getprop ro.product.model)"
	echo "realDeviceName=${realDeviceName}"
	export deviceOSVer="$(adb shell getprop ro.build.version.release)"
	echo "deviceOSVer=${deviceOSVer}"
elif [ $platform == 'ios' ]; then
	export deviceName="${DEV_NAME}"
	echo "deviceName=${deviceName}"
	export platformVersion="12.1"
	echo "platformVersion=${platformVersion}"
	export udid="${DEV_UDID}"
	echo "udid=${udid}"
	export bundleID="com.cliqz.ios.newCliqz"
	echo "bundleID=${bundleID}"
else
	echo "ERROR"
	exit 1
fi
echo "*** Exporting Test Envs ***"
export MODULE="testCompleteSuite"
echo "MODULE=${MODULE}"
export TEST="CompleteSuite"
echo "TEST=${TEST}"
export TEST_TYPE="smoke"
echo "TEST_TYPE=${TEST_TYPE}"
echo "*** DONE ***"
