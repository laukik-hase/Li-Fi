import base64
import serial
ser = serial.Serial("/dev/ttyUSB1",4800,timeout=0)
y=""
while 1:
	if ser.inWaiting():
		x= ser.read()
		if x is "~":
			break
		y+=x
		print(x)
		x=""
	
file = open("img.png","wb")
file.write(y.decode('base64'))
file.close()
ser.close()
