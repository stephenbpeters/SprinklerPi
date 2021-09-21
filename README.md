# SprinklerPi
A home automation project for watering the lawn and/or garden.

Following this project will allow you to turn your home sprinklers on/off from anywhere on the Internet.  Additionally, should you be interested it will also take photos from a USB camera and provide up-to-the minute temperature and humidity readings.  It's designed to be modular, and I expect to be adding more in the future.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a web hosting solution that will run PHP and accept file uploads
* You have a Raspberry Pi with a recent version of Python
* You are ready and able to assemble the hardware that controls the sprinkler valve

## Setup

Setting up a SprinklerPi is non-trivial as it requires building the hardware for the sprinkler valve controller which connects to the rPi.  This is documented extensively at my website: https://tikimojo.com/sprinklerpi/.  This project is built on the work of Ben Finio.  https://www.instructables.com/Raspberry-Pi-Controlled-Irrigation-System/.

The interface for the user to turn on the sprinkler is through the web site forms.  Once you have this set up, direct yourself to http://your-site-here.com/sprinkler

### Software

This project requires a number of python and shell scripts on the rPi and HTML + PHP on the web server.  This is all very modular.  If you don't have a camera or temp sensor, you can either leave those scripts off, or simply allow them to fail.  The scripts expect that you are installing under user "pi" and have three folders: control, input and output.  If you use a different user directory or a different directory structure, you'll need to adjust the scripts appropriately.

#### Raspberry Pi

The shell scripts will need to be set to executable. Sync.sh and upcurl.sh need to be edited to point to your web server address. 

* control
  * check.py --> runs to look for the "turn on" command from the web server, and turn on the sprinkler valve
  * sync.sh --> downloads the command file from the web server
  * upcurl.sh --> uploads the "turn off" command to the web server
  * grabtemp.py --> gets the temperature and humidity readings from the sensor and creates conditions.txt
  * conditions.sh --> runs grabtemp.py and assembles conditions.html
  * camera.sh --> takes a photo from the camera and uploads it to the web server
  * rotate.sh --> rotates our cron.log and check.py log files

* input
  * cmd.txt --> contains the commands from the web server
  * on.txt --> status file, tells the check.py script that the sprinkler is currently on

* output
  * log.txt --> log file written by check.py on it's activity
  * conditions.txt --> written by grabtemp.py
  * conditions.head, .tail --> template files used for building conditions.html
  * camera.jpg --> image from the camera
  * cron.log --> output from our cron jobs
  * cron-1month.log --> the previous month's cron.log
  * cron-2month.log --> ...and the month before that, just in case you need it.

* test-scripts
  * A set of scripts that can be used for debugging the hardware as you're getting things set up

* local
  * This directory is a Python Flask app that provides two simple buttons for toggling two GPIO ports.
  * This is not required to run the project, but you may find it handy.  In fact, if you setup your home network to be reachable from the general internet, you could use these two buttons to turn your sprinkler on and off.  Much of the work in this project is to get around the need for home network configuration.
  * This can be run at the command line with "python app.py"
  * Once the flask app is running, point your web browser at: http://raspberry-pi-ip-address:5000/

#### crontab entries
 
How the SprinklerPi works is it uses cron to run the scripts on a frequent basis to both check for new commands, and push status.  In fact, it's something of ar Rube Goldberg machine (https://en.wikipedia.org/wiki/Rube_Goldberg_machine) in how it functions.  This is intentional as it makes it very modular and easy to add or remove components.  Here are the commands I use in crontab: 
 
```
* * * * * /home/pi/sprinkler/control/sync.sh >> /home/pi/sprinkler/output/cron.log 2>&1
* * * * * /home/pi/sprinkler/control/camera.sh >> /home/pi/sprinkler/output/cron.log 2>&1
* * * * * /home/pi/sprinkler/control/conditions.sh >> /home/pi/sprinkler/input/cron.log 2>&1
* * * * * python /home/pi/sprinkler/control/check.py >> /home/pi/sprinkler/input/cron.log 2>&1
0 0 1 * * /home/pi/sprinkler/control/rotate.sh >> /home/pi/sprinkler/output/cron.log 2>&1
0 * * * * /home/pi/sprinkler/control/upcurl-templog.sh >> /home/pi/sprinkler/output/cron.log 2>&1
0 5 * * * /sbin/shutdown -r now # reboot every day at 5am
```
 
#### Web 

* assets --> contains the css files and future additions
* index.html --> the "home page" for the sprinkler controls
* sprinkler-on.html --> used to turn on the sprinkler 
* * write-out.php --> takes the user input and writes the cmd.txt file
* sprinkler-off.html --> not really needed, but can be used to give the sprinkler-off command
* * write-out-off.php --> writes the off command to cmd.txt
* upload.php --> used by the rPi curl script to upload the cmd.txt file
* upload2.php --> used by the rPi curl script to upload the conditions.html and camera.jpg files
* tosprinklerpi --> directory used for files intended to be picked up by the rPi
* * cmd.txt --> written by sprinkler-on.php with the "turn on" command 
* fromsprinklerpi --> directory for files uploaded from the rPi with curl
* * camera.html --> camera image page
* * camera.jpg --> photo from the USB camera
* * conditions.html --> page constructed by the rPi with temperature and humidity readings


## Contact

If you want to contact me you can reach me at stephen.peters@gmail.com.

## Contributing to SprinklerPi:
I am looking forward to people who'd like to expand / refine this project.  Rather than just accept pull requests, I'd like to discuss the next steps to make this even better!  

## License

This project uses the following license: GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html).
