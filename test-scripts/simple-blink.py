# simple LED blink from:
# blinks a single LED on and off.
# https://www.instructables.com/Raspberry-Pi-LED-Blink/

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

x = 0

while x == 0:
  print "LED on"
  GPIO.output(17,GPIO.HIGH)
  time.sleep(1)
  print "LED off"
  GPIO.output(17,GPIO.LOW)
  time.sleep(1)



