# Project 21：Temperature Instrument

### **Introduction**

Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.

### **Components Required**

| ![img](media/wps46.png) | ![img](media/wps47.jpg)             | ![img](media/wps48.jpg) | ![img](media/wps49.jpg) |                         |
| ----------------------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- |
| Raspberry Pi Pico*1     | Raspberry Pi Pico Expansion Board*1 | Thermistor*1            | 10KΩResistor*1          |                         |
| ![img](media/wps50.jpg) | ![img](media/wps51.jpg)             | ![img](media/wps52.jpg) | ![img](media/wps53.jpg) | ![img](media/wps54.jpg) |
| 10CM M-F Dupont Wires   | Breadboard*1                        | LCD 128X32 DOT*1        | Jumper Wires            | USB Cable*1             |



### **Component Knowledge**

Thermistor: 

A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. 

Thermistors and its electronic symbols are shown below:

![](media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

![img](media/wps1.png)

**In the formula: **

**Rt** is the resistance of the thermistor at T2 temperature.

**R** is the nominal resistance value of the thermistor at T1 room temperature.

**EXP\[n\]** is the nth power of e.

**B** is the temperature index

**T1** and **T2** refer to K degrees, that is, Kelvin temperature. 

Kelvin temperature =273.15 + Celsius temperature. 

For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:



### **Read the Values**

First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](media/c143dc239ceaa5e65a63f47d6512630c.png)

![](media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 21:Temperature Instrument You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project 21：Temperature Instrument””. And double left-click the“Project\_21.1\_Read\_the\_thermistor\_analog\_value.py”.

![](media/4e8c0c25db541f311e4aeffe28249373.png)

```python
from machine import Pin, ADC
import time
import math

#Set ADC
adc=ADC(27)

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        print("ADC value:", adcValue, "  Voltage: %0.2f"%voltage + "V",
              "  Temperature: " + str(tempC) + "C")
        time.sleep(1)
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.

![](media/ba16d8cf0bd8e1d6d9bd8f97ba9b3074.png)

Click “![](media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  

Press“Ctrl+C”or click“![](media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](media/390f4916067d7f96f69e34021493dd98.png)

![](media/06c41e9d588bbf22196cb6bbc80a88ca.png)

### **Circuit Diagram and Wiring Diagram**

Note : LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. 

Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](media/91445212232765942d482b84da03f598.png)

### **Test Code**

The code used in this project is KS3026Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 21：Temperature Instrument. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click “This computer”→“home”→“pi”→“2. Projects”→”Project 21:Temperature Instrument”. And click the “Project\_21.2\_Temperature\_Instrument.py”.

![](media/87a41abd880e2917922bf5001fae3a18.png)

![](media/3410480c2c804ab84e295e7823d13722.png)

![](media/5b360f9f8ce4531e67bfa188bfb4b5f3.png)

```python
from machine import Pin, ADC, I2C
import time
import math
import lcd128_32_fonts
from lcd128_32 import lcd128_32

#Set ADC
adc=ADC(27)

#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        
        if use_i2c:
            scan_for_devices()
            lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
            
        lcd.Clear()
        lcd.Cursor(0, 0)
        lcd.Display("Voltage:")
        lcd.Cursor(0, 8)
        lcd.Display(str(voltage))
        lcd.Cursor(0, 20)
        lcd.Display("V")
        lcd.Cursor(2, 0)
        lcd.Display("Temperature:")
        lcd.Cursor(2, 12)
        lcd.Display(str(tempC))
        lcd.Cursor(2, 15)
        lcd.Display("C")
        time.sleep(0.5)
except:
    pass
```



### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.

![](media/ebb4482f92c24400b9ac289df302bb73.png)

Click“![](media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. 

Click“![](media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](media/0df5f15c0dbad88b64ac82679b42c1b3.png)
