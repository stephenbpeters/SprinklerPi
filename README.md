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

### Software

This project requires a number of python and shell scripts on the rPi and HTML + PHP on the web server.  This is all very modular.  If you don't have a camera or temp sensor, you can either leave those scripts off, or simply allow them to fail.  Here's where to put what, where:

#### Raspberry Pi

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
** stuff

#### Web

#### crontab entries


## Contact

If you want to contact me you can reach me at stephen.peters@gmail.com.

## Contributing to SprinklerPi:
I am looking forward to people who'd like to expand / refine this project.  Rather than just accept pull requests, I'd like to discuss the next steps to make this even better!  

## License

This project uses the following license: GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html).
