## import the serial library
import serial

## Boolean variable that will represent 
## whether or not the arduino is connected
connected = False

## establish connection to the serial port that your arduino 
## is connected to.
ser = serial.Serial('/dev/ttyUSB1', 1200)
while 1:
    if ser.inWaiting():
        x = ser.read()
        print(x)
        
ser.close()