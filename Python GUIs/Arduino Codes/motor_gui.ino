

#include <Braccio.h>
#include <Servo.h>


const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];
char messageFromPC[numChars] = {0};

int m1 = 0;

boolean newData = false;

//============

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);

  Serial.begin(115200);

}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        showParsedData();
        newData = false;

    
    }
}

//============

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index

    strtokIndx = strtok(tempChars,",");    // get the first part - the string
    strcpy(messageFromPC, strtokIndx);    // copy it to messageFromPC

    strtokIndx = strtok(NULL, ",");
    m1 = atoi(strtokIndx);
    


}

//============

void showParsedData() {

    if (strcmp("i", messageFromPC) == 0) {
      Serial.println("Ready!");

      
    }

    if (strcmp("C", messageFromPC) == 0) {
      
      digitalWrite(9, LOW);
      digitalWrite(10, HIGH);
    }

    if (strcmp("CW", messageFromPC) == 0) {
 
      digitalWrite(10, LOW);
      digitalWrite(9, HIGH);
    }

    if (strcmp("e", messageFromPC) == 0) {
      digitalWrite(2, HIGH);

    }

    if (strcmp("d", messageFromPC) == 0) {
      digitalWrite(2, LOW);
      
    }

     if (strcmp("s", messageFromPC) == 0) {
      Serial.println(m1);
      analogWrite(10, m1);

    }

 

}
