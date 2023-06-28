# Project 17：Small Fan

### **Introduction**

In the hot summer, we need an electric fan to cool us down, so in this project, we will use the Plus control board to control 130 motor module and small blade to make a small fan.



### **Components Required**

| ![image-20230516144305354](media/image-20230516144305354.png) | ![image-20230516144310388](media/image-20230516144310388.png) | ![image-20230516144320387](media/image-20230516144320387.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Raspberry Pi Pico*1                                          | Raspberry Pi Pico Expansion Board*1                          | DC Motor*1                                                   |
| ![img](media/wps13-168421945343029.jpg)                      | ![img](media/wps14-168421945491730.jpg)                      | ![img](media/wps15-168421945652431.jpg)                      |
| Breadboard*1                                                 | Fan*1                                                        | S8050 Triode*1                                               |
| ![img](media/wps16-168421948090132.jpg)                      | ![img](media/wps17-168421948556433.jpg)                      | ![img](media/wps18-168421948754934.jpg)                      |
| S8550 Triode*1                                               | 1KΩ Resistor*1                                               | Jumper Wires                                                 |
| ![img](media/wps19-168421949141236.jpg)                      | ![img](media/wps20-168421948978835.jpg)                      |                                                              |
| Diode*1                                                      | USB Cable*1                                                  |                                                              |



### **Component Knowledge**

![](media/9197d4aff9356c585b7ef68e33a6881d.png)

**Triode：**

It is referred as the semiconductor triode and a bipolar transistor or a transistor.

The triode is one of the basic semiconductor components as the core of the electronic circuit., which can amplify current. The triode means that two PN junctions are made on a semiconductor wafer. The two PN junctions divide the entire semiconductor into three parts. The middle part is the base area, and the two sides are the emitter and collector areas.

As for NPN triode, it is composed of two N type semiconductors and a P type semiconductor.

The type of transistor which may be used in some applications in place of the triode tube is the "junction" transistor, which actually has two junctions. It has an emitter, base, and collector which correspond to the cathode, grid, and plate, respectively, in the triode tube. Junction transistors are of two types, the NPN type and the PNP type.

The PN junction between the emitting area and the base area is emitter junction and the PN junction flanked by the collector area and the base area is collector junction. And three pins are E（Emitter, B (Base)and C (Collector).

**S8050（NPN triode）**

![](media/3bace56b6d4c5836d1f334038e88acf1.jpeg)

**S8550（PNP triode）**

![](media/3bace56b6d4c5836d1f334038e88acf1.jpeg)

The S8050 transistor is a low-power NPN silicon tube and its the maximum voltage of collector and base can reach 40V and the current of the collector is (Ic) 0.5A.

The pins of the S8050 transistor should facing down, pin 1 is the emitter (E pole), pin 2 is the base (B pole), and pin 3 is the collector (C pole). Similarly, the S8550 transistor is the same.

![](media/1337a16a23745afe86a78bbc628451f7.png)

The commonly used triodes are divided into two types: PNP type triode and NPN type triode. S8550 is the PNP type triode, S8050 is the NPN type triode, what we provide in this kit are S8050 and S8550.

![](media/5642275b2be86782bd9563ee840b0d1a.png)

### **Connection Diagram 1**

we apply the S8050(NPN triode) in this experiment to control the motor

![](media/5db0687f6510b28cf4ccee7aac0d7f93.png)

![](media/319b4a31b0bc9d65d5f10bfcccf051a1.png)

### **Test Code 1**

The code used in this project is saved in the file KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 17：Small Fan. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route isD:\\2. Python Projects.

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 17：Small Fan”. And double left-click the “Project\_17.1\_Small\_Fan.py”.

![](media/4aa25e4118885549e3492c38e729b364.png)

```python
from machine import Pin
import time

motor = Pin(22, Pin.OUT)   # create S8050 object from Pin 22, Set Pin 22 to output

try:
    while True:
        motor.value(1)    # Set motor turn on
        time.sleep(4) # Sleep 4s
        motor.value(0)    # Set motoe turn off
        time.sleep(2) # Sleep 2s
except:
    pass
```



### **Test Result** 1

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/5f875975457fa98892456951e9635ef3.png)

Click “![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that The small fan turns counterclockwise for 4 seconds and stops for 2 seconds, in a loop way. 

Press“Ctrl+C”or click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/9aa0872d67052898982025fb3b2d0f5d.png)

### **Circuit Diagram and Wiring Diagram 2：**

We use the S8550 PNP triode to control a motor

![](media/3c3bfe5083b9b963b78e76c3b8d387db.png)

![](media/08150e9b22904b62ff4b841a8551fbb6.png)

### **Test Code 2**

Go to the folder KS3026 Keyestudio Raspberry Pi Pico Learning Kit Basic Edition\\3. Raspberry Pi System\\Python\_Tutorial\\2. Projects\\Project 17：Small Fan.

You can move the code to anywhere, for example, We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

![](media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 17：Small Fan”. And double left-click the“Project\_17.2\_Small\_Fan.py”.

![](media/be265b1aedadc67d6f42640aca85d63e.png)

```python
from machine import Pin
import time

motor = Pin(22, Pin.OUT)   # create S8550 object from Pin 22, Set Pin 22 to output

try:
    while True:
        motor.value(0)    # Set motor turn on
        time.sleep(4) # Sleep 4s
        motor.value(1)    # Set motoe turn off
        time.sleep(2) # Sleep 2s
except:
    pass
```



### **Test Result 2**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](media/a48592915a0f512794f70e4ae133289c.png)

Click “![](media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that The small fan turns counterclockwise for 4 seconds and stops for 2 seconds, in a loop way. 

Press“Ctrl+C”or click“![](media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](media/365d4ab2c099ef714f92ffa00fcf4336.png)
