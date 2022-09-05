#Raspberry Pi Pico W by SKANTA (TechCree)
#load liberies for wlan and html
from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password
#load liberies for Pico W Onboard Temperatur Sensor
import machine 
import utime
from machine import ADC #Mainboard Sensor
from machine import Pin
import time, random
#load liberies for Pico W onboard LED
from machine import Pin, Timer

#connect to wifi
connect_to_wifi(ssid, password)
#generate a logfile
logging.info("logged on")

#load Pico Led Pin/GPIO mainboard led ist PIN 25
led = Pin(25, Pin.OUT)

#setup Temperaturmessure and convert to readable
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535)

reading = sensor_temp.read_u16() * conversion_factor
temperature = round(27 - (reading - 0.706) / 0.001721)
tempa=temperature

#blink LED
intled = machine.Pin("LED", machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    
tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

#start server
@server.route("/")
def index(request):
    return render_template("index.html", tempa=(temperature))

server.run()