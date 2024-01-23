import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty

lin_x = [0.00, 4.00, 0.00, 4.00, 0.00, 4.00, 0.00, 6.18, 0.00, 6.18, 0.00, 6.18]
ang_z = [3.11, 0.00, -2.08, 0.00, -2.08, 0.00, -0.52, -3.09, 1.04, -3.09, 1.04, -3.09]

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def set_position(self, x, y, theta):
        tele_client = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        # Async client
        while not tele_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        tele_req = TeleportAbsolute.Request()
        tele_req.x = x
        tele_req.y = y
        tele_req.theta = theta

        # Send the service request and wait for response
        tele_future = tele_client.call_async(tele_req)
        rclpy.spin_until_future_complete(self, tele_future)

        clear_client = self.create_client(Empty, '/clear')
        # Async client
        while not clear_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        clear_req = Empty.Request()
        clear_future = clear_client.call_async(clear_req)
        rclpy.spin_until_future_complete(self, clear_future)
        self.get_logger().info('Clearing complete.')

    def timer_callback(self):
        msg = Twist()

        msg.linear.x = lin_x[self.i] if self.i <= (len(lin_x) - 1) else 0.0
        msg.angular.z = ang_z[self.i] if self.i <= (len(ang_z) - 1) else 0.0

        self.publisher_.publish(msg)
        self.get_logger().info(f'x = {msg.linear.x}, z = {msg.angular.z} || {self.i} = {len(lin_x) - 1}/{len(ang_z) - 1}')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    
    minimal_publisher.set_position(7.5, 5.0, 0.0)
    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()