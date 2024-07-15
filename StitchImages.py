import cv2
import numpy as np

def stitch_images(image_paths):
    # Load images
    images = [cv2.imread(image_path) for image_path in image_paths]
    
    # Create a stitcher and stitch images
    stitcher = cv2.Stitcher.create()
    status, stitched_image = stitcher.stitch(images)
    
    if status != cv2.Stitcher_OK:
        print("Error during stitching")
        return None
    
    return stitched_image

image_paths = ['camera1.png', 'camera2.png', 'camera3.png', 'camera4.png']
stitched_image = stitch_images(image_paths)

if stitched_image is not None:
    cv2.imwrite('stitched_image.png', stitched_image)
    cv2.imshow('Stitched Image', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
