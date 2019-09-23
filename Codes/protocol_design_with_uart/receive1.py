import serial
START = 0x45 #the start of frame
FRAME = 0x00
STOP = 0x54
ACK = 0x95    #the acknowledgement


PULSE_WIDTH = 10   # stop
INIT = 3           # start and control
DATA = 6           #data
END = 1            #stop

# calculated for every pulse
ser = serial.Serial()

def setup():
    ser.baudrate = 4800
    print(ser)
    text = ""


def loop():

  # resets

    SIZE = 0
    CHECK = 0
    packet = ""
    if ser.availale()>PULSE_WIDTH :
        uart[0] = ser.read()
        if uart[0] == START:
            uart[1] = ser.read()
            if uart[1] == FRAME:
                uart[2] = ser.read()
                SIZE = int(uart[2])

                for i in SIZE:
                    uart[i+INIT] = ser.read()
                    packet+=char(uart[i+INIT])
                uart[SIZE+INIT] = ser.read()

                for i in SIZE+INIT:
                    CHECK+=uart[i]
                    uart[i] = 0
                
                if CHECK == uart[SIZE+INIT]:
                    text+=packet
                    FRAME+=1
                    ser.write(ACK)
                    uart[SIZE+INIT]=0

        else if uart[0] == STOP:
            ser.print(text)            

if __name__ == "main":
    setup()
    while(1):
        loop()
