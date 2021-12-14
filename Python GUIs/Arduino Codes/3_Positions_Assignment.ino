#include <Braccio.h>
#include <Servo.h>


Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;


// while loop for position 1
void position1(int increment)
{
  while (increment--) // will count down from 10, increment integer will be subtracted each time the arm finishes making a mark on the target
  {
    Braccio.ServoMovement(20, 0, 0, 101, 84, 90, 73);
    delay(1000);

    Braccio.ServoMovement(20, 0, 130, 131, 143, 86, 73); // robot arm angle that will make a mark on the target

    // when that arm makes the 10th mark, it should go back to its home position
    if (increment == 0) 
    { 
      Braccio.ServoMovement(20, 180, 90, 95, 81, 75, 73);
      delay(5000);
      position2(10);
    }
  }
}



// while loop for position 2
void position2(int increment)
{
  while (increment--)
  {
    Braccio.ServoMovement(20, 180, 180, 101, 84, 90, 73);
    delay(1000);

    Braccio.ServoMovement(20, 180, 60, 71, 7, 86, 73);

    if (increment == 0)
    {
      Braccio.ServoMovement(20, 90, 90, 95, 81, 75, 73);
      delay(5000);
      position3(10);
    }
  }
}



// while loop for position 3
void position3(int increment)
{
  while (increment--)
  {
    Braccio.ServoMovement(20, 90, 180, 101, 84, 90, 73);
    delay(1000);

    Braccio.ServoMovement(20, 90, 62, 70, 8, 90, 73);

    if (increment == 0)
    {
      Braccio.ServoMovement(20, 90, 90, 95, 81, 75, 73);
    }
  }
}



void setup() {  
  Braccio.begin();

  
  // position 1
  Braccio.ServoMovement(20, 0, 90, 95, 81, 75, 73); // grippers opens a little bit to give us a chance to change our markers
  delay(5000);
  Braccio.ServoMovement(20, 0, 90, 95, 81, 90, 73); // gripper closes and should hold the marker tightly
  delay(2000);
  position1(10);  // number of times we expect the robot to make a mark on the target
 

  /*
  // position 2
  Braccio.ServoMovement(20, 180, 90, 95, 81, 75, 73); // the base must be rotated 180 degrees before the while loop can begin
  delay(5000);
  Braccio.ServoMovement(20, 180, 90, 95, 81, 90, 73); // gripper closes and should hold the marker tightly
  delay(2000);
  position2(10);
  


  // position 3
  Braccio.ServoMovement(20, 90, 90, 95, 81, 75, 73); // the base must be rotated 90 degrees before the while loop can begin
  delay(5000);
  Braccio.ServoMovement(20, 90, 90, 95, 81, 90, 73); // gripper closes and should hold the marker tightly
  delay(2000);
  position3(10);
  */
}

void loop() {
}
