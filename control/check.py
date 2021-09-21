# script to run in cron to check commands to the sprinkler
import time
from datetime import datetime
import RPi.GPIO as GPIO
import os

# setup our GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

# first, let's check to see if we have any commands 
cmd_file = open('/home/pi/sprinkler/input/cmd.txt', 'r')
commands = cmd_file.readline()
cmd_file.close()
# set our on/off and runtime variables
cmdline = commands.split('/')
cmd = cmdline[0]
runtime = int(cmdline[1]) * 60 # convert minutes to seconds
if runtime < 1200: 
  runtime = 1200

# now check to see if the sprinkler is already running
status_file = open('/home/pi/sprinkler/input/on.txt', 'r')
status = status_file.readline()
status_file.close()
print('------')
print('script running now...')
run_time = str(datetime.now().time())
print('')

if cmd == 'turn off':
  print('--> cmd.txt contains: ' + cmd)
  print('--> leave sprinkler off, do nothing')
  quit()

if cmd == 'turn on' and status =='running':
  print('---> cmd.txt contains: ' + cmd)
  print('---> and on.txt contains: ' + status)
  print('--> sprinkler currently on, do nothing')
  quit()

if cmd == 'turn on' and status == 'off':
  print('---> cmd.txt contains: ' + cmd)
  print('---> and on.txt contains: ' + status)
  print('---> turn on sprinkler')
  # stick in our turn-on code here
  print('...change on.txt to say we are running')
  print('also write to our log file' + run_time)
  log_file = open('/home/pi/sprinkler/output/log.txt', 'a')
  log_file.write('turn on sprinkler at ' + run_time)
  log_file.write('\n')
  log_file.close()
  # count down the time until we turn the sprinkler off
  print('wait while the the sprinkler runs...')
  print "LED 22 ON"
  GPIO.output(22,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(22,GPIO.LOW)
  print "LED 27 ON"
  GPIO.output(27,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(27,GPIO.LOW)
  print "LED 17 ON"
  GPIO.output(17,GPIO.HIGH)
# wait a bit, then turn off
  time.sleep(runtime)
  GPIO.output(17,GPIO.LOW)
  time.sleep(2)
  # now that the sprinkler is on, reset cmd.txt 

  # code to write our files:
  print('time to turn off the sprinkler cmd file, update files')
  status_file = open('/home/pi/sprinkler/input/on.txt', 'w')
  status_file.write('off')
  status_file.close()

  cmd_file = open('/home/pi/sprinkler/input/cmd.txt', 'w')
  cmd_file.write('turn off/0')
  cmd_file.close()
  os.system("/home/pi/sprinkler/control/upcurl.sh")

print('script done')
