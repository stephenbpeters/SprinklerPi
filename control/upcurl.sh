#!/bin/bash
# send our test command file

curl -F 'fileToUpload=@/home/pi/sprinkler/input/cmd.txt' http://r2d2.tikimojo.com/sprinkler/upload.php

