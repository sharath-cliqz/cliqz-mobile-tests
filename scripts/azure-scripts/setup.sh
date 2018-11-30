echo "*** Azure Script - Setup Test Environment ***"
platform=$1
echo "*** Install Appium and WD ***"
npm install -g appium@1.10.0 wd@1.11.1
echo "*** DONE ***"
echo "*** Install and Setup Virtualenv ***"
echo "Versions Pre-install:"
python -V && pip -V
pip install virtualenv
virtualenv -p python venv
source venv/bin/activate
echo "Versions Post-install:"
python -V && pip -V
pip install -r requirements.txt
echo "*** DONE ***"
echo "*** Install Platform Specific Requirements ***"
if [ $platform == 'ios' ]; then
	echo "Nothing else to setup"
elif [ $platform == 'android' ]; then
	export IMG_NAME='system-images;android-23;google_apis;x86'
	echo "*** Installing System Image using SDKManager ***"
	$ANDROID_HOME/tools/bin/sdkmanager "${IMG_NAME}"
else
	echo "ERROR"
	exit 1
fi
echo "*** DONE ***"
