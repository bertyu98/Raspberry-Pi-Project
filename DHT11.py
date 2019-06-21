#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description : read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
import cimis
import settings

DHTPin = 11     #define the pin of DHT11
GPIO.setwarnings(False)

def check(){
	dht = DHT.DHT(DHTPin)   #create a DHT class object
	sumCnt=0
	sumCnt += 1
	chk = dht.readDHT11() 
	print ("The sumCnt is : %d, \t chk    : %d"%(sumCnt,chk))
	if chk is dht.DHTLIB_OK:      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        print("DHT11,OK!")
}


def update():
    
    totalHumidity =0.0
    totalTemperature=0.0
    i =1
    #while(True):
    
    cimis.function1()
	check()
	#if humidity and temperature is less than or equal to zero then go back to function check()
	if dht.humidity <=0 && dht.temperature<=0:
		check()
	else:
		print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
    settings.dht_temp.append(dht.temperature)
    settings.dht_humidity.append(dht.humidity)
    #time.sleep(60)     
    if(i<60):
        totalHumidity  = totalHumidity+  dht.humidity 
        totalTemperature =totalTemperature + dht.temperature
        i =i+1
    elif(i==60):
        totalHumidity  = totalHumidity+  dht.humidity 
        totalTemperature =totalTemperature + dht.temperature
        print("Average Humidity:%.2f and Average Temperature:%.2f \n"%(totalHumidity/60.0,totalTemperature/60.0)) 
        i =0
        totalHumidity = 0
        totalTemperature = 0
    else:
        print("Error")
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        update()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  

