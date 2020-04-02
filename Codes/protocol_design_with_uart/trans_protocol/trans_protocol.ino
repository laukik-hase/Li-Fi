// permanent info

byte START = 0x45; //the start of frame
byte FRAME = 0x00;
byte STOP = 0x54;
byte ACK = 0x95;  //the acknowledgement
byte ID;

int PULSE_WIDTH = 10;   // stop
int INIT = 3;           // start and control 
int DATA = 6;           // data
int END = 1;            // stop

String TEXT = "po is the dragon warrior!!";
int wait = 500;

// calculated for every pulse

byte SIZE;
byte CHECK;        //check-sum of the packet
byte rec_ack;
unsigned long Time;

// the pulse

byte uart[10];   // the pulse ... start control DATA[size(6)] check

// position and loop

int i=0,a=0;      //on which letter of the string you are currently

#include<SoftwareSerial.h> // soft serial port header file
SoftwareSerial Serial2(0,2); // define the soft serial port as Serial2, D3 as RX, and D4 as TX

void setup()
{
  Serial2.begin(4800);
  Serial.begin(4800);
} 

void loop()
{
// resets

//  /while(Serial2.available())
//    /Serial2.flush();
 
  CHECK = 0;
  SIZE = 0;
  rec_ack = 0;
  
  for(int j = 0 ; j<PULSE_WIDTH ; j++)
    uart[j] = 0;

  if(a<TEXT.length())  
  {
    
// pulse generation

      uart[0] = START;
        CHECK = START;
        
      uart[1] = FRAME;
        CHECK += FRAME;
        
      SIZE = (byte)min(DATA,(int)TEXT.length()-a);
      uart[2] = SIZE;
        CHECK+=SIZE;
      
      for(i=0;i<min(((int)TEXT.length()-a),DATA);i++)
      { 
       uart[i+INIT] = TEXT[i+a];
          CHECK += TEXT[i+a];
      }

      uart[i+INIT] = CHECK;

// pulse transfer

      for(int j = 0; j < (i+INIT+END) ; j++)
      {
      Serial2.write(uart[j]); // start
      Serial.println(uart[j],HEX); // start
      }

// acknowledge 
      
      Time = millis();
      while(millis()-Time < wait)
      {
        yield();  // soft wdt reset (watchdog reset)
        
        if(Serial2.available()>0)
        {  
          rec_ack = Serial2.read();
          
          if(rec_ack == ACK)
          {
            a+=i;
            FRAME++;
            Serial.println("STOP");
            break;
          }
          
        }
      }
    }
    
// end

    else
      Serial2.write(STOP);  
}