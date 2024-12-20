# skr gun rock spidar italy

# skr: Yu
# italy rock: lin
# gun spidar: han

import os
import cv2
from DepthCameraAPI_media import DepthCameraAPI

cam = DepthCameraAPI()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 640, 640)

cv2.namedWindow('media_image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('media_image', 640, 640)

def save_image_to_folder(image, folder_path):
    """Save images to the specified folder and name them sequentially"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Find the maximum index of existing files in the folder
    existing_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    existing_indices = [int(f.split('_')[1].split('.')[0]) for f in existing_files if f.startswith('image_') and f.split('_')[1].split('.')[0].isdigit()]
    next_index = max(existing_indices, default=100) + 1

    # Name the new file sequentially
    file_path = os.path.join(folder_path, f"image_{next_index}.png")
    cv2.imwrite(file_path, image)
    print(f"Image saved to: {file_path}")

try:
    while True:
        image = cam.capture_depth_image()
        media_image = cam.hand_detection(image)

        if media_image is not None:
            cv2.imshow('media_image', media_image)
            cv2.imshow('image', image)
        else:
            print("Image not loaded correctly")

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('p'):
            # Save image to the specified folder
            save_image_to_folder(media_image, 'saved_images')

except KeyboardInterrupt:
    pass

finally:
    cam.release()
    cv2.destroyAllWindows()