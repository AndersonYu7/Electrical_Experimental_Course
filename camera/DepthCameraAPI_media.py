#!/usr/bin/python
#coding-utf-8
import os
import cv2
import mediapipe as mp
import numpy as np

SCRIPT = os.path.dirname(os.path.abspath(__file__))
PHOTO_CLASS = "ddd"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )    
mp_drawing = mp.solutions.drawing_utils
drawing_styles = mp.solutions.drawing_styles

class DepthCameraAPI:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.photo_counter = 0

    def capture_depth_image(self):
        ret, image = self.cap.read()
        if not ret or image is None:
            print("Error: Unable to capture depth image.")
            return None, None
        return image
    
    def capture_photo(self, image):
        self.photo_counter += 1
        photo_name = f"{PHOTO_CLASS}_{self.photo_counter + 0}.png"
        photo_write = SCRIPT + f"/photo/{PHOTO_CLASS}/" + photo_name
        cv2.imwrite(photo_write, image)
        print(f"Photo {self.photo_counter} saved as {photo_name}")

    def hand_detection(self, image):
        results = hands.process(image)
        
        black_image = np.zeros_like(image, dtype=np.uint8)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                mp.solutions.drawing_utils.draw_landmarks(
                    black_image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    drawing_styles.get_default_hand_landmarks_style(),
                    drawing_styles.get_default_hand_connections_style()
                )
            return black_image
        else:
            image = np.zeros_like(image, dtype=np.uint8)
            return image

        # return image

    def release(self):
        # 释放资源
        self.cap.release()