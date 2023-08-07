# Project 18 : Dimming Light

**Introduction**

A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. It works by varying the position of a sliding contact across a uniform resistance. In a potentiometer, the entire input voltage is applied across the whole length of the resistor, and the output voltage is the voltage drop between the fixed and sliding contact. 

In this project, we are going to learn how to use Raspberry Pi Pico to read the values of the potentiometer, and make a dimming lamp with LEDs.

**Components Required**

| ![img](media/wps21.png) |![img](media/wps22-168421985366337.jpg)|![img](media/wps23-168421985550138.jpg)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|
| ------------------------------------------------------- | ------------------------------------ | ------------------------ | --------------------------- |
| Raspberry Pi Pico\*1                                    | Raspberry Pi Pico Expansion Board\*1 | Potentiometer\*1         | Red LED\*1                  |
| ![img](media/wps24.jpg) |![img](media/wps25.jpg)|![img](media/wps26.jpg)|![](media/7dcbd02995be3c142b2f97df7f7c03ce.png)|
| Breadboard\*1                                           | 220ΩResistor\*1                      | Jumper Wires             | USB Cable\*1                |

**Component Knowledge**

![](media/03ab81e8b4f09287d2781ef0fd297f85.png)

**Adjustable potentiometer:** 

It is a kind of resistor and an analog electronic component, which has two states of 0 and 1(high level and low level). The analog quantity is different, its data state presents a linear state such as 1 ~ 1024.

**Read the Potentiometer Value**

We connect the adjustable potentiometer to the analog IO of the Raspberry Pi Pico to read its value and voltage value . Please refer to the following wiring diagram for wiring.

![](media/b8ee6320bce8729a4309857f257d30ec.png)

![](media/cb970a340d830569e9ac4462a1318e44.png)

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 18：Dimming Light. You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click““This computer”→“home”→“pi”→“2. Projects”→“Project 18：Dimming Light”. And click “Project\_18.1\_Read\_Potentiometer\_Analog\_Value.py”.

![](media/d0984cd731cd08a852cc3a56f70aca22.png)

```python
from machine import ADC, Pin
import time
# Initialize the potentiometer to pin 26 (ADC function)
adc = ADC(26)

# Print the current adc value of the potentiometer cyclically 
# Print the current voltage value of the potentiometer cyclically
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        voltage = adcValue / 65535.0 * 3.3
        print("ADC Value:", adcValue, "Voltage:", voltage, "V")
        time.sleep(0.1)
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/a219d9584daf3a064fd034a75bdcf923.png)

Click“![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the ADC value and voltage value of the potentiomete, turn the potentiometer handle, the ADC value and voltage value will change.

Click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/d87e1f1d7a3d9b02ffea5b1685cbdce4.png)

![](media/969b9de3cf505f05d6a9361286cef9c9.png)

**Circuit Diagram and Wiring Diagram**

In the last step, we read the value of the potentiometer, and now we need to convert the value of the potentiometer into the brightness of the LED to make a lamp that can adjust the brightness. 

The wiring diagram is as follows:

![](media/66f721b77035d40556c873e0c4577b4a.png)

![](media/93b03f3cdc8af506d9035b748839ac33.png)

**Test Result**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 18：Dimming Light.

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project 18：Dimming Light”. And double left-click the “Project\_18.2\_Dimming\_Light.py”.

![](media/17160723a76ed212ae136d49533e71c0.png)

```python
from machine import ADC, Pin, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(1000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        pwm.duty_u16(adcValue) #map it to the duty cycle of PWM to control led brightness 
        time.sleep(0.1)
except:
    pwm.deinit()
```



**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/d9074ae5a53d21e2aedc2f78c03ba105.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that turn the potentiometer handle and the brightness of the LED will change accordingly.

Click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/645d76a0282256c7638333914b9a22c9.png)

![](media/eca30dead3f4923afa0dcb0306db2319.jpeg)
