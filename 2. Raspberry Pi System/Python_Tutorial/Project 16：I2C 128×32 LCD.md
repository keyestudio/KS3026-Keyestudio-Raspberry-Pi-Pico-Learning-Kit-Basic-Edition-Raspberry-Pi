# Project 16： I2C 128×32 LCD

### **Introduction**

We can use modules such as monitors to do various experiments in life. You can also DIY a variety of small objects. For example, you can make a temperature meter with a temperature sensor and display, or make a distance meter with an ultrasonic module and display.

In this project, we will use the LCD_128X32_DOT module as a display and connect it to a Raspberry Pi Pico, which will be used to control the LCD_128X32_DOT display to show various English characters, common symbols and numbers.

### **Components Required**

| ![img](media/wps10-168421920933426.png) |![img](media/wps11-168421921147827.jpg)|![img](media/wps12-168421921314128.jpg)|![](media/7dcbd02995be3c142b2f97df7f7c03ce.png)|
| ------------------------------------------------------- | ----------------------- | --------------------------- | ---------------------- |
| Raspberry Pi Pico\*1                                    | LCD\_128X32\_DOT\*1     | 10CM M-F Dupont Wires       | USB Cable\*1           |

### **Component Knowledge**

![](media/2c2645e94a00867ac23e8a022f0a631a.png)

**LCD\_128X32\_DOT:** 

It is an LCD module with 128*32 pixels and its driver chip is ST7567A. The module uses the IIC communication mode, while the code contains a library of all alphabets and common symbols that can be called directly. When using, we can also set it in the code so that the  English letters and symbols show different text sizes. 

To make it easy to set up the pattern display, we also provide a mold capture software that converts a specific pattern into control code and then copies it directly into the test code for use.

**Schematic diagram:**

![](media/5451aed32bc5b7b30fbd5613ad09a65b.png)

**Features:**

- Pixel：128\*32 character

- Operating voltage(chip)：4.5V to 5.5V

- Operating current：100mA (5.0V)

- Optimal operating voltage(module):5.0V



### **Circuit Diagram and Wiring Diagram**

Note: The LCD_128X32_DOT must be connected with 10CM M-F Dupont wires, which can make the LCD_128X32_DOT display normally. Otherwise, using 20CM M-F Dupont wires may cause the LCD_128X32_DOT display abnormally.  

![](media/82aae0a70e5628c53d7f81f7730cf79a.png)

### **Test Code**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 16：I2C 128×32 LCD.

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project 16： I2C 128×32 LCD”. 

Select “lcd128\_32.py” and “lcd128\_32\_fonts.py”，right-click and select “Upload to /”，wait for the “lcd128\_32.py” and the “lcd128\_32\_fonts.py” to be uploaded to the Raspberry Pi Pico. 

And double-click the “Project 16：I2C 128×32 LCD.py”.

![](media/d0c6c793bde093049f25c45588fbf1d3.png)

![](media/596a32d2dee1d8668263634d5e1144d6.png)

![](media/69cd526506cbf06418fb512ba7e7f71e.png)

```python
import machine
import time
import lcd128_32_fonts
from lcd128_32 import lcd128_32

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

if use_i2c:
    scan_for_devices()
    lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)

lcd.Clear()

lcd.Cursor(0, 4)
lcd.Display("KEYESTUDIO")
lcd.Cursor(1, 0)
lcd.Display("ABCDEFGHIJKLMNOPQR")
lcd.Cursor(2, 0)
lcd.Display("123456789+-*/<>=$@")
lcd.Cursor(3, 0)
lcd.Display("%^&(){}:;'|?,.~\\[]")
"""
while True:
    scan_for_devices()
    time.sleep(0.5)
"""
```



### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/716656c043b3708bd826ddf3c8eee1e1.png)

Click “![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the LCD module display will show "KEYESTUDIO" at the first line. 

"ABCDEFGHIJKLMNOPQR" will be displayed at the second line. 

"123456789 + - \* / \<\> = $ @ " will be shown at the third line and "% ^ & () {} :; '|?,. \~ \\\\ \[\] " will be displayed at the fourth line. 

Press“Ctrl+C”or click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/6588b76cf195f9ffeceb3db1f1db9486.png)
