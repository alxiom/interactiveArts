import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mp_face_detection = mp.solutions.face_mesh
face_mesh = mp_face_detection.FaceMesh()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)
    face_landmarks = results.multi_face_landmarks

    if face_landmarks:
        for face_landmark in face_landmarks:
            mp_draw.draw_landmarks(
                img,
                landmark_list=face_landmark,
                connections=mp_face_detection.FACE_CONNECTIONS,
            )

    cv2.imshow("image", img)
    cv2.waitKey(1)
