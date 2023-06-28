# Project 19：Flame Alarm

### **Introduction**

Fire is a terrible thing and fire alarm systems are very useful in houses, commercial buildings and factories. In this project, we will use a Raspberry Pi Pico to control a flame sensor , a buzzer and LED to make fire alarm devices, which is a meaningful maker activity.



### **Components Required**

| ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps27.png) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps28.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps29.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps30.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps31.jpg) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Raspberry Pi Pico*1                                          | Raspberry Pi Pico Expansion Board*1                          | Flame Sensor*1                                               | Red LED*1                                                    | Active Buzzer*1                                              |
| ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps32.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps33.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps34.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps35.jpg) | ![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml11676\wps36.jpg) |
| Breadboard                                                   | 220ΩResistor*1                                               | 10KΩResistor*1                                               | Jumper Wires                                                 | USBCable*1                                                   |



### **Component Knowledge**

![image-20230425100858161](media/image-20230425100858161.png)

**Flame Sensor**：

The flame emits a certain degree of IR light, which is invisible to the human eye, but our flame sensor can detect it and alert the microcontroller. If the Raspberry Pi Pico has detected a fire, it has a specially designed infrared receiver to detect the flame, and then convert the flame brightness into a fluctuating level signal. 

The short pin of the receiving triode is negative pole and the other long pin is positive pole. We should connect the short pin (negative pole) to 5V and the long pin (positive pole) to the analog pin, a resistor and GND. As shown in the figure below.

![](media/87bd204db523c602c80745266c1ee452.png)

Note: 

Since vulnerable to radio frequency radiation and temperature changes, the flame sensor should be kept away from heat sources like radiators, heaters and air conditioners, as well as direct irradiation of sunlight, headlights and incandescent light.



### **Read the Simulation Value**

We start with a simple code to read the value of the flame sensor and print it on the serial monitor. For wiring, please refer to the following wiring diagram.

![](media/85531078db041bba05599b3a1118a7bc.png)

![](media/1e3c424f7cc7ac797ab0b8ae4a00f4f1.png)

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\3. Raspberry Pi System\Python_Tutorial\2. Projects\Project 19：Flame Alarm. 

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→”Project 19：Flame Alarm”. And double left-click “Project\_19.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](media/f566b02fa7abceb8c609fa961f94ebf7.png)

```python
from machine import ADC, Pin
import time
# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the flame sensor cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/7bb44e167d87bdb821315bf809cf8036.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the simulation value read by the flame sensor. 

When the flame is close to the sensor, the simulation value increases. On the contrary, the simulated value decreases. 

Press“![](media/ec00367ea605788eab454cd176b94c7b.png)Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](media/a5bb49291add50b4016c8215ae6b698d.png)

![](media/7c04b9dd8c4a10e7b9788ecd95eeeeaa.png)

### **Circuit Diagram and Wiring Diagram**

Next, we will use flame sensor and buzzer, an RGB LED to make an interesting project, that is flame alarm. When flame is detected, RGB LED is red and buzzer alarms.

![](media/c2b7feb8039e618ba070a9714ef06554.png)

![](media/0cd1ee17a6f8de81464817090c5832eb.png)

### **Test Code**

Note：![](media/40a3ea572836945268b22dfc0cce29c3.png) The threshold of 500 in the code can be reset itself as required.

Go to the folder KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 19：Flame Alarm.

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→Project 19：Flame Alarm”. And double left-click the“Project\_19.2\_Flame\_Alarm.py”.

![](media/96fac91877005bf6b06ad3e43bec025e.png)

```python
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
```



### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/0c1eb4ac2520b87b4cdae31f89188d14.png)

Click“![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that when the flame sensor detects the flame, the LED flashes and the buzzer alarms. Otherwise, the LED does not light, the buzzer does not sound. 

Click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/158932123b144f9b09e64b05b38bf139.png)
