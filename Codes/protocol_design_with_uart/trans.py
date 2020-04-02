import serial
START = 0x45 
FRAME = 0x00
STOP = 0x54
ACK = 0x95  


PULSE_WIDTH = 10 
INIT = 3           
DATA = 6           
END = 1           

TEXT = "po is the dragon warrior!!"
wait = 500
print(wait)

i=0
a=0
ser = serial.Serial()
def setup():   
   
    ser.baudrate = 4800
    print(ser)


def loop():
    CHECK = 0
    SIZE = 0
    rec_ack = 0
    for j in PULSE_WIDTH:
        uart[j]=0
      #  print(hex(10))

    if a<len(TEXT):
        uart[0] = START
        CHECK = START
        uart[1] = FRAME
        CHECK += FRAME
        SIZE = byte(min(DATA,int(len(TEXT))-a))
        uart[2] = SIZE
        CHECK+=SIZE
      #  print(hex(10))

        for i in min(int(len(TEXT))-a):
            uart[i+INIT] = TEXT[i+a]
            CHECK += TEXT[i+a]
        #    print(hex(10))

    
        uart[i+INIT] = CHECK

        for j in i+INIT+END:
            ser.write(uart[j])
         #   print(ser.hex(uart[j]))
          #  print(hex(10))
    
        TIME = ser.in_waiting
        while ser.in_waiting-TIME < wait:
        #yeild()   watchdog reset search command in pyserail
            if ser.available()>0 :
                rec_ack = ser.read()
                if rec_ack == ACK :
                    a+=i
                    FRAME+=1
                   # ser.print("STOP")
                    break

    else:
        ser.write(STOP)        

if __name__ == "main":
    setup()
    while(1):
        loop()

