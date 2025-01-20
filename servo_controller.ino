//#include "ServoController.h"
//#include "SerialCommand.h"
#include <string.h>
#include <Servo.h>

const int SERVO_A_PIN = 9;
const int SERVO_B_PIN = 10;

Servo servoA;
Servo servoB;

int pos = 0;

void setup()
{
    Serial.begin(9600);

    servoA.attach(SERVO_A_PIN);
    servoB.attach(SERVO_B_PIN);


}

void loop()
{
	if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();

        if (input.substring(1).toInt() >= 0 && input.substring(1).toInt() <= 180) {
            if (input.charAt(0) == 'A') {
                servoA.write(input.substring(1).toInt());
                Serial.print("Servo A set to: ");
                Serial.println(input.substring(1));
            } else if (input.charAt(0) == 'B') {
                servoB.write(input.substring(1).toInt());
                Serial.print("Servo B set to: ");
                Serial.println(input.substring(1));
            }
        } else {
            Serial.println("ERROR");
        }
    }
}
