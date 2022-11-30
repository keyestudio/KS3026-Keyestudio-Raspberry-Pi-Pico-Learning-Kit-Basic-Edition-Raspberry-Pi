from machine import ADC, Pin
import time

# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)
# create LED object from Pin 16,Set Pin 16 to output
led = Pin(16, Pin.OUT) 
# create buzzer object from Pin 17, Set Pin 17 to output
buzzer = Pin(17, Pin.OUT)   

# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# If the flame sensor detects a flame, the buzzer will beep
# and the LED will blink when the analog value is greater than 500
# Otherwise, the buzzer does not sound and the LED goes off 
while True:
    value = get_value()
    if value >500:
        buzzer.value(1)    # Set buzzer turn on
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
    else:
        buzzer.value(0)    # Set buzzer turn off
        led.value(0)    # Set led turn off
