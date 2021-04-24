float sensorValue;
float filterValue;
float sensitivity = 0.1;
                               
void setup() {
  Serial.begin(9600);
  sensorValue = analogRead(A0);
  filterValue = sensorValue;
}

void loop() {
  sensorValue = analogRead(A0);
  filterValue = (1 - sensitivity) * filterValue + sensitivity * sensorValue;

  float voltage = filterValue * 5 / 1024.0;
  float distance = 65 * pow(voltage, -1.10);

  Serial.print(distance);
  Serial.print(",");
  Serial.println(65 * pow(sensorValue * 5 / 1024.0, -1.10));
  
  delay(20);                                     
}

//#define num 20
//float sensorValues[num];
//
//void setup() {
//  Serial.begin(9600);
//}
//
//void loop() {
//  for (int i = 0; i < num - 1; i++) {
//    sensorValues[i] = sensorValues[i + 1];
//  }
//  float sensorValue = analogRead(A0);
//  sensorValues[num - 1] = sensorValue;
//  float filterValue = 0;
//  for (int i = 0; i < num; i++) {
//    filterValue += sensorValues[i];
//  }
//  filterValue /= num;
//
//  Serial.print(65 * pow(filterValue * 5 / 1024.0, -1.10));
//  Serial.print(",");
//  Serial.println(65 * pow(sensorValue * 5 / 1024.0, -1.10));
//  
//  delay(20);      
//}
