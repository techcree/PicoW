import machine
from machine import Pin, Timer

intled = machine.Pin("LED", machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    
tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)