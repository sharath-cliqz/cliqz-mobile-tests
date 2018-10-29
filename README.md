# Cliqz Mobile Tests
Shared mobile automation using the Appium Framework.


## Running Appium Tests:

### 1. Clone the Repository

### 2. Install Dependencies:
    sh scripts/setup.sh

### 3. Run Tests:
    sh runTests

#### Arguments:
* <code>testCaseNames</code> :: Pass the test method names (separated by white spaces) if you want to run only specific test cases.

#### Example:
    sh runTests test01_001_Onboarding
(Will run only the test01_001_Onboarding Test Method)


#### NOTE:
* IMPORTANT: Please set the ANDROID_HOME and JAVA_HOME as environment variables to allow Appium to work properly.
* Do Not Forget to set the required environment variables in <code>scripts/envs.sh</code>.
* You Can find the list of test methods in <code>testSuites/Test Cases.txt</code> file.


### 4. Debugging the Test Results:
* <code>devicelog.log</code> :: Contains the full log of the Device during the Test Run.
* <code>scriptlog.log</code> :: Contains the Full log of the Script Run during the Test Run.
* <code>appium.log</code> :: Contains the full log of the Appium Server during the Test Run.
* <code>test-reports (folder)</code> :: Contains the Report file in XML format.
* <code>screenshots (folder)</code> :: Contains the screenshots of the Test Run (Mostly of Failed Test Cases).