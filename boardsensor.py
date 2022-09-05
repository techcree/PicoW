#Show Temperatur
import machine 
import utime
from machine import ADC #Mainboard Sensor
from machine import Pin
import time, random


#Led Pins laden nach Feldnr. GPIO sortiert
led = Pin(25, Pin.OUT) #mainboard led

# Setup Temperaturmessung und Konvertierung
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535)
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)
    tempa=temperature
    #print("TEMPERATUR")
#    print ((tempa), "°C")
    #print("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 7)
    utime.sleep(3)
