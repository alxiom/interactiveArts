int led_pin = 9;

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  int nob = analogRead(A5) / 4;
  Serial.println(nob);
  analogWrite(led_pin, nob);
}
