#include <Braccio.h>
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];
char messageFromPC[numChars] = {0};

int m1 = 0;
int m2 = 0;
int m3 = 0;
int m4 = 0;
int m5 = 0;
int m6 = 0;

boolean newData = false;

//============

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(115200);
    Braccio.begin();
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
    
    strtokIndx = strtok(NULL, ",");
    m2 = atoi(strtokIndx);     

    strtokIndx = strtok(NULL, ",");
    m3 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    m4 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    m5 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    m6 = atoi(strtokIndx);

}

//============

void showParsedData() {

    if (strcmp("i", messageFromPC) == 0) {
      Serial.println("Ready!");
      Serial.println(m1);
      Serial.println(m2);
      Serial.println(m3);
      Serial.println(m4);
      Serial.println(m5);
      Serial.println(m6);
    }

    if (strcmp("H", messageFromPC) == 0) {
      digitalWrite(13, HIGH);
    }

    if (strcmp("m1", messageFromPC) == 0) {
      Braccio.ServoMovement(20, m1, m2, m3, m4, m5, m6);
      Serial.println(m1);
    }

    if (strcmp("p1", messageFromPC) == 0) {
      Braccio.ServoMovement(20, m1, m2, m3, m4, m5, m6);

    }

    if (strcmp("p2", messageFromPC) == 0) {
      Braccio.ServoMovement(20, m1, m2, m3, m4, m5, m6);

    }

    if (strcmp("p3", messageFromPC) == 0) {
      Braccio.ServoMovement(20, m1, m2, m3, m4, m5, m6);
  
    }

}
