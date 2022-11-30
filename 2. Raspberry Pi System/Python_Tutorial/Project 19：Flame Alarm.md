# Project 19：Flame Alarm

1.  **Introduction**
    
    Fire is a terrible thing and fire alarm systems are very useful in
    houses, commercial buildings and factories. In this project, we will
    use a Raspberry Pi Pico to control a flame sensor , a buzzer and
    LEDs to make fire alarm devices, which is a meaningful maker
    activity.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/f70a6a892505b1816d151452b9b995a7.jpeg" style="width:1.55417in;height:0.61875in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/a50ec3e38adf10643eafac8cb62bec8a.png" style="width:0.20278in;height:1.25764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/ef77f5a64c382157fc2dea21ec373fef.png" style="width:0.29514in;height:1.25903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:0.86111in;height:0.70069in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Flame Sensor*1</td>
<td>Red LED*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.59028in;height:1.44583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:0.25833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/b395b1cd2678f87b3a34dec15659efbc.png" style="width:0.22431in;height:1.00556in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Breadboard</td>
<td>220ΩResistor*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
<td>USBCable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
    ![](/media/a50ec3e38adf10643eafac8cb62bec8a.png)

**Flame Sensor**：The flame emits a certain degree of IR light, which is
invisible to the human eye, but our flame sensor can detect it and alert
the microcontroller. If the Raspberry Pi Pico has detected a fire, it
has a specially designed infrared receiver to detect the flame, and then
convert the flame brightness into a fluctuating level signal. The short
pin of the receiving triode is negative pole and the other long pin is
positive pole. We should connect the short pin (negative pole) to 5V and
the long pin (positive pole) to the analog pin, a resistor and GND. As
shown in the figure below.

![](/media/87bd204db523c602c80745266c1ee452.png)

Note: Since vulnerable to radio frequency radiation and temperature
changes, the flame sensor should be kept away from heat sources like
radiators, heaters and air conditioners, as well as direct irradiation
of sunlight, headlights and incandescent light.

4.  **Read the Simulation Value**

We start with a simple code to read the value of the flame sensor and
print it on the serial monitor. For wiring, please refer to the
following wiring diagram.

![](/media/85531078db041bba05599b3a1118a7bc.png)

![](/media/1e3c424f7cc7ac797ab0b8ae4a00f4f1.png)

The code used in this project is saved in the file KS3026 Keyestudio
Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi
System\\Python\_Tutorial\\2. Projects\\Project 19：Flame Alarm.

You can move the code anywhere. We save the code to the pi folder of the
Raspberry Pi system. The path:home/pi/2. Projects

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→”Project
19：Flame Alarm”. And double left-click
the“Project\_19.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](/media/f566b02fa7abceb8c609fa961f94ebf7.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the flame sensor to pin 26 (ADC function)</p>
<p>adc = ADC(26)</p>
<p># Read the current analog value of the flame sensor and return [0, 1023]</p>
<p>def get_value():</p>
<p>return int(adc.read_u16() * 1024 / 65536)</p>
<p># Print the current value of the flame sensor cyclically, value=[0, 1023]</p>
<p>while True:</p>
<p>value = get_value()</p>
<p>print(value)</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“![](/media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](/media/7bb44e167d87bdb821315bf809cf8036.png)

Click ![](/media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts
executing, we will see that the "Shell" window of Thonny IDE will print
the simulation value read by the flame sensor. When the flame is close
to the sensor, the simulation value increases. On the contrary, the
simulated value decreases. Press“![](/media/ec00367ea605788eab454cd176b94c7b.png)Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/a5bb49291add50b4016c8215ae6b698d.png)

![](/media/7c04b9dd8c4a10e7b9788ecd95eeeeaa.png)

5.  **Circuit Diagram and Wiring Diagram**

Next, we will use flame sensor and buzzer, an RGB LED to make an
interesting project, that is flame alarm. When flame is detected, RGB
LED is red and buzzer alarms.

![](/media/c2b7feb8039e618ba070a9714ef06554.png)

![](/media/0cd1ee17a6f8de81464817090c5832eb.png)

6.  **Test Code**
    
    Note：![](/media/40a3ea572836945268b22dfc0cce29c3.png) The threshold of 500 in the code can be
    reset itself as required

Go to the folder KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic
Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project
19：Flame Alarm.

You can move the code anywhere. We save the code to the pi folder of the
Raspberry Pi system. The path:home/pi/2. Projects

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→Project
19：Flame Alarm”. And double left-click
the“Project\_19.2\_Flame\_Alarm.py”.

![](/media/96fac91877005bf6b06ad3e43bec025e.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the flame sensor to pin 26 (ADC function)</p>
<p>adc = ADC(26)</p>
<p># create LED object from Pin 16,Set Pin 16 to output</p>
<p>led = Pin(16, Pin.OUT)</p>
<p># create buzzer object from Pin 17, Set Pin 17 to output</p>
<p>buzzer = Pin(17, Pin.OUT)</p>
<p># Read the current analog value of the flame sensor and return [0, 1023]</p>
<p>def get_value():</p>
<p>return int(adc.read_u16() * 1024 / 65536)</p>
<p># If the flame sensor detects a flame, the buzzer will beep</p>
<p># and the LED will blink when the analog value is greater than 500</p>
<p># Otherwise, the buzzer does not sound and the LED goes off</p>
<p>while True:</p>
<p>value = get_value()</p>
<p>if value &gt;500:</p>
<p>buzzer.value(1) # Set buzzer turn on</p>
<p>led.value(1) # Set led turn on</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>led.value(0) # Set led turn off</p>
<p>time.sleep(0.5) # Sleep 0.5s</p>
<p>else:</p>
<p>buzzer.value(0) # Set buzzer turn off</p>
<p>led.value(0) # Set led turn off</p></td>
</tr>
</tbody>
</table>

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the
computer，click“![](/media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](/media/0c1eb4ac2520b87b4cdae31f89188d14.png)

Click“![](/media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts
executing, we will see that when the flame sensor detects the flame, the
LED flashes and the buzzer alarms. Otherwise, the LED does not light,
the buzzer does not sound. Click“![](/media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart
backend”to exit the program.

![](/media/158932123b144f9b09e64b05b38bf139.png)
