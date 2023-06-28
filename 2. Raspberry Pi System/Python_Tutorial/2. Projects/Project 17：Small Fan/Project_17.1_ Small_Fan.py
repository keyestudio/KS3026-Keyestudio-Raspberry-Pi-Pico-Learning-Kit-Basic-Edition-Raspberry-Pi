from machine import Pin
import time

motor = Pin(22, Pin.OUT)   # create S8050 object from Pin 22, Set Pin 22 to output

try:
    while True:
        motor.value(1)    # Set motor turn on
        time.sleep(4) # Sleep 4s
        motor.value(0)    # Set motoe turn off
        time.sleep(2) # Sleep 2s
except:
    pass
