#!/bin/bash
# Quick bash script to spam a Splunk HEC endpoint to test for availability.
# This was used to troubleshoot HEC availability issue.

# Variable assignment
log=output.txt	# Output file
count=10000 	# Run script $count times
url="https://"	# Enpoint
authHeader=""	# Auth headers
authHeader2=""
mssg=""			# Log message

# Clear current log file
echo > $log

# Loop curl request
for i in  $(seq 1 $count)
do
   echo -n "Attempt $i | " >> $log
   curl $url -H $authHeader -H $authHeader2 -d $mssg -k >> $log
   echo "" >> $log
   sleep 1
done
