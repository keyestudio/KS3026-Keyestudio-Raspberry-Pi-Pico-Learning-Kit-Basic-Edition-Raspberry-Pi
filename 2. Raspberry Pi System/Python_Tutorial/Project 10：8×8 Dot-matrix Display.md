# Project 10：8×8 Dot-matrix Display

1.  **Introduction**

The dot-matrix display is an electronic digital display device that can
show information on machines, clocks and many other devices. In this
project, we will use the Raspberry Pi Pico to control the 8x8 LED dot
matrix to make a“❤”pattern.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:1.03333in;height:1.02708in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td><blockquote>
<p>Jumper Wires</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/d226a1f3c801ac78321f0692143c853e.png" style="width:1.09375in;height:1.05208in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.50347in;height:1.23333in" /></td>
</tr>
<tr class="even">
<td>8*8 Dot-matrix Display *1</td>
<td><blockquote>
<p>220Ω Resistor*8</p>
</blockquote></td>
<td><blockquote>
<p>USB Cable*1</p>
</blockquote></td>
<td>Breadboard*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**8\*8 Dot-matrix display module:**

The 8\*8 dot matrix is composed of 64 LEDs, and each LED is placed at
the intersection of a row and a column. When using a single-chip
microcomputer to drive an 8\*8 dot matrix, we need to use a total of 16
digital ports, which greatly wastes the data of the single-chip
microcomputer. For this reason, we specially designed this module, using
the HT16K33 chip to drive an 8\*8 dot matrix, and only need to use the
I2C communication port of the single-chip microcomputer to control the
dot matrix, which greatly saves the microcontroller resources.

![](/media/69c719a7898907ab32f089f0cbbaff13.png)

![](/media/bcfa2498367eaf9c7733da15af32eae7.png)

4.  **Circuit Diagram and Wiring Diagram**
    
    ![](/media/dc2d64f3098b039937483e04589cbc17.png)
    
    ![](/media/094a47e28b2c735ab475ede10c0deb43.png)
    
    **Test Code**

The code used in this project is saved in the file KS3026 Keyestudio
Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi
System\\Python\_Tutorial\\2. Projects\\Project 10：8×8 Dot-matrix
Display.

You can move the code to anywhere.For example, we save it in the pi
folder of the Raspberry Pi system, the route is home/pi/2. Projects.

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click “This computer”→“home”→“pi”→“2. Projects”→“Project
10：8×8 Dot-matrix Display”.and
double-click“Project\_10\_8×8\_Dot\_Matrix\_Display.py”

![](/media/56f723f2f7f293747d18a4dd06298076.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Define the pin of the row and Set to output</p>
<p>row1 = machine.Pin(18, machine.Pin.OUT)</p>
<p>row2 = machine.Pin(26, machine.Pin.OUT)</p>
<p>row3 = machine.Pin(17, machine.Pin.OUT)</p>
<p>row4 = machine.Pin(21, machine.Pin.OUT)</p>
<p>row5 = machine.Pin(10, machine.Pin.OUT)</p>
<p>row6 = machine.Pin(16, machine.Pin.OUT)</p>
<p>row7 = machine.Pin(11, machine.Pin.OUT)</p>
<p>row8 = machine.Pin(14, machine.Pin.OUT)</p>
<p>#Define the pins of the column and Set to output</p>
<p>col1 = machine.Pin(22, machine.Pin.OUT)</p>
<p>col2 = machine.Pin(12, machine.Pin.OUT)</p>
<p>col3 = machine.Pin(13, machine.Pin.OUT)</p>
<p>col4 = machine.Pin(19, machine.Pin.OUT)</p>
<p>col5 = machine.Pin(15, machine.Pin.OUT)</p>
<p>col6 = machine.Pin(20, machine.Pin.OUT)</p>
<p>col7 = machine.Pin(27, machine.Pin.OUT)</p>
<p>col8 = machine.Pin(28, machine.Pin.OUT)</p>
<p>#Sets the pin of the column to low level</p>
<p>col1.value(0)</p>
<p>col2.value(0)</p>
<p>col3.value(0)</p>
<p>col4.value(0)</p>
<p>col5.value(0)</p>
<p>col6.value(0)</p>
<p>col7.value(0)</p>
<p>col8.value(0)</p>
<p>#Since the column of the lattice has been set to low level,</p>
<p>#the corresponding row of the lattice will light up when the pin of the row is at high level</p>
<p>def Row(d):</p>
<p>if(d ==1):</p>
<p>row1.value(1) #Light the first line</p>
<p>if(d ==2):</p>
<p>row2.value(1) #Light the second line</p>
<p>if(d ==3):</p>
<p>row3.value(1)</p>
<p>if(d ==4):</p>
<p>row4.value(1)</p>
<p>if(d ==5):</p>
<p>row5.value(1)</p>
<p>if(d ==6):</p>
<p>row6.value(1)</p>
<p>if(d ==7):</p>
<p>row7.value(1)</p>
<p>if(d ==8):</p>
<p>row8.value(1)</p>
<p>#Close the lattice</p>
<p>def off():</p>
<p>row1.value(0)</p>
<p>row2.value(0)</p>
<p>row3.value(0)</p>
<p>row4.value(0)</p>
<p>row5.value(0)</p>
<p>row6.value(0)</p>
<p>row7.value(0)</p>
<p>row8.value(0)</p>
<p>try:</p>
<p>print("test...")</p>
<p>while True:</p>
<p>for num in range(1,10): #Light the lattice line by line</p>
<p>Row(num)</p>
<p>if(num == 9): #Because the lattice has only 8 rows, and I'm limiting it here, is equal to 9</p>
<p>off() #Close the lattice</p>
<p>time.sleep(0.2)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the computer,
    click ![](/media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”.
    
    ![](/media/64d11d2a6a0e7c42f7bd9e2481ab7c44.png)
    
    Click ![](/media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts
    executing, we will see that the 8 x 8 dot matrix displays the
    character "A" 1S, "B" 1S, and "C" 1S. Then scroll to display the
    string "Hello
    World”repeatedly. Click![](/media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart
    backend”to exit the program.

![](/media/af164a5db1ee0578a52e289510f7a958.png)
