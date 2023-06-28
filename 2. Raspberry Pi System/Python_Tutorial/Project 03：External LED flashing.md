## Project 03：External LED flashing 

### **Introduction**

In this project, we are going to show you the external LED flashing effect.  We will use the Raspberry Pi Pico's digital pins to turn on the LED and make it flash.



### **Components**

| ![image-20230516134405295](media\image-20230516134405295.png) | ![](media/bbed91c0b45fcafc7e7163bfeabf68f9-16841338154662.png) | ![image-20230425084841759](media/image-20230425084841759.png) |![74ca4fa6d49dbd04de6a603c6e55a9ee](media/74ca4fa6d49dbd04de6a603c6e55a9ee.png)|
| ------------------------------------------------------- | ------------------------------------ | ---------------------- | ---------------------- |
| Raspberry Pi Pico\*1                                    | Raspberry Pi Pico Expansion Board\*1 | Red LED\*1 | Jumper Wire\*2 |
|  |![image-20230516134432857](media\image-20230516134432857.png)|![image-20230516134512344](media/image-20230516134512344.png)|![](media/7dcbd02995be3c142b2f97df7f7c03ce-16841338328473.png)|
|                                                 | 220Ω Resistor\*1                     | Breadboard\*1          | USB Cable\*1           |

### **Knowledge**

**LED:**

![image-20230425084841759](media/image-20230425084841759.png)

The LED is a kind of semiconductor called “light-emitting diode”, which is an electronic device made from semiconducting materials (silicon, selenium, germanium, etc.). It has a anode and a cathode. The short lead is cathode, which connects to GND, the long lead is anode , which connects to3.3V or 5V.

![](media/f70404aa49540fd7aecae944c7c01f83.jpeg)

**5-band Resistor**

A resistor is an electronic component in a circuit that restricts or regulates the flow current flow. On the left is the appearance of the resistor and on the right is the symbol for the resistance in the circuit . Its unit is(Ω). 1 mΩ= 1000 kΩ，1kΩ= 1000Ω.

![image-20230425085223112](media/image-20230425085223112.png)


We can use resistors to protect sensitive components, such as LEDs. The strength of the resistance is marked on the body of the resistor with an electronic color code. Each color code represents a number, and you can refer to it in a resistance card.

\-Color 1 – 1st Digit

\-Color 2 – 2nd Digit

\-Color 3 – 3rd Digit

\-Color 4 – Multiplier

\-Color 5 – Tolerance

![](media/c3df005312cd9f6d4cdae6abf3cddb83.png)

In this kit, we provide three 5-band resistors with different resistance values. Take three 5-band resistors as an example.

220Ω resistor\*10

![](media/55c0199544e9819328f6d5778f10d7d0.png)

10KΩ resistor\*10

![](media/246cf3885dc837c458a28123885c9f7b.png)

1KΩ resistor\*10

![](media/19f5dfc51adfd79b04c3b164529767ed.png)

In the same voltage, there will be less current and more resistance. The connection between current, voltage, and resistance can be expressed by the formula: I=U/R. In the figure below, if the voltage is 3V, the current through R1 is: I = U / R = 3 V / 10 KΩ= 0.0003A=0.3mA.

![](media/b3eec552e4dfad361833730698621776.png)

Do not directly connect resistors with very low resistance to the two poles of the power supply, as this will cause excessive current to damage the electronic components. Resistors do not have positive and negative poles.

**Breadboard**

A breadboard is used to build and test circuits quickly before finalizing any circuit design. The breadboard has many holes , into which circuit components like integrated circuits and resistors can be inserted. A typical breadboard is as follows.

![](media/612c1381811b2d780d5f6ed6a7ec3701.png)

The bread board has strips of metal, which run underneath the board and connect the holes on the top of the board. The metal strips are laid out as shown below. 

Note that the top and bottom rows of holes are connected horizontally while the remaining holes are connected vertically.

![](media/b45e70b961537035c85878b73d371725.png)

The first two rows (top) and the last two rows (bottom) of the breadboard are used for the positive (+) and negative (-) terminals of the power supply, respectively. The conductive layout of the breadboard is shown in the following diagram.

![](media/d5478bd5eac558252cbc235479d979eb.png)

When we connect DIP (Dual In-line Packages) components, such as integrated circuits, microcontrollers, chips and so on, we can see that a groove in the middle isolates the middle part, so the top and bottom of the groove is not connected. 

DIP components can be connected as shown in the figure below:

![](media/50caf14e911c4244779e99445c658db6.png)

![](media/9b66ae2199e77fbc99b7b278dac0b567.png)

**How to use the keyestudio raspberry pico expansion board.**

Stack the Raspberry Pi Pico on the expansionboardto use, as shown below:


![](media/fae969ca3b1a4592a83a4e05f5795a5b.png)

**Power Supply**

In this project, we use a USB to connect the Raspberry Pi Pico to the computer. Please refer to the documentation for connection methods: Preparation for Python

![](media/8ea81d60b8e2132c358041235490b7d5.jpeg)

### **Circuit Diagram and Wiring Diagram**

First, cut all power to the Raspberry Pi Pico.  Then build the circuit according to the circuit diagram and wiring diagram.  After the circuits are set up and verified, using a USB cable to connect the Raspberry Pi Pico to a computer .  Note: Avoid any possible short circuits (especially connecting 3.3V and GND)\!

Warning: A short circuit may cause a large current in the circuit, causing components to overheat and permanent damage to the hardware.

![](media/cb069d7553d861e3293d8bdbe85bbd05.png)

![](media/898285da10fa9b39e52a02bc68758d27.png)

**Wiring Diagram**

Note:

How to connect a LED

![](media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω five-band resistor

![](media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

According to the circuit diagram, when the GP16 output of the Pico is high, the LED will light up; When the output power is low, the LED will light off. Therefore, we can make the LED flash repeatedly by controlling the GP16 to repeatedly output high and low levels.  

The code used in the project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\3. Raspberry Pi System\Python_Tutorial\2. Projects\Project 03：External LED flashing. You can move the code anywhere, You can move the code to anywhere. 

For example, we save it in the oi folder of the Raspberry Pi system, the route is home/pi/2. Projects.

Code running online:

Open “Thonny”, clickThis computer”→“home”→“pi”→“2. Projects”→“Project 03：External LED flashing”.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Enter the file“Project 03：External LED flashing”, double left-click“Project\_03\_External\_LED\_flashing.py”,open it, as shown below:

![](media/8b4bad2c707397cc37c542c03d7c349f.png)

![](media/41dbfef0bb4a9e876293a090afc41637.png)

```python
from machine import Pin
import time

led = Pin(16, Pin.OUT)   # create LED object from Pin 16, Set Pin 16 to output

try:
    while True:
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
```


Connect the pico board to the Raspberry Pi. Click ![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](media/de1565c576c4233dfbe6d143404f03ac.png)

Click ![](media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then the LED on the pico board will flash; click ![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](media/bb35d00ea60c7905ab81c4f36b528be6.png)

![](media/2dcc6a55b77b4175b5175f717eb196c3.png)

Note: This is the code that runs online, if we disconnect the USB cable, then restart the“Raspberry Pi Pico”, the LED will stop flashing. 

The following information will be displayed in the "Shell" window of Thonny software:  

![](media/e9abb644348e7adcdeddcee76b992755.png)

Code running offline（Upload the code to the Raspberry Pi Pico）：

Ensure that the Raspberry Pi Pico is connected to the computer, click“![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)Stop/Restart backend”.

![](media/2a48bcd6f59f1e11f127f9faa50cad92.png)

As shown below, right-click the file“Project\_03\_External\_LED\_flashing.py”，select “**Upload to**” to upload the code to the Raspberry Pi Pico.

![](media/d73c9e4598ed1888447561693be920ca.png)

Upload main.py in the same way

![](media/60dea66634bc33fd2a56495765fd6887.png)

Disconnect the USB from the Raspberry Pi Pico and reconnect, the LED in the circuit will flash repeatedly.

![](media/2dcc6a55b77b4175b5175f717eb196c3.png)

Note: The code here runs offline. If you want to stop and display the information in the Shell window, simply click“![](media/32e03e9d4211e9ef97c1d2b18f05c902.png)Stop/Restart backend” in Thonny software.


![](media/a400b9db13988d0762d991a2cb7abaec.png)
