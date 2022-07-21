#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

class FastSubscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Float32, self.fastCallback)

    def fastCallback(self, topic_data):
        rospy.loginfo("FastCallback: " + str(topic_data.data))


class SlowSubscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Float32, self.slowCallback)

    def slowCallback(self, topic_data):
        # Waiting 5 seconds
        rate = rospy.Rate(1)
        for i in range(0, 5):
            rate.sleep()

        rospy.loginfo("SlowCallback: " + str(topic_data.data))


if __name__ == '__main__':
    rospy.init_node('double_subscriber')
    fastSubscriber = FastSubscriber("topic_1")
    fastSubscriber = SlowSubscriber("topic_2")
    rospy.spin()


## ROS Commands to publish to topic
## Run roscore

## Publish topic
# rostopic pub /topic_1 std_msgs/Float32 "data: 1.0"

## Publish msg at a fixed rate (10 Hz)
# rostopic pub -r 10 /topic_1 std_msgs/Float32 "data: 1.0"
# rostopic pub -r 10 /topic_2 std_msgs/Float32 "data: 5.0"