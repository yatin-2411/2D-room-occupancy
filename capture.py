import numpy as np
from PIL import Image
import cv2

def create_composite_map(images):
    composite_map = np.zeros((512, 512), dtype=np.uint8)
    for img in images:
        resized_img = cv2.resize(img, (512, 512))
        composite_map += resized_img // 4
    Image.fromarray(composite_map).save('composite_map.pgm')

images = [
    cv2.imread('camera1.png', 0),
    cv2.imread('camera2.png', 0),
    cv2.imread('camera3.png', 0),
    cv2.imread('camera4.png', 0)
]
create_composite_map(images)
