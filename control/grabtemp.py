#!/usr/bin/python
# script for use in cron for grabbing temp and humidity from
# our sensor from adafruit: https://www.adafruit.com/product/393
# 
# following instructions from:
# https://thepihut.com/blogs/raspberry-pi-tutorials/am2302-temp-humidity-sensor
# using the Adafruit code from here:
# https://github.com/adafruit/Adafruit_Python_DHT
# Stephen Peters sbp@tikimojo.com
# started 5/9/2021

import sys
import Adafruit_DHT
import time
from datetime import datetime

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# seems like sensor should = 2302 but the logic above selects 22
sensor = 22
pin = 23
#print (' sensor = '+ str(sensor))
#print(" pin = " + str(pin))

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
temperature = temperature * 9/5.0 + 32
run_time = str(datetime.now().time())

if humidity is not None and temperature is not None:
    #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    cmd_file = open('/home/pi/sprinkler/output/conditions.txt', 'w')
    cmd_file.write('current conditions at ' + str(run_time) + ' are ')
    cmd_file.write('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    cmd_file.close()
else:
    print('Failed to get a reading from the sensor, try again!')
    sys.exit(1)

