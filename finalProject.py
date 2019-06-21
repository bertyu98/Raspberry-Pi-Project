import DHT11
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep
import PIR_test
import Relay
import time
import settings



###Funtion to update temperature and humidity on LCD
def updatedisplay():    
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    print ('Attempting to Print')
    lcd.setCursor(0,0)  # set cursor position
    lcd.message( 'Currently:' )
    lcd.setCursor(11,0)  # go to next row
    lcd.message( str(settings.dht_temp[-1]))
    lcd.setCursor(15, 0)
    lcd.message( 'C' )
    lcd.setCursor(0,1)
    lcd.message( 'With' )
    lcd.setCursor(5,1)
    lcd.message( str(settings.dht_humidity[-1]))
    lcd.setCursor(8, 1)
    lcd.message( '% Humid' )
    
def final():
    Relay.setup()       # Initialize relay
    PIR_test.setup()    # initialize PIR
    settings.init()     # Initialize arrays and variables
    
    DHT11.update()      # Update values
    updatedisplay()
    setduration()
    print('Starting Irrigation Now')
    Relay.irrigate()

def setduration():
    settings.gallonsneeded = (float(settings.eto[0]) * 165.333)
    settings.secondsneeded = (settings.gallonsneeded/0.283)
    val = settings.secondsneeded
    print ('Need ', val , 'seconds of irrigation at 1020 gallons per hour')
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.

try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    print ('I2C Address Error !')
    exit(1)
    
    
    
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

#adding event detection for PIR sensor, if detected callback is called
GPIO.add_event_detect(7, GPIO.RISING, callback= PIR_test.loop)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        final()
    except KeyboardInterrupt:
        lcd.clear()                         # lcd off
        GPIO.output(relayPin, GPIO.LOW)     # relay off
        RPi.GPIO.cleanup()
        exit()  
