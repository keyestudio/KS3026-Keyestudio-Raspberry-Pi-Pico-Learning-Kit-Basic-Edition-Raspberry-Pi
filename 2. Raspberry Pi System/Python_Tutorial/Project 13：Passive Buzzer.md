# Project 13：Passive Buzzer

**Introduction**

In a previous project, we have learned an active buzzer, which can only
produce one sound and may let you feel monotonous. In this project, we
will learn a passive buzzer and use the Raspberry Pi Pico to control the
passive buzzer to sound an alarm. Unlike the active buzzer, the passive
buzzer can emit sounds of different frequencies.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi PicoExpansion Board*1</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/d1ea1bb2b2749820cab389d5b85b838b.png" style="width:0.66181in;height:0.79444in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.69375in;height:1.70139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.77778in;height:0.74792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3026-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Basic-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Passive Buzzer*1</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

**3.Component Knowledge**

![](/media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal
vibration source. It must be driven by 2K to 5K square wave, not a DC
signal. The two buzzers are very similar in appearance, but one buzzer
with a green circuit board is a passive buzzer, while the other with
black tape is an active buzzer. Passive buzzers cannot distinguish
between positive polarity while active buzzers can.

![](/media/fc42c5ed014609ff0b290ee5361bb2fd.png)

**4. Circuit Diagram and Wiring Diagram**

![](/media/e0da1ccdbff24d256db130816c55da74.png)

![](/media/e601e48f8deddb3e9e7734d0022106b3.png)

5.  **Test Code**
    
    The code used in this project is saved in the file KS3026 Keyestudio
    Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi
    System\\Python\_Tutorial\\2. Projects\\Project 13：Passive Buzzer.
    You can move the code anywhere. We save the code to the pi folder of
    the Raspberry Pi system. The path:home/pi/2. Projects

![](/media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“2. Projects”→“Project
13：Passive Buzzer”. And double left-click
the“Project\_13\_Passive\_Buzzer.py”.

![](/media/0ae6aecf5d0df477745a223e743a1362.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Initialize the passive buzzer</p>
<p>buzzer = Pin(16,Pin.OUT)</p>
<p>#Simulate two different frequencies</p>
<p>while True:</p>
<p>#Output 500HZ frequency sound</p>
<p>for i in range(80):</p>
<p>buzzer.value(1)</p>
<p>time.sleep(0.001)</p>
<p>buzzer.value(0)</p>
<p>time.sleep(0.001)</p>
<p>#Output 250HZ frequency sound</p>
<p>for i in range(100):</p>
<p>buzzer.value(1)</p>
<p>time.sleep(0.002)</p>
<p>buzzer.value(0)</p>
<p>time.sleep(0.002)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.
    
    ![](/media/768c2e41ce5b5cc212a79538d77fc815.png)
    
    Click ![](/media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts
    executing, we will see that the the passive buzzer sounds the alarm.
    Click ![](/media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the
    program.
    
    ![](/media/6d7aeb45a390b49d5852638137dff2b4.png)
