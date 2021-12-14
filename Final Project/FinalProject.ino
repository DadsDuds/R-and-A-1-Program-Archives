// Marshall Sullivan
// Assignment 8
// ENGN4075 - Robotics & Automation I

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
    Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);

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

    if (strcmp("TL", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 67, 106, 163, 151, 85, 73);
      delay(500);
      Braccio.ServoMovement(20, 67, 106, 163, 151, 45, 73);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
     }

   if (strcmp("X", messageFromPC) == 0) {
    Braccio.ServoMovement(20, 137, 78, 180, 175, 45, 41);
    delay(1000);
    Braccio.ServoMovement(20, 137, 78, 180, 175, 85, 41);
    delay(500);
    Braccio.ServoMovement(20, 137, 60, 180, 175, 85, 41);
   }
   
   if (strcmp("O", messageFromPC) == 0) {
     Braccio.ServoMovement(20, 52, 105, 171, 155, 45, 51);
     delay(1000);
     Braccio.ServoMovement(20, 52, 105, 171, 155, 85, 51);
     delay(500);
     Braccio.ServoMovement(20, 50, 95, 171, 155, 85, 51);
   }

    

    if (strcmp("TM", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 78, 102, 163, 156, 85, 73);
      delay(500);
      Braccio.ServoMovement(20, 78, 102, 163, 156, 45, 73);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
      
    }

    if (strcmp("TR", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 92, 110, 180, 127, 85, 10);
      delay(500);
      Braccio.ServoMovement(20, 92, 110, 180, 127, 45, 10);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);

    }

    if (strcmp("ML", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 63, 85, 168, 168, 85, 73);
      delay(500);
      Braccio.ServoMovement(20, 63, 85, 168, 168, 45, 73);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);

    }

    if (strcmp("M", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 80, 80, 171, 169, 85, 73);
      delay(500);
      Braccio.ServoMovement(20, 80, 80, 171, 169, 45, 73);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
  
    }

    if (strcmp("MR", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 94, 96, 180, 150, 85, 10);
      delay(500);
      Braccio.ServoMovement(20, 94, 96, 180, 150, 45, 10);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
  
    }

    if (strcmp("BL", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 60, 71, 180, 176, 85, 65);
      delay(500);
      Braccio.ServoMovement(20, 60, 71, 180, 176, 45, 65);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
  
    }

    if (strcmp("BM", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 78, 68, 180, 180, 85, 73);
      delay(500);
      Braccio.ServoMovement(20, 78, 68, 180, 180, 45, 73);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
  
    }

    if (strcmp("BR", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 96, 70, 177, 176, 85, 10);
      delay(500);
      Braccio.ServoMovement(20, 96, 70, 177, 176, 45, 10);
      delay(500);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
  
    }

    if (strcmp("W", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
      delay(1000);
      Braccio.ServoMovement(20, 0, 70, 117, 106, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 105, 78, 57, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 70, 117, 106, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 105, 78, 57, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 70, 117, 106, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 105, 78, 57, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 70, 117, 106, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 105, 78, 57, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 70, 117, 106, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 0, 105, 78, 57, 90, 73);
      delay(250);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
    }

    if (strcmp("L", messageFromPC) == 0) {
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
      delay(1000);
      Braccio.ServoMovement(20, 88, 93, 180, 121, 90, 73);
      delay(5000);
      Braccio.ServoMovement(20, 90, 88, 100, 81, 81, 73);
    }

}
