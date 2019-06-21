#!/usr/bin/env python3
########################################################################
# Filename    : Relay.py
# Description : Button control Relay and Motor
# Author      : freenove
# modification: 2018/09/27
########################################################################
import RPi.GPIO as GPIO
import time
import settings

relayPin = 12    # define the relayPin

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(relayPin, GPIO.OUT)   # Set relayPin's mode is output
    
def irrigate():
    relayState = False
    while True:
        lastChangeTime = round(time.time())
        while True:    
            if ((round(time.time()) - lastChangeTime) > settings.secondsneeded):
                        if relayState:
                            print("Relay On ...")
                            relayState = GPIO.LOW
                            lastChangeTime = round(time.time())
                            left = settings.secondsneeded - (round(time.time()) - lastChangeTime)
                            print(left, 'seconds left')
            GPIO.output(relayPin,relayState)