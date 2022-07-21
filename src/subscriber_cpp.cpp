#include <ros/ros.h>
#include <std_msgs/Float32.h>

class FastSubscriber {
    public:
        ros::Subscriber sub;

        FastSubscriber(ros::NodeHandle nh, std:: string topic_name)
        {
            sub = nh.subscribe<std_msgs::Float32>(topic_name, 1, &FastSubscriber::fastCallback, this);
        }

        void fastCallback(const std_msgs::Float32::ConstPtr &topic_data) 
        {
            ROS_INFO_STREAM("FastCallback: " << topic_data->data);
        }
};

class SlowSubscriber {
    public:
        ros::Subscriber sub;

        SlowSubscriber(ros::NodeHandle nh, std:: string topic_name)
        {
            sub = nh.subscribe<std_msgs::Float32>(topic_name, 1, &SlowSubscriber::slowCallback, this);
        }

        void slowCallback(const std_msgs::Float32::ConstPtr &topic_data)
        {
            ros::Rate rate(1);
            for(int i = 0; i < 5; i++) {
                rate.sleep();
            }

            ROS_INFO_STREAM("SlowCallback: " << topic_data->data);
        }
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "subscriber_cpp");
    ros::NodeHandle nh;

    FastSubscriber fastsubs(nh, "topic_1");
    SlowSubscriber slowsubs(nh, "topic_2");

    // An alternative to ros::spin()
    ros::MultiThreadedSpinner spinner(2);
    spinner.spin();

    // ros::spin();

    return 0;
}
