echo "*** Azure Script - Parse Report XML ***"
status=$(python -c '''
import os
errorsCount = 0
totalCount = 0
for report in sorted(os.listdir("test-reports")):
	with open("test-reports/"+report) as fp:
		for i, line in enumerate(fp):
			if i==1:
				for valueset in line.split(" "):
					if "errors" in valueset or "failures" in valueset: 
						errorsCount += int(valueset.split("\"")[1])
					elif "tests" in valueset:
						totalCount += int(valueset.split("\"")[1])
if errorsCount == 0 and totalCount > 2:
	print errorCount
elif totalCount == 0:
	print -1
else:
	print errorCount
''')
if [ $status != "0" ]; then
	echo ERROR: Some Tests Failed !
	exit 1
elif [ $status == "-1" ]; then
	echo ERROR: Tests were not run !
	exit 1
else
	echo "All Tests Passed !"
fi
echo "*** DONE ***"