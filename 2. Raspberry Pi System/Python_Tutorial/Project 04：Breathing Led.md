# Project 04: Breathing Led

### **Introduction**

In previous studies, we know that LEDS have on/off state, so how to enter the intermediate state? How to output an intermediate state to make the LED "half bright"? That's what we're going to learn. Breathing lights, or LEDS turn on and off again, which are like "breathing". 

So, how to control the brightness of LEDS? We will use the Raspberry Pi Pico PWM to achieve this goal.  



### **Components**

| ![image-20230516135150566](media/image-20230516135150566.png) | <img src="media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="zoom:50%;" /> | ![image-20230516135157409](media/image-20230516135157409.png) ||
| ------------------------------------------------------- | ------------------------------------ | ---------------------- | ---------------------- |
| Raspberry Pi Pico\*1                                    | Raspberry Pi Pico Expansion Board\*1 | Breadboard\*1 |                        |
| ![image-20230516135207872](media/image-20230516135207872.png) |![image-20230516135213310](media/image-20230516135213310.png)|![image-20230516135218781](media/image-20230516135218781.png)|![](media/7dcbd02995be3c142b2f97df7f7c03ce.png)|
| Red LED\*1                                              | 220Ω Resistance\*1                   | Jumper Wire\*2         | USB Cable\*1           |

### **Knowledge**

![](media/6549bdbfd4e7b6b2b341012105d655e8.png)

**Analog & Digital**

Analog signals are continuous signals in both time and value. By contrast, a digital or discrete time signal is a time series consisting of a series of numbers. 

Most signals in life are analog signals. A familiar example of an analog signal is how temperatures change continuously throughout the day, rather than suddenly changing from 0 to 10 in a flash. However, the value of a digital signal can change instantaneously. 

This change is represented numerically as 1 and 0(the basis of binary code). It's easier to see the difference, as shown below:

![](media/4bdf6127e563b453a1fd8953b4ebb277.png)

In practical applications, we often use a binary as a digital signal, which are a series of 0 and 1. Since binary signals have only two values (0 or 1), they have great stability and reliability. 

Finally, analog and digital signals can be converted to each other. 

**PWM：**

Pulse Width Modulation (PWM) is an effective method to control analog circuit by digital signal. 

Ordinary processors cannot directly output analog signals. The PWM makes this conversion (convert digital signal to analog signal) very convenient, which uses digital pins to send square waves at a certain frequency, which is high and low output to alternate for a period of time. 

The total time of each set of high and low levels is generally fixed, which is called the period (Note: the reciprocal of the period is the frequency). The time of the high level output is usually called pulse width, and the duty cycle is the percentage of the pulse width (PW) to the total period (T) of the waveform. The longer the duration of the high level output as well as the duty cycle is, the higher the corresponding voltage in the analog signal will be. 

The figure below shows the variation of analog signal voltage from 0V to 3.3V(high level is 3.3V) corresponding to pulse width of 0% to 100%.  

![](media/a439e1bd8a4578b43b7188c821d58594.jpeg)

We all know that the longer the PWM duty cycle is, the higher the output power will be. Therefore, we can use PWM to control the brightness of LEDS or the speed of dc motors and so on. 

As can be seen from the above, the PWM is not a real analog signal, and the effective value of the voltage is equal to the corresponding analog signal. 

Therefore, we can control the output power of LEDS and other output modules to achieve different effects.

**Raspberry Pi Pico and PWM**

The Raspberry Pi Pico has 16 PWM channels, each of which can control frequency and duty cycle independently. The clock frequency ranges from 7Hz to 125MHz.  Each pin on the Raspberry Pi Pico can be configured for PWM output.  



### **Circuit Diagram and Wiring Diagram**

![](media/cb069d7553d861e3293d8bdbe85bbd05.png)

![](media/898285da10fa9b39e52a02bc68758d27.png)

**Note:**

How to connect the LED

![](media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

The design of this project makes the GP16 output PWM, and the pulse width gradually increases from 0% to 100%, and then gradually decreases from 100% to 0%.  

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\3. Raspberry Pi System\Python_Tutorial\2. Projects\Project 04：Breathing Led. 

You can move the code to anywhere.For example, we save it in the oi folder of the Raspberry Pi system, the route is home/pi/2. Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“2. Projects”→”Project 04: Breathing Led”. And double-click “Project\_04\_Breathing\_Led.py”.

![](media/fb732f2603ea6f808c2fda117dd865f8.png)

```python
#MicroPython implementation of raspberry PI Pico board LED breathing lamp program example
import time
from machine import Pin,PWM
PWM_PulseWidth=0
#Using external LED, build PWM object PWM LED
pwm_LED=PWM(Pin(16))
#Set the PWM LED frequency
pwm_LED.freq(500)
while True:
    while PWM_PulseWidth<65535:
        PWM_PulseWidth=PWM_PulseWidth+50
        time.sleep_ms(1)   #Delay 1 ms 
        pwm_LED.duty_u16(PWM_PulseWidth)
    while PWM_PulseWidth>0:
        PWM_PulseWidth=PWM_PulseWidth-50
        time.sleep_ms(1)
        pwm_LED.duty_u16(PWM_PulseWidth)
```



### **Test Result：**

Connect the pico board to the Raspberry Pi. Click![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](media/ac7c042fd7d45662f04395de18f19019.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then the LED on the picoboard will flash; click ![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](media/9e8a8c744f9d22c8821016ea4b0491ba.png)

![image-20230425090657130](media/image-20230425090657130.png)
