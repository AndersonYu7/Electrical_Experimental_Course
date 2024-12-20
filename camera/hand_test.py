#!/usr/bin/python
#coding-utf-8
from builtins import breakpoint
import os
import cv2
from DepthCameraAPI_media import DepthCameraAPI
from ultralytics import YOLO

cam = DepthCameraAPI()

CAMERANUMBER_FLAG = None

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 640, 640)

cv2.namedWindow('media_image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('media_image', 640, 640)

script_dir = os.path.dirname(os.path.abspath(__file__))
model = YOLO(os.path.join(script_dir, 'yolo_weights', 'best.pt'))

try:
    while True:
        image = cam.capture_depth_image()
        media_image = cam.hand_detection(image)
        results = model(media_image)
        
        res = results[0]
        high_conf_boxes = res.boxes[res.boxes.conf > 0.9]
        res.boxes = high_conf_boxes

        media_image = res.plot()

        if media_image is not None:
            cv2.imshow('media_image', media_image)
            cv2.imshow('image', image)
        else:
            print("image not load correctly")

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('p'):
            cam.capture_photo(media_image)

except KeyboardInterrupt:
    pass

finally:
    cam.release()
    cv2.destroyAllWindows()
