#!/bin/bash
# rotate our log files

rm /home/pi/sprinkler/output/cron-2month.log
cp /home/pi/sprinkler/output/cron-1month.log /home/pi/sprinkler/output/cron-2month.log
cp /home/pi/sprinkler/output/cron.log /home/pi/sprinkler/output/cron-1month.log 
rm /home/pi/sprinkler/output/cron.log
cp /home/pi/sprinkler/output/log.txt /home/pi/sprinkler/output/log-lastmonth.txt
rm /home/pi/sprinkler/output/log.txt
