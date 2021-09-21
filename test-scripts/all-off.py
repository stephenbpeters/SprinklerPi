# turn all three LED's off

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

print "LED 22, 27 and 17 Off"
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(17,GPIO.LOW)

