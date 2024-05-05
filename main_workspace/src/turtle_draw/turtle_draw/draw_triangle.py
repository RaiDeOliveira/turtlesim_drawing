import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class TriangleDrawer(Node):

    def __init__(self):
        super().__init__('triangle_drawer')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/turtle1/cmd_vel',
            qos_profile=10
        )

        self.timer = self.create_timer(
            timer_period_sec=2,
            callback=self.triangle_path
        )

    def triangle_path(self):
        msg = Twist()
        msg.angular.z = 3.0
        msg.linear.x = 2.0
        self.publisher.publish(msg)

def main():
    rclpy.init()
    dt = TriangleDrawer()
    rclpy.spin(dt)
    dt.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



