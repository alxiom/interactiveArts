import org.openkinect.processing.*;

Kinect2 yan;

PImage img;

void setup() {
  size(512, 424);
  yan = new Kinect2(this);
  yan.initDepth();
  yan.initDevice();
  img = createImage(yan.depthWidth, yan.depthHeight, RGB);
}

void draw() {  
  //PImage img  = yan.getDepthImage();
  //image(img, 0, 0);
  
  img.loadPixels();
  
  int[] depth = yan.getRawDepth();
  
  for (int x = 0; x < yan.depthWidth; x++) {
    for (int y = 0; y < yan.depthHeight; y++) {
      int offset = x + y * yan.depthWidth;
      int d = depth[offset];
      
      if (d > 2000 && d < 2500) {
        img.pixels[offset] = color(255, 0, 150);
      } else {
        img.pixels[offset] = color(0);
      }
      
    }
  }
  img.updatePixels();
  image(img, 0, 0);
}
