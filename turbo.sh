#!/bin/bash
for number in {1..1000}
do
	java -jar /home/adrian/.BurpSuite/bapps/9abaa233088242e8be252cd4ff534988/build/libs/turbo-intruder-all.jar ./script.py request.txt http://13.40.10.158  foo
	sleep 10 
done

