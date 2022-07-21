#!/usr/bin/env python

from mimetypes import init
import rospy
from geometry_msgs.msg import Twist


class RemoteController:
    def __init__(self):
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def control(self, linear_vel, angular_vel):
        msg = Twist()
        msg.linear.x = linear_vel
        msg.angular.z = angular_vel
        self.cmd_pub.publish(msg)


# Main function
if __name__ == '__main__':
    rospy.init_node('husky_robot_controller')
    controller = RemoteController()
    # -2 m/s
    vel = 0
    # 0 rad/s
    angVel = 0.5
    rate = rospy.Rate(10)
    counter = 0

    try:
        while not rospy.is_shutdown():
            if counter == 20:
                vel = -vel
                counter = 0

            controller.control(vel, angVel)
            rate.sleep()
            counter += 1

    except rospy.ROSInterruptException:
        rospy.loginfo('Got interrupt request')

    rospy.loginfo('Closing remote controller')