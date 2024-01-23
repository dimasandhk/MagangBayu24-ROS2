import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            String,
            'topic1',
            self.listener_callback1,
            10
        )
        self.subscription1

        self.subscription2 = self.create_subscription(
            String,
            'topic2',
            self.listener_callback2,
            10
        )
        self.subscription2

        self.param1 = None
        self.param2 = None

    def listener_callback1(self, msg):
        self.param1 = msg.data

    def listener_callback2(self, msg):
        self.param2 = msg.data
        res = eval(f'{self.param1} and {self.param2}')
        
        status = 'sudah siap nih, gass min!' if res else 'tunggu dulu, kami belum ready!'
        self.get_logger().info(f'pub1 - ({self.param1}) | pub2 ({self.param2}) -> {status}')

        self.param1 = None
        self.param2 = None


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
