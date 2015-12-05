#!/usr/bin/env python
#
# Created by Patricio Gonzalez Vivo ( @patriciogv ) on 11/08/2015
#
width = 800
height = 800
freq = 137500

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
        print("Taking picture " + time_stamp)
        os.system("raspistill -vf -hf -w " + str(width) + " -h " + str(height) + " -o " + time_stamp + ".jpg -t 1" )
        print("Applying LUT filter")
        os.system("glslViewer /home/pi/hawkeye/shaders/lut.frag " + time_stamp + ".jpg /home/pi/hawkeye/shaders/lut-0010.png -w " + str(width) + " -h " + str(height) + " -o " + time_stamp + ".png -s 1")
        print("Converting to RGB")
        os.system("convert -depth 8 " + time_stamp + ".png " + time_stamp + ".rgb" )
        print("Conveting to FT ")
        os.system("pisstv "+ time_stamp +".rgb "+ time_stamp +".ft")
        print("Sending in " + str(freq))
        os.system("sudo rpitx -m RF -i " + time_stamp+ ".ft -f " + str(freq))
        time.sleep(1)
