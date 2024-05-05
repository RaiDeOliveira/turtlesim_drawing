import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from turtlesim.srv import Kill, Spawn, SetPen

import time

class TriangleDrawer(Node):

    def __init__(self):
        super().__init__('triangle_drawer')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/turtle1/cmd_vel',
            qos_profile=10
        )

    def publicar_desenho(self, angular_z, linear_x):
        msg = Twist()
        msg.angular.z = angular_z
        msg.linear.x = linear_x
        self.publisher.publish(msg)

def fazer_desenho(publisher):

    caminho = [(0.0, 0.0),
               (2.2, 0.0),
               (0.0, 3.0),
               (2.1, 0.0),
               (0.0, 3.0),
               (2.06, 0.0),
               (0.0, 2.96),
               (0.0, 0.0)]
    
    for angular_z, linear_x in caminho:
        publisher.publicar_desenho(angular_z, linear_x)
        time.sleep(1)

def main():
    rclpy.init()
    publisher = TriangleDrawer()

    fazer_desenho(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



