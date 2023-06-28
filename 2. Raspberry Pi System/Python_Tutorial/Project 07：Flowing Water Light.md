# Project 07: Flowing Water Light

### **Introduction**

In our daily life, we can see many billboards made up of different colors of LED. 

They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

### **Components Required**

| ![img](media/wps10.png) | ![img](media/wps11.jpg)             | ![img](media/wps12.jpg) |                         |
| ----------------------- | ----------------------------------- | ----------------------- | ----------------------- |
| Raspberry Pi Pico*1     | Raspberry Pi Pico Expansion Board*1 | Red LED*10              |                         |
| ![img](media/wps13.jpg) | ![img](media/wps14.jpg)             | ![img](media/wps15.jpg) | ![img](media/wps16.jpg) |
| 220ΩResistor*10         | Breadboard*1                        | Jumper Wires            | USB Cable*1             |



### **Circuit Diagram and Wiring Diagram**

![](media/e6f92039d131685369db2d1ac2c30267.png)

![](media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED

![](media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

This project is to design and manufacture a flowing water light.  

Here are the steps: 

1. turn on LED \#1, then turn it off.  
2. turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off.  
3. repeating the process to achieve the "movement" of the water.

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 07：Flowing Water Light.

You can move the code to anywhere.For example, we save it in the oi folder of the Raspberry Pi system, the route is home/pi/2. Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“2. Projects”→”Project 07：Flowing Water Light”and double-click“Project\_07\_Flowing\_Water\_Light.py”

![](media/7b5bf98a689171d60a3601f16e0ad283.png)

```python
from machine import Pin
import time

#Use an array to define 10 GPIO ports connected to LED Bar Graph for easier operation.
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
#Use two for loops to turn on LEDs separately from left to right and then back from right to left
def showLed():
    for pin in pins:
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)        
    for pin in reversed(pins):
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
          
while True:
    showLed()
```



### **Test Result：**

Connect the pico board to the Raspberry Pi. Click ![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](media/909f8976896d54a32d84d7ac1f0537c1.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up like a flowing light. 

Click ![](media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](media/723dd7931ac070cf30719700f47f6850.png)

![image-20230516141018279](media/image-20230516141018279.png)
