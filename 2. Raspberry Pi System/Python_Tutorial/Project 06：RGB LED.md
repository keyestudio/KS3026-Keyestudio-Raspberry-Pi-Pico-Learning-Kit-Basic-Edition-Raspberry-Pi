# Project 06: RGB LED

**Introduction**

![](media/94bdff69e438989d8e0934e57f2e5c00.png)

RGB LEDS are made up of three colors (red, green, and blue) , which can emit different colors by mixing these three basic colors. 

In this project, we will introduce the RGB LED and show you how to use the Raspberry Pi Pico to control the RGB LED. Even though RGB LED is very basic, it is also a great way to learn the fundamentals of electronics and coding.

**Components Required**

| ![image-20230516140304148](media/image-20230516140304148.png) | ![image-20230516140312233](media/image-20230516140312233.png) |![](media/f1a86fc81ab4b043263ce7e01e14d470.png)||
| ------------------------------------------------------- | ------------------------------------ | ------------------------------- | ---------------------- |
| Raspberry Pi Pico\*1                                    | Raspberry Pi Pico Expansion Board\*1 | RGB LED\*1                      |                        |
| ![image-20230516140324245](media/image-20230516140324245.png) |![image-20230516140331045](media/image-20230516140331045.png)|![image-20230516140336503](media/image-20230516140336503.png)|![](media/7dcbd02995be3c142b2f97df7f7c03ce.png)|
| 220ΩResistor\*3                                         | Breadboard\*1                        | Jumper Wires                    | USB Cable\*1           |



**Component Knowledge**

The monitors mostly adopt the RGB color standard, and all the colors on the computer screen are composed of the three colors of red, green and blue mixed in different proportions.

![](media/8bf1339719a922f2fbc1e01a4347b4ab.png)

This RGB LED has 4 pins and a common cathode. To change its brightness, we can use the PWM of the Raspberry Pi Pico pins, which can give different duty cycle signals to the RGB LED to produce different colors.

If we use three 10-bit PWM to control the RGBLED, theoretically we can create 210\*210\*210= 1,073,741,824(1 billion) colors through different combinations.



**Circuit Diagram and Wiring Diagram**

![](media/f6950bc8498e6139cbb67db84cdd5a9a.png)

![](media/fdab8c2fd2dfdd1670c09962e7b458ce.png)

**Note:**

RGB LED longest pin (common cathode) connected to GND.

![](media/1584356c63bf99934ae0810ee02dced3.png)

How to identify the 220Ω 5-band resistor

![](media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3.Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 06：RGB LED. You can move the code to anywhere.For example, we can save the pi folder of the Raspberry Pi System, the route is home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“2. Projects”→“Project 06：RGB LED”and double left-click the“Project\_06\_RGB\_LED.py”.

![](media/fa2c2f91ec4700ce6c73e4acb045df45.png)

```python
# import Pin, PWM and Random function modules.
from machine import Pin, PWM
from random import randint
import time

#configure ouput mode of GP18, GP17 and GP16 as PWM output and PWM frequency as 10000Hz.
pins = [18, 17, 16]
freq_num = 10000

pwm0 = PWM(Pin(pins[0]))  #set PWM
pwm1 = PWM(Pin(pins[1]))
pwm2 = PWM(Pin(pins[2]))
pwm0.freq(freq_num)
pwm1.freq(freq_num)
pwm2.freq(freq_num)

#define a function to set the color of RGBLED.
def setColor(r, g, b):
    pwm0.duty_u16(65535 - r)
    pwm1.duty_u16(65535 - g)
    pwm2.duty_u16(65535 - b)
    
try:
    while True:
        red   = randint(0, 65535) 
        green = randint(0, 65535)
        blue  = randint(0, 65535)
        setColor(red, green, blue)
        time.sleep_ms(200)
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit() 
```



**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, click ![](media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”.

![](media/c338d727e51749fcf4e331cc729207ae.png)

Click “![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that RGB LED starts showing random colors.

Press“Ctrl+C”or click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/b6f35a993624aa56b058ca411d43e096.png)
