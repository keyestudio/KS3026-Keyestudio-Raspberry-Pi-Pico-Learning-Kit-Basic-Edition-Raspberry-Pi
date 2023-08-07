# Project 20：Night Lamp

**Introduction**

Sensors or components are ubiquitous in our daily life. For example, some public street lights turn on automatically at night and turn off automatically during the day. 

Why? In fact, this make use of a photosensitive element that senses the intensity of external ambient light. When the outdoor brightness decreases at night, the street lights will automatically turn on. In the daytime, the street lights will automatically turn off. The principle of this is very simple. 

In this lesson we will use Raspberry Pi Pico to control LEDs to implement the function of this street light.

**Components Required**

| ![img](media/wps37.png) | ![img](media/wps38.jpg)             | ![img](media/wps39.jpg) | ![img](media/wps40.jpg) | ![img](media/wps41.jpg) |
| ----------------------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- |
| Raspberry Pi Pico*1     | Raspberry Pi Pico Expansion Board*1 | Photoresistor*1         | Red LED*1               | 10KΩResistor*1          |
| ![img](media/wps42.jpg) | ![img](media/wps43.jpg)             | ![img](media/wps44.jpg) | ![img](media/wps45.jpg) |                         |
| Breadboard*1            | 220ΩResistor*1                      | Jumper Wires            | USB Cable*1             |                         |



**Component Knowledge**

<img src="media/9e553e75b6f976f33438171eb2f2e775.png" style="zoom:33%;" />

It is a photosensitive resistor, its principle is that the photoresistor surface receives brightness (light) to reduce the resistance. The resistance value will change with the detected intensity of the ambient light . With this property, we can use photoresistors to detect light intensity.  

Photoresistors and other electronic symbols are as follows:


![](media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of photoresistors:

![](media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes due to the change of light intensity, the voltage between the photoresistor and resistance R2 will also change.  Thus, the intensity of light can be obtained by measuring this voltage.



**Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print it in the serial monitor. For wiring, please refer to the following wiring diagram.

![](media/e3fde13b200927346e04b032373ce638.png)

![](media/b97ff27ae10e3499c36312c8ee4881f8.png)

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 20：Night Lamp.

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→”Project 20：Night Lamp”. And double left-click the “Project\_20.1\_Read\_Photosensitive\_Analog\_Value.py”.

![](media/2d0202f60ae6bc534126b44e28b74602.png)

```python
from machine import ADC, Pin
import time
# Initialize the photoresistance to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the photoresistance and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the photoresistance cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click “![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/e298d8af35eb4a25f83169e0fd067e57.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog value read by the photoresistor. 

When the light intensity around the photoresistor is gradually reduced, the analog value will gradually increase. On the contrary, the analog value decreases gradually. 

Click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/d78d3517ac1f6c9cea373c862291897f.png)

![](media/bbabb2d5c4a997c5024e6023cb272261.png)

**Circuit Diagram and Wiring Diagram**

We made a little dimmer in the front, now let's make a light controlled lamp. The principle is the same, the Raspberry Pi Pico will be used to obtain the analog value of the sensor and then adjust the brightness of the LED.  

![](media/b8e8d95bdc869bf76465fa73645db831.png)

![](media/71f2886dc6fa97d02e2ecd0d429af71b.png)

**Text Code**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 20：Night Lamp. You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→Project 20：Night Lamp. And double left-click the“Project\_20.2\_Night\_Lamp.py”.

![](media/ae27830403a2f741aa9b725e5324c215.png)

![](media/d90699744cf1df3038872afef61bbb4a.png)

```python
from machine import Pin, ADC, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(10000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of photoresistance
        pwm.duty_u16(adcValue) # map ADC value to the duty cycle of PWM to control led brightness
        time.sleep(0.1) # delay
except:
    pwm.deinit()
```



**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/af676243a409f680afc488edadb24a15.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that when the intensity of light around the photoresistor is reduced, the LED will be bright, on the contraty, the LED will be dim. 

Click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/823af9b3bdb27286aa07871e9457064b.png)
