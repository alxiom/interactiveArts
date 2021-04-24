#include <Servo.h>

Servo testServo;
int pos = 0;
int velocity = 0;
int minVelocity = 3;

void setup() {
  Serial.begin(9600);
  testServo.attach(4);
}

void loop() {  
  for (pos = 0; pos < 360; pos++) {
    testServo.write(pos);
//    velocity = readNob(minVelocity);
    delay(minVelocity);
  }

  for (pos = 360; pos > 0; pos--) {
    testServo.write(pos);
//    velocity = readNob(minVelocity);
    delay(minVelocity);
  }
  
}

int readNob(int minV) {
  int nob = analogRead(A5) / 4;
  Serial.println(nob);
  return max(minV, nob);
}
