# Project 05：Traffic Lights

**Introduction**

Traffic lights are closely related to people's daily lives, which generally show red, yellow, and green. Everyone should obey the traffic rules, which can avoid many traffic accidents. In this project, we will use Raspberry Pi Pico and some LEDs (red, green and yellow) to simulate the traffic lights.

**Components Required**

| ![img](media/wps1-16842165985231.png) | ![img](media/wps2.jpg)              | ![img](media/wps3.jpg) |
| ------------------------------------- | ----------------------------------- | ---------------------- |
| Raspberry Pi Pico*1                   | Raspberry Pi Pico Expansion Board*1 | Breadboard*1           |
| ![img](media/wps4.jpg)                | ![img](media/wps5.jpg)              | ![img](media/wps6.jpg) |
| Red LED*1                             | Yellow LED*1                        | Green LED*1            |
| ![img](media/wps7.jpg)                | ![img](media/wps8.jpg)              | ![img](media/wps9.jpg) |
| USB Cable*1                           | 220ΩResistor*3                      | Jumper Wires           |



**Circuit Diagram and Wiring Diagram**

![](media/4cf2ad735b0df82d62a5fcdb19ebf3c0.png)

![](media/98f9db025163638c33095cbd16abe7e7.png)

Note:

How to connect an LED

![](media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\3. Raspberry Pi System\Python_Tutorial\2. Projects\Project 05:Traffic Lights. You can move the code to anywhere.For example, we save it in the oi folder of the Raspberry Pi system, the route is home/pi/2. Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“2. Projects”→"Project 05: Traffic Lights”. And double-click “Project\_05\_Traffic\_Lights.py”.

![](media/bb44b31699957a99ec3e33f7a887e1be.png)

```python
from machine import Pin
import time

led_red = machine.Pin(16, machine.Pin.OUT)  # create red led object from Pin 16, Set Pin 16 to output
led_yellow = machine.Pin(17, machine.Pin.OUT)  # create yellow led object from Pin 17, Set Pin 17 to output
led_green = machine.Pin(18, machine.Pin.OUT) # create green led object from Pin 18, Set Pin 18 to output

while True:
    led_red.value(1)  # Set red led turn on
    time.sleep(5)   # Sleep 5s
    led_red.value(0) # Set red led turn off 
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_green.value(1)
    time.sleep(5) 
    led_green.value(0) 
```



**Test Result：**

Connect the pico board to the Raspberry Pi. Click![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](media/3691a51f61750b1dc918de0f771a5482.png)

Click“![](media/bb4d9305714a178069d277b20e0934b7.png)”, the code starts executing, what we will see are below:

1.  First, the green light will be on for 5 seconds and then off; 

2.  Next, the yellow light blinks three times and then goes off. 

3.  Then, the red light goes on for five seconds and then goes off. 
    

Repeat steps 1 to 3 above and press“Ctrl+C”or click“![](media/ec00367ea605788eab454cd176b94c7b.png)” to exit the program.

![](media/5da95e477cc75ec61a63e001cd7e6a58.png)
