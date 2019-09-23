import serial
import time
ser=serial.Serial('/dev/ttyUSB0',9600,timeout=0)

connected = False


while not connected:
    ser.write('#)')
    time.sleep(0.1)
    print("Sent")
    if ser.read()is '#':
        print("Received")
        connected=True

f=open("lifi.txt","r")
f1=f.readlines()
while True:
    for x in f1:
        ser.write(x)


	
