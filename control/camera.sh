#!/bin/bash

# grab an image from the USB camera
fswebcam -r 1280x720 /home/pi/sprinkler/output/camera.jpg

#rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress /home/pi/sprinkler/output/camera.jpg bot9@r2d2.tikimojo.com:/home/bot9/r2d2.tikimojo.com/vinhus/fromvinhus/camera.jpg

curl -F 'fileToUpload=@/home/pi/sprinkler/output/camera.jpg' http://r2d2.tikimojo.com/sprinkler/upload2.php


