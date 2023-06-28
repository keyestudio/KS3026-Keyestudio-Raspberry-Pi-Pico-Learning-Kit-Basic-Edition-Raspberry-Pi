# Preparation before class for Python

Raspberry Pi is a card computer whose official system is Raspberry Pi OS, and can be installed on the Raspberry Pi, such as: ubuntu, Windows IoT. Raspberry Pi can be used as a personal server, performing camera monitoring and recognition, as well as voice interaction by connecting a camera and a voice interactive assistant. 

Also, Raspberry Pi leads out 40Pin pins that can be connected to various sensors and control LEDs, motors, etc. This can be used to make a robot with a Raspberry Pi.



## 1. Tools needed for the Raspberry Pi system

**Hardware Tool:**

  - Raspberry Pi 4B/3B/2B

  - Above 16G TFT Memory Card

  - Card Reader

  - Computer and other parts

### 1.1 Install Software Tools

**Windows System:**

(1)**Putty**

Download link:
[<span class="underline">https://www.chiark.greenend.org.uk/\~sgtatham/putty/</span>](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

![](/media/c26be4cd1f5543f20f275556ce5892c0.png)

![](/media/d888918aa7bf9e5ea94597aad1ee4224.png)



1.  After downloading the package file ![](/media/e597704d7033c7c3c5da06d4f561822c.png), double-click it and tap “Next”.
    
    ![](/media/01f1b2d98915be2be9c0c2a3d330dde2.png)
    
2.  Click “Next”.
    
    ![](/media/bd698753a8eea7a2ff5c5e0e598cbd94.png)

3.  Choose “Install PuTTY files” and click “Install”.
    
    ![](/media/071a0acc98bb2dc5cd45d85dec72d111.png)

4.  After a few seconds, click "Finish".
    
    ![](/media/ec368c3a549c09edd70f9786456d5430.png)

**SSH Remote Login software -WinSCP**

Link:
[<span class="underline">https://winscp.net/eng/download.php</span>](https://winscp.net/eng/download.php)

1.  After downloading the package file![](/media/1719daa1002d7477ad4700e1df85d2df.png), click<img src="/media/e09e48a32781d08aabb06156efe1de49.png" style="zoom:80%;" />.
    
    ![](/media/5ee80ade909fe3eb73dc9535704b4c0b.png)
    
2.  Click “Accept”.

![](/media/9c652f54f6a7d53f6b2aedba40104a00.png)

![](/media/f32891714d5966037d59d1812aa15686.png)

![](/media/57d6139ba0aac9ca996bcbe6f6fd218f.png)

![](/media/49ffed878ee84546b156af3a0bf5556e.png)

![](/media/14ffa1e11243835d30ffb933219dcef5.png)

Download link:

[<span class="underline">http://www.canadiancontent.net/tech/download/SD\_Card\_Formatter.html</span>](http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html)

![](/media/fa229f4e063572ce1c59574c308bf452.png)

![](/media/ac5d5eb9463805484b9239b99faf04eb.png)

1.  Unzip the SDCardFormatterv5\_WinEN package, double-click![](/media/8c6f8da97bf702080a8e302db2e9f982.png) to run it.
    
    ![](/media/046c67e4072093ee3dad27e8088fcf9f.png)
    
    ![](/media/384203e0b54ddfe37f18b65f70e786e5.png)
    
    ![](/media/cf4e91eac0c0573cff282256a915a01a.png)
    
2.  Click “Next” and “Install”.
    
    ![](/media/0af58ee3afb14005a884ca2dc941157f.png)
    
    ![](/media/807623ddeea20c8b61503845d8aec9bc.png)

3.  After a few seconds, click "Finish".
    
    ![](/media/df2deb7e04c25ee207e994f0d2808194.png)
    
    ##### **Win32DiskImager**
    
    Download：http://www.nirsoft.net/utils/wnetwatcher.zip
    
    
### 1.2 Raspberry Pi Imager

Download link for **the latest version**:

[<span class="underline">https://www.raspberrypi.org/downloads/raspberry-pi-os/</span>](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

**Old version**：

Raspbian：<span class="underline">https://downloads.raspberrypi.org/raspbian/images/</span>

Raspbian full：<span class="underline">https://downloads.raspberrypi.org/raspbian_full/images/</span>

Raspbian lite：https://downloads.raspberrypi.org/raspbian_lite/images/

We use the 2020.05.28 version in the tutorial and recommend you to use this version

(Please download this version as shown in the picture below.)

<https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/>

![](/media/857946c171dd1f5617a0cbbdd2608baf.png)



## 2. Install Raspberry Pi OS on Raspberry Pi 4B

Interface the TFT memory card with a card reader, then plug the card reader into a computer’s USB port.

Use the SD Card Formatter to format a TFT memory card, as illustrated below.

![](/media/79d747e6f00f857a593b3327397cc44f.png)

![](/media/cbc55902de71ce984d873ca2cb67fffa.png)

![](/media/82031b5354cc4edeccf2bfa7465b7c6c.png)

#### **Burn system**

Burn the Raspberry Pi OS to the TFT memory card using Win32DiskImager software.

![](/media/80d236cae8bdf63d80dc65048ffb52b3.png)

![](/media/243d1ef34211eafe1a92b67fc0ee85a2.png)

![](/media/ea854c476e9a8d4f82dd4a7c714cd5af.png)

Don’t eject card reader after burning mirror system, build a file named SSH, then delete .txt.

The SSH login function can be activated by copying SSH file to boot category, as shown below.

![](/media/ffb73310322accd671da373bb2e71945.png)

Eject card reader.

#### **Log in system**

(Raspberry and PC should be in the same local area network.)

Insert TFT memory card into Raspberry Pi, connect internet cable and plug in power. If you have screen and HDMI cable of Raspberry Pi, you could view Raspberry Pi OS activating. If not, you can enter the desktop of Raspberry Pi via SSH remote login software---WinSCP andxrdp.

#### **Remote login**

**Enter default user name, password and host name on WinSCP to log in. Only a Raspberry Pi is connected in same network.**

![](/media/0a41d5c629ec98afbc31dc47ff5c18ec.png)

![](/media/ff64e71b9e30df60d0b099dbc2532587.png)

#### **Check IP and mac address**

![](/media/a4285a452978026c9e60c31d35974315.png)

Click to open terminal and input the password: raspberry, and press“Enter”on keyboard.

![](/media/a433a9ee584c821a702d0250937e2ba8.png)

![](/media/7fb10d842cc7fd824a325d30fc3ecdc7.png)

Logging in successfully, open the terminal, input **ip a** and tap“Enter”to check IP and mac address.

![](/media/132e9ab754a0f63e38b3e4cfbc3679f2.png)

From the above figure, mac address of this Raspberry Pi is a6:32:17:61:9c, and IP address is 192.168.1.128(use IP address to finish xrdp remote login).

Since mac address never changes, you could confirm IP via mac address when not sure which IP it is.

#### **Fix IP address of Raspberry Pi**

IP address is changeable, therefore, we need to make IP address fixed for convenient use.

Follow the below steps:

Switch to root user

If without root user’s password

① Set root password

Input password in the terminal: sudo passwd root to set password.

② Switch to root user

su root

③ Fix the configuration file of IP address

Firstly change IP address of the following configuration file.

(\#New IP address: address 192.168.1.99)

Copy the above new address to terminal and press“Enter”.

Configuration File**:**

echo -e '

auto eth0

iface eth0 inet static

\#Change IP address

address 192.168.1.99

netmask 255.255.255.0

gateway 192.168.1.1

network 192.168.1.0

broadcast 192.168.1.255

dns-domain 119.29.29.29

dns-nameservers 119.29.29.29

metric 0

mtu 1492

'\>/etc/network/interfaces.d/eth0

As shown below:

![](/media/a68a4f59d4d364efa28b6680a2c48d43.png)

④ Reboot the system to activate the configuration file.

Input the restart command in the terminal: sudo reboot

You could log in via fixed IP afterwards.

⑤ Check IP and insure IP address fixed well.

![](/media/b4313e2d78a4289705c658a1ebbc962b.png)

(6) Log in desktop on Raspberry Pi wirelessly

In fact, we can log in desktop on Raspberry Pi wirelessly even without screen and HDMI cable.

VNC and Xrdp are commonly used to log in desktop of Raspberry Pi wirelessly. Let’s take example of Xrdp.

Install Xrdp Service in the terminal

Installation commands:

Switch to Root User: su root

Installation: apt-get install xrdp

Enter y and press“Enter”.

As shown below:

![](/media/aa59941ff4c1e582e8183c1dc3767fce.png)

Open the remote desktop connection on Windows

Press WIN+R on keyboard and enter mstsc.exe.

As shown below:

![](/media/e5a66a3a1c998f8feb1c21c7a457ec4e.png)

Input IP address of Raspberry Pi, as shown below.

Click“Connect”and tap“Connect”.

192.168.1.99 is IP address we use, you could change into your IP address.

![](/media/c41c66bea61b30019e02a74b483af700.png)

Click“Yes”.

![](/media/297813f1370ce5c158fac61511f61295.png)

Input user name: pi, default password: raspberry, as shown below.

![](/media/251fddc1decc15d0b69f8a0c7467d5c1.png)

Click“OK”or“Enter”, you will view the desktop of Raspberry Pi OS, as shown below.

![](/media/56bd5693edd484c4433dc438b58c6130.png)

Now, we finish the basic configuration of Raspberry Pi OS.

## 3.Preparations for Python

Python is a programming language that lets you work more quickly and integrate your systems more effectively.

Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Next to pick up Python to control 40 pin of Raspberry Pi.

#### Hardware：

| **Raspberry Pi 4B**     | **Raspberry Pi 4B Model** |
| :---------------------: | :-----------------------: |
| ![image-20230425081935044](media/image-20230425081935044.png) |![image-20230425081939356](media/image-20230425081939356.png)|

#### **Hardware Interfaces：**

![](/media/d232a87d73f7426894a6cafed80521a0.png)

#### **40-Pin GPIO Header Description：**

GPIO pins are divided into BCM GPIO number, physics number and WiringPi GPIO number.

We usually use WiringPi GPIO when using C language and BCM GPIO and physics number are used to Python, as shown below;

In these lessons, we use Python, so BCM GPIO number is adopted.

![](/media/ca74a57f9eb9086f102688bf043e49fd.png)

Note: pin(3.3 V) on the left hand is square, but other pins are round. Turn Raspberry Pi over, there is a square GPIO on the back.(you could tell from pin(3.3V).

![](/media/86a686aad06cfe7563e7a01456e2cb7a.jpeg)

Note: the largest current of each pin on Raspberry Pi 4B is 16mA and the aggregate current of all pins is not less than 51mA.

#### Copy Example Code Folder to Raspberry Pi：

Place example code folder to the pi folder of Raspberry Pi. and extract the example code from **Projects.zip** file, as shown below:

![](/media/e7b577a013d27250449f6a6062f2a692.png)

![](/media/5f4f542cedf657c9cdf83c8fcc9b4b91.png)

![](/media/6721cea2e1524674a8732217b3f998ac.png)

Double-click pythonCode\_A to check py files.

![](/media/fbf63c5b42b99c080e5be93603e1facb.png)



## 4.Python

#### **Update the firmware of Micropython**

If you want to run the MicroPython on the Pi Pico board, you need to upload a firmware to the pico board.

You can program via C language or MicroPython on the pico board. But you need to download the MicroPython firmware.

Note: 

MicroPython firmware is required to be downloaded once. You don’t need to download it again when programming with MicroPython. 

If you have downloaded the .uf2 program firmware written in C language, the MicroPython firmware will be overwritten, so next time you use MicroPython, you need to follow the steps below to update the Raspberry Pi Pico's firmware.



#### **Download the firmward of Micropython**

**Method 1**: 

Click ![](/media/e1e5a14737d3f99726202e22e731d506.png)to enter the website：[<span class="underline">https://www.raspberrypi.com/documentation/microcontrollers/</span>](https://www.raspberrypi.com/documentation/microcontrollers/)

![](/media/3b3e6a639416b76c44f2a0854dc451cc.png)

![](/media/5d04d67506852588d126ce760739a3c5.png)

Click “**MicroPython(**Getting started MicroPython**)**” to go to the firmware download page.

![](/media/137e21851df02502fb989d8541fa0da8.png)

**Method 2**：

Click![](/media/e1e5a14737d3f99726202e22e731d506.png)to open the browser，click [<span class="underline">https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2</span>](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2) to download the firmware

Note：

transfer the firmware（rp2-pico-20210902-v1.17.uf2）to the desktop of Raspberry pi imager



#### **Program the firmware of MicroPython**

Connect a microUSB cable to the USB port of the pico board.

Hold down **BOOTSEL**

![](/media/33c91d51b2aeb2c943691706354aaad1.png)

Release the button, then there pops up a page.

Enter raspberry in the Password box, click OK.

The drive RPI-RP2 will appear on the desktop of the Raspberry Pi imager

Note：

The latest Raspberry Pi mirroring system will not display the following dialog box, and the old version will display the following dialog box

![](/media/57aa727673e02ed5cc889c8669c587f2.png)

![](/media/6e6c11ffed92c2ae8307044bb19ef4dc.png)

Click **OK** and open drive(RPI-RP2). Copy the file（rp2-pico-20210902-v1.17.uf2）to the RPI-RP2

![](/media/9cc833c1f1a30f7dc03dbf3704bb8078.png)

![](/media/39b8a265056f4a28d55ba3aba3bbae33.png)

After the firmware is programmed, the Pico board will reboot. Then you can run Micropython

**Serial Ports**

The MicroPython firmware is equipped with a virtual USB serial port which is accessed through the micro USB connector on Raspberry Pi Pico.

Your computer should notice this serial port and list it as a character device, most likely /dev/ttyACM0.

You can run ls /dev/tty\* to list your serial ports. There may be quite a few, but MicroPython’s USB serial will start with /dev/ttyACM. If in doubt, unplug the micro USB connector and see which one disappears. If you don’t see anything, you can try rebooting your Raspberry Pi.

Enter the following command to install minicom:

sudo apt install minicom

![](/media/76bae15ef182b33d6a7b4d8b03d65475.png)

Select Y

![](/media/b3d8daaf8399339b323c84b3c56f9306.png)

Enter the following commander, press **Enter** and open minicom

minicom -o -D /dev/ttyACM0

![](/media/69b6047c7ba379310c76fcd52985d73f.png)

![](/media/0477b4ed6ddd221558d39de98d232f9d.png)

Press Ctrl + B

![](/media/eedefa717220824a6ef39d944aaf8e5e.png)

Enter print("Hello World") at the terminal and press Enter，then **Hello World** will be displayed.

![](/media/fc41b356fd7081524dccb490ce9a3259.png)

#### **Install Thonny**

The Raspberry Pi Imager that we downloaded comes with some commonly used software, and Thonny is among them.

![](/media/0d1bd2cf2c99d19959684424c425c6ce.png)

If the Raspberry Pi Imager does not have Thonny, you need to manually download it yourself. Enter the following command in the terminal to download and install Thonny.

sudo apt install thonny

![](/media/abf9b407362422678af8eb0fd1b49684.png)

Open Thonny, click“**Switch to regular mode**”to switch modes, and click OK to reopen the Thonny.

![](/media/08a1b220328ad8b9c071741ea46fdb25.png)

![](/media/31139bbd6173717bb10421de36cf1334.png)

#### **Connect the Raspberry Pi Pico on the Thonny**

Click“Python3.9.2”and select“MicroPython(Raspberry Pi Pico)”

![](/media/00ae7e7e6e18b5610b71e4186311c84a.png)

![](/media/3bfbbdcd940252fbdf399ff0de47dea2.png)

Click“Tools”→“Options...”

![](/media/c98465fe869c72654adb035aceaaf83e.png)

Select“Micropython (generic)”or “Micropython (Raspberry Pi Pico).

How to choose Micropython(Raspberry Pi Pico)? As shown below;

![](/media/2a698bf071942ac19ccb5eaa9fada66e.png)

Click“Port”to select corresponding port and click OK

![](/media/e72a434210946d6f9c981128e7f1195e.png)

![](/media/bb18e9e6d072469b230a06926dd5a3cc.png)

Click“**View**”→“**Files**”, then“This computer” and Raspberry Pi Pico” will appear

![](/media/69e6ee6703f190b059bf8eb4902ee637.png)

![](/media/9388fd552f625574f9a77c1c855867c2.png)

![](/media/5ef0b1e392c2e8f1ffc375bc966da812.png)

![](/media/7f98556c0fa277c215058ec2c4a14b3a.png)

#### **Test Code**

Test the Shell commander

Enter“**print(Hello World\!)**”in the Shell and press **Enter**”

![](/media/77c268003ff676b5d6c3baab9b2ebef3.png)

#### **Online running：**

To run Raspberry Pi Pico online, we need to connect the Raspberry Pi Pico to our computer, which allows us to compile or debug programs using Thonny software.  

**Advantages**: you can compile or debug programs using Thonny software.  

Through the "Shell" window, we can view the error information and output results generated during the operation of the program, and query related function information online to help improve the program.  

**Disadvantages**: To run Raspberry Pi Pico online, you must connect Raspberry Pi Pico to a computer and run it with Thonny software.  

If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  



**basic operation:**

Open Thonny and click ![](/media/e776b2c874ac9c5d852212383b3cec27.png)“**Open...**”

![](/media/d275ff88709c9e660a68545cdf1a1b4a.png)

Click“**This computer**”

![](/media/f419da64013966003b63315c70bd88ad.png)

Enter home/pi/2.Projects/Project 01: Hello World to select **Project\_01\_HelloWorld.py and click OK**

![](/media/03b115c1a39fcde581112f86a47fdb87.png)

Click ![](/media/0e4d02d37292e9d2c208b6b8bcde4f21.png)“**Run current script to program Hello World\!.** "**Welcome Keyestudio**" will be displayed on the **Shell**

![](/media/e1aafe9ff0bfa4214e56f682d653ff07.png)

**Exit online**

When running online, click **“**![](/media/92a50d0579b5d50ea659a6b8930da44a.png)Stop /Restart Backend**”** on Thonny to exit the program.  

![](/media/5d0aa92074c5aebbcb37c0638ab308f0.png)



#### **Offline running**:

When running offline, the Raspberry Pi Pico doesn't need to connect to a computer and Thonny. Once powered up, it can run the main.pyprogram stored in the Raspberry Pi Pico.  

**Pros**: We don't need to connect a computer to Thonny's software to run the program.  

**Cons**: The program stops automatically when an error occurs or the Raspberry Pi Pico runs out of power, and the code is hard to change.

**Basic Operation:**

Once powered up, the Raspberry Pi Pico will  check for the presence of main.py on the device automatically. If so, run the program in main.py and go to the shell command system. (If we want the code to run offline, we can save it as main.py); If the main.py does not exist, go directly to the shell command system.   

Click “File”→“New”, create and write code.

![](/media/7a6988dfff80ecb0479e3e878ccde171.png)

Enter the code in the newly opened file. Here we use the Project\_02\_Onboard\_LED\_Flashing. Py code as an example.  

![](/media/9a7d7e35504c9f750e4a58eccd38e094.png)

Click“**Save**”on the menu bar, we can save the code in This computer or MicroPython device.

![](/media/3f7945cc8586bb85aa7bc24c480fd012.png)



Select“MicroPython device”，enter“main.py”in the new pop-up window and click“OK”.

![](/media/0f5f516143bdb28bdcb62bad6784729d.png)

![](/media/c789c476ad5d517082b9c992ea365080.png)

![](/media/78a529ec66e2726b93dee1434e790554.png)

Disconnect the microUSB cable to the Raspberry Pi Pico and reconnect, and the LEDs on the Raspberry Pi Pico will  flash repeatedly. 

![](/media/529c3be102eb7414ac1e5e66fb203b6e.png)

**Exit from Offline operation**

Connect Raspberry Pi Pico to the computer，click“Stop/Restart backend”on Thonny to end the offline operation.  

![](/media/1de7ccf1eee2c1acc908a70fa151774d.png)

If it does’t work, click“Stop/Restart backend”on Thonny several times or reconnect to the Raspberry Pi Pico.

![](/media/3abb1b4a1e2e600d06f76735cfe1c522.png)

We provide a main.py file to run offline.  The code added to main.py is the bootstrap that executes the user code file. We just need to upload the offline project's code file (.py) to the "MicroPython Device".

Move the folder 2.Projects to the folder home/pi of Raspberry Pi system and open Thonny

![](/media/aa2f0b276daa0dbffb031744c3083747.png)

Expand Project 00 : main in Disk(D) directory D:\\2. Python Projects. Double-click **main.py** to make the code in **"**MicroPython Device" run offline.  

![](/media/476b7d201f06b4f2a8d6479677e389bc.png)

Here, we use project 00 and Project 02 cases as examples.  

The results are displayed using an LED(GP25 pin) on a Raspberry Pi Pico.  If we have modified the Project\_02\_Onboard\_LED\_Flashing. Py file, then we need to modify it accordingly. 

Right-click the Project\_02\_Onboard\_LED\_Flashing. Py file and select **'**Upload to/' to upload the code to Raspberry Pi Pico, as shown below.  

![](/media/2d1b1056c12d938570df999d8136b74b.png)

Upload the main.py in the same way

![](/media/bf2c18b6154ce77b2c449b9b9cdb5a76.png)

Disconnect and reconnect the microUSB cable to the Raspberry Pi Pico, and the LEDs will flash repeatedly .

![](/media/529c3be102eb7414ac1e5e66fb203b6e.png)

Note:

The code here runs offline.  If we want to stop running offline and go to "Shell", simply click "![](/media/0b9cf6411531d005d760df16819813e3.png)Stop/Restart Backend" on Thonny software.

![](/media/c3dab4ada7b2e618d6278c570b9b1955.png)



#### **Thonny common operations**

**Upload the code to Raspberry Pi Pico**

In the Project 01：Hello World file, right-click and select Project\_01\_HelloWorld.py，select“**Upload to /**”and upload the code to the root directory of the Raspberry Pi Pico.

![](/media/77c723c6c821dce154aecf2d7b5f1581.png)

**Download the code to the computer**

In the“**MicroPython device**”, right-click and select Project\_01\_HelloWorld.py，select“**Download to ...**”to download the code to our computer.

![](/media/f0ed82cf3717041f02d12958c6209171.png)

**Delete the files in the Raspberry Pi Pico root directory**

In the“**MicroPython device**”，right-click and select Project\_01\_HelloWorld.py，select“**Delete”**，delete the Project\_01\_HelloWorld.py from the Raspberry Pi Pico root directory.

![](/media/82158486bd8db01e825cfe907c60204b.png)

**Delete files from the computer's directory**

In the Project\_01 : Hello World file, right-click and select Project\_01\_HelloWorld.py，select“**Move to Recycle Bin**”，then it can be deleted from the Project\_01\_HelloWorld file.

![](/media/7fc1a7b93f57fe8994e3ab0d429ffc1f.png)

**Create and Save Code**

Click“**File**”→“**New**”to create and compile code.

![](/media/373922a344188cda87b797b0ad639522.png)

Enter code in the newly opened file, here we use Project\_02\_Onboard\_LED\_Flashing.py code as an example.

![](/media/9a7d7e35504c9f750e4a58eccd38e094.png)

Click“**Save**”，and we can save the code to our computer or the Raspberry Pi Pico.

![](/media/3f7945cc8586bb85aa7bc24c480fd012.png)

Select“**MicroPython device**”，enter“**main.py**”in the new pop-up window and click“**OK**”.

![](/media/0f5f516143bdb28bdcb62bad6784729d.png)

![](/media/c789c476ad5d517082b9c992ea365080.png)

We can see the code has been uploaded to the Raspberry Pi Pico.

![](/media/78a529ec66e2726b93dee1434e790554.png)

Click“**Run current script**”, the LED on the Raspberry Pi Pico will flash periodically.

![](/media/88c2dc64c5f38600d8ef7180ea8a7b30.png)
