import processing.serial.*;

Serial myPort;
String myText;
float distance;

void setup() {
  size(300, 300);  
  myPort = new Serial(this, Serial.list()[1], 9600);
  myPort.bufferUntil('\n'); 
}

void serialEvent(Serial myPort) {
  myText = myPort.readStringUntil('\n');
}

void draw() {
  background(0);     
  text(myText, 120, 120);
  distance = float(trim(myText));
  if (distance > 0.0) {
    if (distance < 50.0) {
      fill(255, 0, 0);
      rect(0, 0, 30, 30);
    } else if (distance < 100.0) {
      fill(0, 255, 0);
      rect(0, 0, 30, 30);
    } else {
      fill(0, 0, 255);
      rect(0, 0, 30, 30);
    }
  } else {
    rect(0, 0, 30, 30);
  }
  
  myText = "";
  
  
  
}
