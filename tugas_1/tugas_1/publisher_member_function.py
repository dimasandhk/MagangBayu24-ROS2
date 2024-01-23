import random as rand
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# Mempublish secara random permasalahan matematika sederhana dengan format: (num1) (opr1) (num2) (opr2) (num3)

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        opr = ['+', '-', '*', '/', '%']
        msg = String()

        num1 = rand.randint(1, 10000)
        num2 = rand.randint(1, 10000)
        num3 = rand.randint(1, 10000)

        opr1 = rand.choice(opr)
        opr2 = rand.choice(opr)

        msg.data = f'{num1} {opr1} {num2} {opr2} {num3}'
        self.publisher_.publish(msg)
        self.get_logger().info('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
