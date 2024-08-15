#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

char command;

void setup() {  
  pinMode(2,OUTPUT);   
 Serial.begin(9600);  // Set the baud rate for Bluetooth module.
 Stop();  // Initialize with motors stopped
}

void loop() {
   if (Serial.available() > 0) { 
       command = Serial.read(); 
       Serial.println(command);
       if(command=='c'){
          digitalWrite(2, HIGH);
       }
       
       if (command == 'f') {
            forward();
            Serial.println("MOTOR MOVE FORWARD");
       } else if (command == 'b') {
            back();
            Serial.println("MOTOR MOVE REVERSE");
       } else if (command == 'l') {
            left();
            Serial.println("MOTOR MOVE LEFT");
       } else if (command == 'r') {
            right();
            Serial.println("MOTOR MOVE RIGHT");
       } else if (command == 's') {
            Stop();
       }
   } 
}

void forward() {
    // motor1.setSpeed(255); // Define maximum velocity
    // motor1.run(FORWARD); // Rotate the motor clockwise
    motor2.setSpeed(255); // Define maximum velocity
    motor2.run(FORWARD); // Rotate the motor clockwise

    // motor3.setSpeed(255); // Define maximum velocity
    // motor3.run(BACKWARD); // Rotate the motor clockwise
    motor4.setSpeed(255); // Define maximum velocity
    motor4.run(FORWARD); // Rotate the motor clockwise
}

void back() {
    left();
    left();
}

void left() {
    // motor1.setSpeed(255); // Define maximum velocity
    // motor1.run(FORWARD); // Rotate the motor clockwise
    motor2.setSpeed(255); // Define maximum velocity
    motor2.run(FORWARD); // Rotate the motor counterclockwise

    // motor3.setSpeed(255); // Define maximum velocity
    // motor3.run(FORWARD); // Rotate the motor clockwise
    motor4.setSpeed(255); // Define maximum velocity
    motor4.run(BACKWARD); // Rotate the motor counterclockwise
}

void right() {
    // motor1.setSpeed(255); // Define maximum velocity
    // motor1.run(BACKWARD); // Rotate the motor counterclockwise
    motor2.setSpeed(255); // Define maximum velocity
    motor2.run(BACKWARD); // Rotate the motor clockwise

    // motor3.setSpeed(255); // Define maximum velocity
    // motor3.run(BACKWARD); // Rotate the motor counterclockwise
    motor4.setSpeed(255); // Define maximum velocity
    motor4.run(FORWARD); // Rotate the motor clockwise
}

void Stop() {
    motor1.run(RELEASE); // Turn motor1 off
    motor2.run(RELEASE); // Turn motor2 off
    motor3.run(RELEASE); // Turn motor3 off
    motor4.run(RELEASE); // Turn motor4 off
}