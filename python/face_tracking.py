import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)
    faces = results.detections

    if faces:
        for face in faces:
            mp_draw.draw_detection(img, face)

    cv2.imshow("image", img)
    cv2.waitKey(1)
