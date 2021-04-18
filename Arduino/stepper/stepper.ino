#include <Stepper.h>

const int spr = 64;
Stepper testStepper(spr, 8, 9, 10, 11);
int minSpeed = 10;


void setup() {
  Serial.begin(9600);
  testStepper.setSpeed(250);
//  testStepper.setSpeed(readNob(minSpeed));
}

void loop() {
  
  testStepper.step(1);
  delay(readNob(minSpeed));

}

int readNob(int minValue) {
  int nob = analogRead(A5) / 4;
  Serial.println(nob);
  return max(minValue, nob);
}
