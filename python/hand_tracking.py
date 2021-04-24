import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    hand_landmarks = results.multi_hand_landmarks

    if hand_landmarks:
        for hand_landmark in hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                landmark_list=hand_landmark,
                connections=mp_hands.HAND_CONNECTIONS,
            )

    cv2.imshow("image", img)
    cv2.waitKey(1)
