#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

class OdometrySubscriber(object):
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Odometry, self.odomCallback)

    def odomCallback(self, topic_data):
        ori_q = topic_data.pose.pose.orientation
        (roll, pitch, yaw) = euler_from_quaternion([ori_q.x, ori_q.y, ori_q.z, ori_q.w])
        #roll_deg = math.degrees(roll)
        #pitch_deg = math.degrees(pitch)
        yaw_deg = math.degrees(yaw)
        rospy.loginfo("Yaw: " + str(yaw_deg))


if __name__ == '__main__':
    rospy.init_node('quatertions_to_euler')
    odomSubscriber = OdometrySubscriber("/odometry/filtered")
    rospy.spin()


