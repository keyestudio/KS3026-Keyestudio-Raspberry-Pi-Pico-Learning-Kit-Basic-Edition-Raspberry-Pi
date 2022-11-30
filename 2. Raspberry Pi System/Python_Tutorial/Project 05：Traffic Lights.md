# Project 05：Traffic Lights

1.  **Introduction**

Traffic lights are closely related to people's daily lives, which
generally show red, yellow, and green. Everyone should obey the traffic
rules, which can avoid many traffic accidents. In this project, we will
use Raspberry Pi Pico and some LEDs (red, green and yellow) to simulate
the traffic lights.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.07986in;height:0.82778in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/afa6edd3ff90b027a6f43995a6fb15a2.png" style="width:0.28333in;height:1.20972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/0c1b0f91b4e56bcbc235d06b48809ac9.png" style="width:0.27986in;height:1.22222in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td>Red LED*1</td>
<td>Yellow LED*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/6c688493b558ed5f3e90e7dab38cbd93.png" style="width:0.26736in;height:1.16389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/b57b4057770f0bcc43f037c0ab8e1c41.png" style="width:0.44444in;height:1.17361in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.66736in;height:0.64097in" /></td>
</tr>
<tr class="even">
<td>Green LED*1</td>
<td>USB Cable*1</td>
<td>220ΩResistor*3</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
</tr>
</tbody>
</table>

3.  **Circuit Diagram and Wiring Diagram**

![](/media/4cf2ad735b0df82d62a5fcdb19ebf3c0.png)

![](/media/98f9db025163638c33095cbd16abe7e7.png)

Note:

How to connect an LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

4.  **Test Code**

The code used in this project is saved in the file KS3026 Keyestudio
Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi
System\\Python\_Tutorial\\2. Projects\\Project 05:Traffic Lights. You
can move the code to anywhere.For example, we save it in the oi folder
of the Raspberry Pi system, the route is home/pi/2. Projects.

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“2. Projects”→"Project 05:
Traffic Lights”. And double-click“Project\_05\_Traffic\_Lights.py”.

![](/media/bb44b31699957a99ec3e33f7a887e1be.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>led_red = machine.Pin(16, machine.Pin.OUT) # create red led object from Pin 16, Set Pin 16 to output</p>
<p>led_yellow = machine.Pin(17, machine.Pin.OUT) # create yellow led object from Pin 17, Set Pin 17 to output</p>
<p>led_green = machine.Pin(18, machine.Pin.OUT) # create green led object from Pin 18, Set Pin 18 to output</p>
<p>while True:</p>
<p>led_red.value(1) # Set red led turn on</p>
<p>time.sleep(5) # Sleep 5s</p>
<p>led_red.value(0) # Set red led turn off</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(1)</p>
<p>time.sleep(0.5)</p>
<p>led_yellow.value(0)</p>
<p>time.sleep(0.5)</p>
<p>led_green.value(1)</p>
<p>time.sleep(5)</p>
<p>led_green.value(0)</p></td>
</tr>
</tbody>
</table>

**Test Result：**

Connect the pico board to the Raspberry Pi. Click
![](/media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](/media/3691a51f61750b1dc918de0f771a5482.png)

Click“![](/media/bb4d9305714a178069d277b20e0934b7.png)”, the code starts executing, what we will
see are below:

1.  First, the green light will be on for 5 seconds and then off; 

2.  Next, the yellow light blinks three times and then goes off. 

3.  Then, the red light goes on for five seconds and then goes off. 
    
    Repeat steps 1 to 3 above and press“Ctrl+C”or
    click“![](/media/ec00367ea605788eab454cd176b94c7b.png)” to exit the program.

![](/media/5da95e477cc75ec61a63e001cd7e6a58.png)
