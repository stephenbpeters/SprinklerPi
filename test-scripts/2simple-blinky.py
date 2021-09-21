# simple LED blink from:
# blinks a single LED on and off.
# https://www.instructables.com/Raspberry-Pi-LED-Blink/
# this script modified to sequentially blink the LED's 
# on the rPi sprinkler project
# including toggling the valve open and closed

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

x = 0

while x == 0:
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
  time.sleep(2)
  GPIO.output(17,GPIO.LOW)
#  print "relay off"
#  GPIO.output(17,GPIO.HIGH)
#  time.sleep(1)




