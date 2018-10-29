#!/bin/env groovy

node('us-east-1 && ubuntu && docker && !gpu') {
    stage('Checkout'){
        checkout([
         $class: 'GitSCM',
         branches: scm.branches,
         extensions: scm.extensions + [$class: 'CleanBeforeCheckout'],
         userRemoteConfigs: scm.userRemoteConfigs
        ])
    }
    def cliqzApk = "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/cliqz/latest_x86.apk"
    def ghosteryApk = "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/ghostery/latest_x86.apk"
    def instance_id = sh(returnStdout: true, script: '''
            aws ec2 run-instances --image-id ami-07457b491395bb595 --count 1 --instance-type t2.medium --key-name android_ci_genymotion --security-group-ids sg-5bbf173f --subnet-id subnet-341ff61f  --region=us-east-1 --query "Instances[].InstanceId" --output text
        ''').trim()
    def ip = sh(returnStdout: true, script: """
            aws ec2 describe-instances --instance-ids $instance_id  --region=us-east-1 --query 'Reservations[].Instances[].PrivateIpAddress' --output text
        """).trim()
    sh "aws ec2 create-tags --resources $instance_id --region=us-east-1 --tag Key=Name,Value='Appium-Genymotion'"
    try{
        def dockerTag = sh(returnStdout: true, script: """curl https://raw.githubusercontent.com/cliqz-oss/cliqz-android/master/mozilla-release/browser/config/version_display.txt""").trim()
        def baseImageName = "browser-f/android:${dockerTag}"
        timeout(10){
            withEnv(["INSTANCE_ID=${instance_id}"]){
                stage('Genymotion Status'){
                    def status = sh(returnStdout: true, script: """
                            aws ec2 describe-instance-status --region=us-east-1 --instance-id $INSTANCE_ID --query 'InstanceStatuses[].InstanceStatus[].Details[].Status' --output text
                        """).trim()
                    while (status != 'passed') {
                        println "Waiting for the instance to fully Boot up...."
                        sleep(15)
                        status = sh(returnStdout: true, script: """
                            aws ec2 describe-instance-status --region=us-east-1 --instance-id $INSTANCE_ID --query 'InstanceStatuses[].InstanceStatus[].Details[].Status' --output text
                        """).trim()
                        println "Instance Status: ${status}"
                    }
                }
            }
        }
        def args = "-v ${pwd}/artifacts:/artifacts:rw"
        docker.image("141047255820.dkr.ecr.us-east-1.amazonaws.com/${baseImageName}").inside(args) {
            try{
                withEnv([
                        "IP=${ip}",
                        "CLIQZ_APK=${cliqzApk}",
                        "GHOSTERY_APK=${ghosteryApk}",
                        "CLIQZ_PACKAGE=com.cliqz.browser",
                        "GHOSTERY_PACKAGE=com.ghostery.android.ghostery",
                        "platformName=android",
                        "deviceName=127.0.0.1:5556",
                        "appActivity=org.mozilla.gecko.LauncherActivity",
                        "MODULE=testCompleteSuite",
                        "TEST=CompleteSuite",
                        "TEST_TYPE=smoke"
                    ]){
                    withCredentials([file(credentialsId: 'f4141ff9-4dc0-4250-84b5-ef212d4fbb42', variable: 'FILE' )]){
                        stage('Install Dependencies') {
                            timeout(10) {
                                sh'''#!/bin/bash -l
                                    set -x
                                    set -e
                                    chmod 400 $FILE
                                    export "PATH=${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/platform-tools/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${PATH}"
                                    ssh -v -o StrictHostKeyChecking=no -i $FILE shell@$IP "setprop persist.sys.usb.config adb"
                                    ssh -v -o StrictHostKeyChecking=no -i $FILE -NL 5556:127.0.0.1:5555 shell@$IP &
                                    adb connect 127.0.0.1:5556
                                    adb wait-for-device
                                    chmod 0755 requirements.txt
                                    virtualenv ~/venv
                                    source ~/venv/bin/activate
                                    pip install -r requirements.txt
                               '''
                           }
                        }
                        /*stage('Run Tests: CLIQZ') {
                            timeout(15) {
                                sh'''#!/bin/bash -l
                                    set -x
                                    set -e
                                    appium --log Cliqz-appium.log &
                                    echo $! > appium.pid
                                    source ~/venv/bin/activate
                                    sleep 15
                                    cat appium.pid
                                    export "PATH=${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/platform-tools/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${PATH}"
                                    export deviceType="$(adb shell getprop ro.build.characteristics)"
                                    export deviceType="$(adb shell getprop ro.build.characteristics)"
                                    export realDeviceName="$(adb shell getprop ro.product.model)"
                                    export deviceOSVer="$(adb shell getprop ro.build.version.release)"
                                    adb forward tcp:6000 localfilesystem:/data/data/$CLIQZ_PACKAGE/firefox-debugger-socket
                                    adb forward --list
                                    export app="${CLIQZ_APK}"
                                    export appPackage="${CLIQZ_PACKAGE}"
                                    python testRunner.py || true
                                    adb uninstall ${appPackage}
                                    adb forward --remove-all
                                    kill `cat appium.pid` || true
                                    rm -f appium.pid
                               '''
                           }
                        }*/
                        stage('Run Tests: GHOSTERY') {
                            timeout(15) {
                                sh'''#!/bin/bash -l
                                    set -x
                                    set -e
                                    appium --log Ghostery-appium.log &
                                    echo $! > appium.pid
                                    source ~/venv/bin/activate
                                    sleep 15
                                    cat appium.pid
                                    export "PATH=${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/platform-tools/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${PATH}"
                                    export deviceType="$(adb shell getprop ro.build.characteristics)"
                                    export deviceType="$(adb shell getprop ro.build.characteristics)"
                                    export realDeviceName="$(adb shell getprop ro.product.model)"
                                    export deviceOSVer="$(adb shell getprop ro.build.version.release)"
                                    adb forward tcp:6000 localfilesystem:/data/data/$GHOSTERY_PACKAGE/firefox-debugger-socket
                                    adb forward --list
                                    export app="${GHOSTERY_APK}"
                                    export appPackage="${GHOSTERY_PACKAGE}"
                                    python testRunner.py || true
                                    adb uninstall ${appPackage}
                                    adb forward --remove-all
                                    kill `cat appium.pid` || true
                                    rm -f appium.pid
                               '''
                           }
                        }
                    }
                }
            }
            catch (e){
                print e
            }
            finally{
                stage('Upload Results and Clean Up') {
                    junit "test-reports/*.xml"
                    archiveArtifacts allowEmptyArchive: true, artifacts: '*.log'
                    try {
                        zip archive: true, dir: 'screenshots', glob: '', zipFile: 'screenshots.zip'
                        zip archive: true, dir: 'test-reports', glob: '', zipFile: 'reports.zip'
                    }
                    catch (e){
                        print e
                    }
                    sh'''#!/bin/bash -l
                        rm -rf screenshots
                        rm -rf test-reports
                        rm -rf *.log
                        rm -f screenshots.zip || true
                        rm -f reports.zip || true
                    '''
                }
            }
        }
    }
    finally{
        sh """#!/bin/bash -l
            set -x
            set -e
            aws ec2 terminate-instances --instance-ids ${instance_id} --region=us-east-1
        """
    }
}
