#!/bin/bash

# attempting a bash shell to use rsync to push our file
# to the r2d2.tikimojo.com server

#rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress bot9@r2d2.tikimojo.com:/home/bot9/r2d2.tikimojo.com/vinhus/fromvinhus/conditions.txt /home/pi/sprinkler/output/conditions.txt 

python /home/pi/sprinkler/control/grabtemp.py
rm /home/pi/sprinkler/output/conditions.html
cat /home/pi/sprinkler/output/conditions.head >> /home/pi/sprinkler/output/conditions.html
cat /home/pi/sprinkler/output/conditions.txt >> /home/pi/sprinkler/output/conditions.html
cat /home/pi/sprinkler/output/conditions.tail >> /home/pi/sprinkler/output/conditions.html

# turning off our rysnc commands and using curl instead
#rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress /home/pi/sprinkler/output/conditions.txt bot9@r2d2.tikimojo.com:/home/bot9/r2d2.tikimojo.com/vinhus/fromvinhus/conditions.txt 
#rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress /home/pi/sprinkler/output/conditions.html bot9@r2d2.tikimojo.com:/home/bot9/r2d2.tikimojo.com/vinhus/fromvinhus/conditions.html 

curl -F 'fileToUpload=@/home/pi/sprinkler/output/conditions.html' http://r2d2.tikimojo.com/sprinkler/upload2.php
curl -F 'fileToUpload=@/home/pi/sprinkler/output/conditions.txt' http://r2d2.tikimojo.com/sprinkler/upload2.php
