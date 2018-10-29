#!/usr/bin/env bash -l
set -x
set -e

## Install Pre-Requisites
chmod 0755 requirements.txt
echo "Installing requirements for the Tests....."
pip install -r requirements.txt
echo "Installing Appium..."
npm install -g appium
echo "Installing WebDriver..."
npm install -g wd