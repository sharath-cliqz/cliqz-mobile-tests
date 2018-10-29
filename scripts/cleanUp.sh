#!/bin/bash

echo ""
echo ""
echo "Cleaning Up Workspace...."
echo ""
echo ""

cd ../

echo ""
echo " Cleaning up *.pyc files..."
echo ""
find . -name "*.pyc" -exec rm -f {} \;
echo "Done."

echo ""
echo " Cleaning up *.log files..."
echo ""
rm -rf *.log
echo "Done."

echo ""
echo " Cleaning up Screenshots..."
echo ""
rm -rf screenshots/
echo "Done."

echo ""
echo " Cleaning up XML Reports files..."
echo ""
rm -rf test-reports/
echo "Done."

echo ""
echo ""
echo "Workspace Clean Up:  COMPLETE !!"
echo ""
echo ""