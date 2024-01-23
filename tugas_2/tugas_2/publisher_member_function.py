import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher1 = self.create_publisher(String, 'topic1', 10)
        self.publisher2 = self.create_publisher(String, 'topic2', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        param1 = str(not (self.i % 2))
        param2 = str(not (self.i % 3))

        msg1 = String()
        msg1.data = param1
        self.publisher1.publish(msg1)
        self.get_logger().info(f'publisher - 1 - ({self.i} sec) -> {msg1.data}')

        msg2 = String()
        msg2.data = param2
        self.publisher2.publish(msg2)
        self.get_logger().info(f'publisher - 2 - ({self.i} sec) -> {msg2.data}')

        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
