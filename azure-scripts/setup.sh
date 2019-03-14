echo "*** Azure Script - Setup Test Environment ***"
platform=$1
echo "*** Install Appium and WD ***"
npm install --global appium@beta wd npm
echo "*** DONE ***"
echo "*** Install and Setup Virtualenv ***"
echo "Versions Pre-install:"
python -V && python3 -V && pip -V
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
echo "Versions Post-install:"
python -V && pip -V
pip install -r requirements.txt
mkdir screenshots
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