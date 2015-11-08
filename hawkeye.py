#!/usr/bin/env python
#
# Created by Patricio Gonzalez Vivo ( @patriciogv ) on 11/08/2015
#


width = 800
height = 800

import RPi.GPIO as GPIO
import time
import os
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        time_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        print("Shot!! " + time_stamp)
        
        os.system("raspistill -w " + str(width) + " -h " + str(height) + " -o " + time_stamp + ".jpg" )
        time.sleep(0.2)
