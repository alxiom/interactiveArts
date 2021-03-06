import cv2
import time
from scipy.spatial import ConvexHull
import numpy as np
import mediapipe as mp

title = "useless_mirror"

cap = cv2.VideoCapture(1)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=2)
mp_draw = mp.solutions.drawing_utils

snapshot_key = 76
track_key = 75
fps_key = 74

snapshot = None
is_track = False
show_fps = True
mode = "T"  # ["TRANSPARENT", "OVERLAY"]
frame_count = 0
speed = 5e-3

time_gap = 0.2
prev_time = 0
curr_time = 0

boundary = 20

while True:
    success, img = cap.read()
    height, width, _ = img.shape

    if is_track:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img_rgb)
        face_landmarks = results.multi_face_landmarks

        if face_landmarks:
            for face_landmark in face_landmarks:
                face_points = []
                for landmark in face_landmark.landmark:
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    face_points.append((x, y))
                points = np.array(face_points)
                hull_index = ConvexHull(points).vertices
                hull_point = [face_points[i] for i in hull_index]
                hull_array = [np.array(hull_point, np.int32).reshape((-1, 1, 2))]

                if mode.upper() in ["OVERLAY", "O"]:
                    cv2.polylines(img, hull_array, isClosed=True, color=(0, 0, 255), thickness=boundary)
                    cv2.fillPoly(img, hull_array, color=(0, 0, 255))
                elif mode.upper() in ["TRANSPARENT", "T"]:
                    mask = np.zeros(img.shape, img.dtype)
                    cv2.polylines(mask, hull_array, isClosed=True, color=(255, 255, 255), thickness=boundary)
                    cv2.fillPoly(mask, hull_array, color=(255, 255, 255))

                    if snapshot is not None:
                        patch = cv2.bitwise_and(mask, snapshot)
                        patch_inverse = cv2.bitwise_not(mask)
                        background = cv2.bitwise_and(patch_inverse, img)
                        alpha = min(frame_count * speed, 1.0)
                        patch_image = cv2.add(patch, background)
                        img = cv2.addWeighted(patch_image, alpha, img, 1.0 - alpha, 1)
                        frame_count += 1
        else:
            frame_count = 0

    if show_fps:
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow(title, img)

    key_pressed = cv2.waitKey(1)

    if key_pressed == snapshot_key:
        print("take snapshot")
        snapshot = img.copy()
        time.sleep(time_gap)

    elif key_pressed == track_key:
        is_track = not is_track
        print("tracking status:", is_track)
        time.sleep(time_gap)

    elif key_pressed == fps_key:
        show_fps = not show_fps
        print("show fps:", show_fps)
        time.sleep(time_gap)
