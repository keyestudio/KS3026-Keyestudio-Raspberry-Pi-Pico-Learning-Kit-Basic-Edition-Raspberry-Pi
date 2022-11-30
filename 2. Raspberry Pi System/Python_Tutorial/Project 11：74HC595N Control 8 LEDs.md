# Project 11：74HC595N Control 8 LEDs 

1.  **Introduction**
    
    In previous projects, we have learned how to light an LED.  However,
    how to light up a lot of LEDs with only 26 I/O ports on the
    Raspberry Pi Pico? Sometimes we may run out of pins , at that time,
    we need to extend it with the shift register. You can use a 74HC595N
    chip to control up to eight outputs at a time, using only a few pins
    on your microcontroller. In addition, You can also connect multiple
    registers together to further expand the output. In this project, we
    will use a Raspberry Pi Pico, a 74HC595 chip and LEDs to make a
    flowing water light to understand the function of the chip.  

2.  **Components Required**

|                                                         |                                      |                        |                             |
| ------------------------------------------------------- | ------------------------------------ | ---------------------- | --------------------------- |
| ![](/media/3ec5906fad2172708d449390140f55e6.png) |
| Raspberry Pi Pico\*1                                    | Raspberry Pi Pico Expansion Board\*1 | 74HC595N Chip\*1       | Red LED\*8                  |
| ![](/media/7dcbd02995be3c142b2f97df7f7c03ce.png)      |
| 220ΩResistor\*8                                         | Breadboard\*1                        | Jumper Wires           | USB Cable\*1                |

3.  **Component Knowledge**
    
    ![](/media/6921c6d60135e072ed4bd24564ec4a6d.png)

**74HC595N Chip:** To put it simply, 74HC595N chip is a combination of
8-digit shifting register, memorizer and equipped with tri-state output.
The shift register and the memorizer are synchronized to different
clocks, and the data is input on the rising edge of the shift register
clock SCK and goes into the memory register on the rising edge of the
memory register clock RCK. If the two clocks are connected together, the
shift register is always one pulse earlier than the storage register.
The shift register has a serial shift input (SI) and a serial output
(SQH) for cascading. The 8-bit shift register can be reset
asynchronously (low-level reset), and the storage register has an 8-bit
Three-state parallel bus output, when the output enable (OE) is enabled
(active low), the storage register is output to the 74HC595N pin (bus).

![](/media/858b189f06ad68afe051b15043b2affd.png)

**Pins**：

|                       |                                                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pin13 OE              | It is an output enable pin to ensure that the data of the latch is input to the Q0 to Q7 pins or not. When it is low, no high level is output. In this experiment, we directly connect to GND and keep the data output low. |
| Pin14 SI              | This is the pin for 74HC595 to receive data, i.e. serial data input, only one bit can be input at a time, then 8 times in a row, it can form a byte.                                                                        |
| Pin10 SCLR            | A pin to initialize the storage register pins. It initializes the internal storage registers at a low level. In this experiment, we connect VCC to maintain a high level.                                                   |
| Pin11 SCK             | The clock pin of the shift register. At the rising edge, the data in the shift register is shifted backward as a whole, and new data input is received.                                                                     |
| Pin12 RCK             | The clock input pin of the storage register . At the rising edge, the data is transferred from the shift register to the storage register. At this time, the data is output in parallel from the Q0 to Q7 ports.            |
| Pin9 SQH              | It is a serial output pin dedicated for chip cascading to the SI terminal of the next 74HC595.                                                                                                                              |
| Q0--Q7(Pin 15,Pin1-7) | Eight-bit parallel output, can directly control the 8 segments of the digital tube.                                                                                                                                         |

4.  **Circuit Diagram and Wiring Diagram**

![](/media/1738cecf584c83b55370153ebc1688b7.png)

Note: Pay attention to the direction in which the 74HC595N chip is
inserted.

![](/media/a6d03617539b70d6d69fa7e9acb25be9.png)

![](/media/91833532723f4ee623902c0252092741.png)

5.  **Test Code**

The code used in this project is saved in the file KS3026 Keyestudio
Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi
System\\Python\_Tutorial\\2. Projects\\Project 11：74HC595N Control 8
LEDs. You can move the code to anywhere.For example, we save it in the
pi folder of the Raspberry Pi system, the route is home/pi/2. Projects.

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project
11：74HC595N Control 8 LEDs”. Select“my74HC595.py”, right-click and
select“Upload to /”，wait for“my74HC595.py”to be uploaded to the
Raspberry Pi Pico. And double-click
the“Project\_11\_74HC595N\_Controls\_8\_LEDs.py”.

![](/media/2ac6ee416569798a1c50a9d0f3da0cb2.png)

![](/media/48a039f4961237761acbaa6cbbeacba7.png)

<table>
<tbody>
<tr class="odd">
<td><p>#Import time and my74HC595 modules.</p>
<p>from my74HC595 import Chip74HC595</p>
<p>import time</p>
<p>#Create a Chip74HC595 object and configure pins</p>
<p>chip = Chip74HC595(18, 20, 21)</p>
<p>#Chip74HC595() == Chip74HC595(18, 20, 21)</p>
<p>#The first for loop makes LED Bar display separately from left to right</p>
<p>#while the second for loop make it display separately from right to left.</p>
<p>while True:</p>
<p>x = 0x01</p>
<p>for count in range(8):</p>
<p>chip.shiftOut(1, x)</p>
<p>x = x&lt;&lt;1;</p>
<p>time.sleep_ms(300)</p>
<p>x = 0x01</p>
<p>for count in range(8):</p>
<p>chip.shiftOut(0, x)</p>
<p>x = x&lt;&lt;1</p>
<p>time.sleep_ms(300)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](/media/c1b73a6a1a33fc7af94b5487703125d7.png)

Click ![](/media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts
executing, we will see that the 8 LEDs start flashing in flowing water
mode. Press“Ctrl+C”or click![](/media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart
backend”to exit the program.

![](/media/a8284225cd537ee03f3c8ae031f4213b.png)
