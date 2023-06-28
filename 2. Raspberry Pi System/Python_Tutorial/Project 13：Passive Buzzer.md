# Project 13：Passive Buzzer

### **Introduction**

In a previous project, we have learned an active buzzer, which can only produce one sound and may let you feel monotonous. 

In this project, we will learn a passive buzzer and use the Raspberry Pi Pico to control the passive buzzer to sound an alarm. Unlike the active buzzer, the passive buzzer can emit sounds of different frequencies. 

### **Components Required**

| ![img](media/wps5.png)                | ![img](media/wps6-16842186555165.jpg) | ![img](media/wps7-16842186569006.jpg) |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| Raspberry Pi Pico*1                   | Raspberry Pi PicoExpansion Board*1    | Passive Buzzer*1                      |
| ![img](media/wps8-16842186587557.jpg) | ![img](media/wps9-16842186604858.jpg) | ![img](media/wps10.jpg)               |
| Breadboard*1                          | Jumper Wires                          | USB Cable*1                           |



### **Component Knowledge**

![](media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave, not a DC signal. 

The two buzzers are very similar in appearance, but one buzzer with a green circuit board is a passive buzzer, while the other with black tape is an active buzzer. 

Passive buzzers cannot distinguish between positive polarity while active buzzers can.

![](media/fc42c5ed014609ff0b290ee5361bb2fd.png)

### **Circuit Diagram and Wiring Diagram**

![](media/e0da1ccdbff24d256db130816c55da74.png)

![](media/e601e48f8deddb3e9e7734d0022106b3.png)

### **Test Code**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 13：Passive Buzzer. 

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project 13：Passive Buzzer”. And double left-click the“Project\_13\_Passive\_Buzzer.py”.

![](media/0ae6aecf5d0df477745a223e743a1362.png)

```python
from machine import Pin
import time

#Initialize the passive buzzer
buzzer = Pin(16,Pin.OUT)

#Simulate two different frequencies
while True:
    #Output 500HZ frequency sound
    for i in range(80):
        buzzer.value(1)
        time.sleep(0.001)
        buzzer.value(0)
        time.sleep(0.001)
    #Output 250HZ frequency sound
    for i in range(100):
        buzzer.value(1)
        time.sleep(0.002)
        buzzer.value(0)
        time.sleep(0.002)
```



### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/768c2e41ce5b5cc212a79538d77fc815.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the the passive buzzer sounds the alarm.

Click ![](media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](media/6d7aeb45a390b49d5852638137dff2b4.png)
