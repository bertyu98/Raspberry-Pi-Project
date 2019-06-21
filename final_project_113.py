import RPi.GPIO as GPIO
import time
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep


sensorPin = 7    # define the sensorPin
relayPin = 12    # define the relayPin

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(sensorPin, GPIO.IN)    # Set sensorPin's mode is input
    GPIO.setup(relayPin, GPIO.OUT)   # Set relayPin's mode is output
    GPIO.setwarnings(False)
    
def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    relayState = True
    while True:
        #lastChangeTime = round(time.time())
        #GPIO.output(relayPin,relayState)
        while True:
            GPIO.output(relayPin,relayState)
            lastChangeTime = round(time.time())
            lcd.clear()
            if GPIO.input(sensorPin)==GPIO.HIGH:
                lcd.setCursor(0,0)  # set cursor position
                lcd.message("Irrigation off") #turn off irrigation
                relayState = False
                GPIO.output(relayPin,relayState)

                #lastChangeTime = round(time.time())
                break
                    #time.sleep(10)
                        #lastChangeTime = round(time.time())
                #break
                    #If its been a minute or until the senser is not detected, then turn on the sprinkler
                    #60-time.time()%60 or 
            elif((60-time.time()%60 or GPIO.input(sensorPin)==GPIO.LOW)) :
                lcd.setCursor(0,0)  # set cursor position
                lcd.message("Irrigation on")
                relayState = True
                GPIO.output(relayPin,relayState)
                #lastChangeTime = round(time.time())
                break
            #GPIO.output(relayPin,relayState)
            
                    #lastChangeTime = round(time.time())
                    #break
    
def destroy():
    GPIO.cleanup()                     # Release resource

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    print ('I2C Address Error !')
    exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()