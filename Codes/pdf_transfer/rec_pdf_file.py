import os
import serial

save_path = os.path.join(os.path.expanduser('~'),'Desktop/LiFi-master/Recieved_files') 
ser  = serial.Serial('/dev/ttyUSB2',4800,timeout=0)
base_path = os.path.basename("received.pdf")
#print("base path")
file = open(os.path.join(save_path,base_path),"wb")
#print("file open")

while 1:
    if ser.inWaiting():
        readf = ser.read()
    	file.write(readf)
	print("Receiving File...")	
	file.flush()
file.close()
ser.close()
