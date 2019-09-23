// permanent info

byte START = 0x45;  //the start of frame
byte FRAME = 0x00;
byte STOP = 0x54;
byte ACK = 0x95;    //the acknowledgement
byte ID;

int PULSE_WIDTH = 10;   // stop
int INIT = 3;           // start and control
int DATA = 6;           // data
int END = 1;            // stop

// calculated for every pulse

int SIZE;
byte CHECK;        //check-sum of the packet
String packet = "";
String text = "";
unsigned long Time;

// the pulse

byte uart[10];

#include<SoftwareSerial.h>// soft serial port header file
SoftwareSerial Serial2(0, 2); // define the soft serial port as Serial2, D3 as RX, and D4 as TX

void setup()
{
  Serial2.begin(9600);
  Serial.begin(9600);
  text = "";
}

void loop()
{
  // resets

  SIZE = 0;
  CHECK = 0;
  packet = "";


  if (Serial2.available() > PULSE_WIDTH) // number udane ka try kar
  {
    // pulse detection

    // start

    uart[0] = Serial2.read();
    if (uart[0] == START)
    {

      //controls

      uart[1] = Serial2.read();
      if (uart[1] == FRAME)
      {

        uart[2] = Serial2.read();
        SIZE = (int)uart[2];

        //data

        for (int i = 0 ; i < SIZE ; i++)
        {
          uart[i + INIT] = Serial2.read();
          packet += (char)uart[i + INIT];
        }

        // CHECKSUM

        uart[SIZE + INIT] = Serial2.read();

        // error detection

        for (int i = 0; i < ( SIZE + INIT ); i++)
        {
          CHECK += uart[i]; //sum on the receiving side
          uart[i] = 0;      // reset pulse
        }

        if (CHECK == uart[SIZE + INIT])
        {

          // data storage

          text += packet;

          // acknowledge

          FRAME++;
          Serial2.write(ACK);

          // reset error

          uart[SIZE + INIT] = 0;

        }
      }
    }
    // end

    else if (uart[0] == STOP) {

      Serial.println(text);
    }

  }
}
