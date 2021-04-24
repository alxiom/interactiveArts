int motorPin = 11;

void setup() {
  Serial.begin(9600);
  pinMode(motorPin, OUTPUT);
}

void loop() {
  int nob = analogRead(A5) / 4;
  Serial.println(nob);
  analogWrite(motorPin, nob);
}
