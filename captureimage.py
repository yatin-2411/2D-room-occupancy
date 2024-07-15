import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraListener(Node):
    def __init__(self):
        super().__init__('camera_listener')
        self.bridge = CvBridge()
        self.image_subs = {
            'camera1': self.create_subscription(Image, '/camera1/image_raw', lambda msg: self.image_callback(msg, 'camera1'), 10),
            'camera2': self.create_subscription(Image, '/camera2/image_raw', lambda msg: self.image_callback(msg, 'camera2'), 10),
            'camera3': self.create_subscription(Image, '/camera3/image_raw', lambda msg: self.image_callback(msg, 'camera3'), 10),
            'camera4': self.create_subscription(Image, '/camera4/image_raw', lambda msg: self.image_callback(msg, 'camera4'), 10)
        }
        self.images = {}

    def image_callback(self, msg, camera_name):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.images[camera_name] = cv_image

    def save_images(self):
        for name, img in self.images.items():
            cv2.imwrite(f'{name}.png', img)

def main(args=None):
    rclpy.init(args=args)
    camera_listener = CameraListener()
    rclpy.spin_once(camera_listener, timeout_sec=2.0)

    if len(camera_listener.images) == 4:
        camera_listener.save_images()
    else:
        camera_listener.get_logger().info('Not all camera images received')

    rclpy.shutdown()

if __name__ == '__main__':
    main()
