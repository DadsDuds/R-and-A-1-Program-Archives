#include <Braccio.h>
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

int a, b, c, d, e, f;

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];
char messageFromPC[numChars] = {0};

int MotorOne = 0;
int MotorTwo = 0;
int MotorThree = 0;
int MotorFour = 0;
int MotorFive = 0;
int MotorSix = 0;

boolean newData = false;

//============

void setup() {
    Serial.begin(115200);
    //Serial.println("This demo expects 6 pieces of data - text, integers for each motor");
    //Serial.println("Enter data in this style <1, 2, 3, 4, 5, 6>  ");
    Braccio.begin();
    Braccio.ServoMovement(20, 90, 90, 90, 90, 90, 73);
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        Braccio.ServoMovement(20, MotorOne, MotorTwo, MotorThree, MotorFour, MotorFive, MotorSix);
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
    MotorOne = atoi(strtokIndx);
    
    strtokIndx = strtok(NULL, ",");
    MotorTwo = atoi(strtokIndx);     // convert this part to a float

    strtokIndx = strtok(NULL, ",");
    MotorThree = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    MotorFour = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    MotorFive = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    MotorSix = atoi(strtokIndx);

}

//============

void showParsedData() {

    Serial.print("Angle: ");
    Serial.println(MotorOne);
    Serial.print("Angle: ");
    Serial.println(MotorTwo);
    Serial.print("Angle: ");
    Serial.println(MotorThree);
    Serial.print("Angle: ");
    Serial.println(MotorFour);
    Serial.print("Angle: ");
    Serial.println(MotorFive);
    Serial.print("Angle: ");
    Serial.println(MotorSix);

}
