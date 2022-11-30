from machine import Pin
import time

#Define the pin of the row and Set to output
row1 = machine.Pin(18, machine.Pin.OUT)
row2 = machine.Pin(26, machine.Pin.OUT)
row3 = machine.Pin(17, machine.Pin.OUT)
row4 = machine.Pin(21, machine.Pin.OUT)
row5 = machine.Pin(10, machine.Pin.OUT)
row6 = machine.Pin(16, machine.Pin.OUT)
row7 = machine.Pin(11, machine.Pin.OUT)
row8 = machine.Pin(14, machine.Pin.OUT)
#Define the pins of the column and Set to output
col1 = machine.Pin(22, machine.Pin.OUT)
col2 = machine.Pin(12, machine.Pin.OUT)
col3 = machine.Pin(13, machine.Pin.OUT)
col4 = machine.Pin(19, machine.Pin.OUT)
col5 = machine.Pin(15, machine.Pin.OUT)
col6 = machine.Pin(20, machine.Pin.OUT)
col7 = machine.Pin(27, machine.Pin.OUT)
col8 = machine.Pin(28, machine.Pin.OUT)

#Sets the pin of the column to low level
col1.value(0)
col2.value(0)
col3.value(0)
col4.value(0)
col5.value(0)
col6.value(0)
col7.value(0)
col8.value(0)

#Since the column of the lattice has been set to low level, 
#the corresponding row of the lattice will light up when the pin of the row is at high level
def Row(d):
    if(d ==1):
        row1.value(1)  #Light the first line
    if(d ==2):
        row2.value(1)  #Light the second line
    if(d ==3):
        row3.value(1)
    if(d ==4):
        row4.value(1)
    if(d ==5):
        row5.value(1)
    if(d ==6):
        row6.value(1)
    if(d ==7):
        row7.value(1)
    if(d ==8):
        row8.value(1)
    
#Close the lattice
def off():
    row1.value(0)
    row2.value(0)
    row3.value(0)
    row4.value(0)
    row5.value(0)
    row6.value(0)
    row7.value(0)
    row8.value(0) 

try:
    print("test...")
    while True:
         for num in range(1,10):  #Light the lattice line by line
             Row(num)
             if(num == 9):  #Because the lattice has only 8 rows, and I'm limiting it here, is equal to 9
                off()      #Close the lattice
             time.sleep(0.2)

except:
    pass