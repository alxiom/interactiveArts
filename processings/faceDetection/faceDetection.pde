import gab.opencv.*;
import processing.video.*;
import java.awt.*;

Capture cam;
OpenCV opencv;
PImage snapshot;
PImage patch;
PGraphics maskImage;
int scaleFactor = 2;
boolean isTracking = false;


void setup() {
  size(640, 480);
  cam = new Capture(this, width / scaleFactor, height / scaleFactor);
  opencv = new OpenCV(this, width / scaleFactor, height / scaleFactor);
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);

  cam.start();
  snapshot = createImage(width / scaleFactor, height / scaleFactor, ARGB);
  maskImage = createGraphics(width / scaleFactor, height / scaleFactor);
}

void draw() {
  noStroke();
  noFill();
  scale(scaleFactor);
  opencv.loadImage(cam);
  
  image(cam, 0, 0 );

  if (isTracking) {
    Rectangle[] faces = opencv.detect();
    //println(faces.length);
    
    for (int i = 0; i < faces.length; i++) {
      //println(faces[i].x + "," + faces[i].y);
      //rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
      
      //patch = snapshot.get(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
      //image(patch, faces[i].x, faces[i].y, faces[i].width, faces[i].height);
     
      float centerX = faces[i].x + faces[i].width / 2;
      float centerY = faces[i].y + faces[i].height / 2;
      float radious = sqrt(sq(faces[i].width) + sq(faces[i].height));
      maskImage.beginDraw();
      maskImage.background(0);
      maskImage.fill(255);
      maskImage.ellipse(centerX, centerY, radious, radious);
      maskImage.endDraw();

      patch = snapshot.copy();
      patch.mask(maskImage);
      image(patch, 0, 0);
    }
  }
}

void captureEvent(Capture c) {
  c.read();
}

void keyReleased() {
  if (key == 'x') {
    snapshot.copy(cam, 0, 0, cam.width, cam.height, 0, 0, snapshot.width, snapshot.height);
    println("create snapshot");
  } else if (key == 'z') {
    isTracking = !isTracking;
    println("tracking: ", isTracking);
  }
}
