#!/usr/bin/env python

## This node subscribes to topic name 'sensed_object' of type Pose
## This node subscribes to topic name '/cmd_vel' of type Twist
## Rate is set to 2 Hz
# Import required libraries
import rospy
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
import numpy as np

# defining the class DataReporter
class Reporter:
    # Initializing variables with 0
    def __init__(self):
        self.d = 0
        self.e = 0
        self.e_bar = 0
        self.avl1 = 0
        self.avl2 = 0
        self.orientation_angle = 0
        self.linear_velocity = 0
        self.angular_velocity = 0

    # Fetches the variable values from sensed_object
    def variables_callback(self,msg):
        self.d = msg.position.x
        self.e = msg.position.y
        self.e_bar = msg.position.z
        self.avl1 = msg.orientation.x
        self.avl2 = msg.orientation.y
        self.orientation_angle = msg.orientation.z*180.0/np.pi

    # Sets linear and angular velocities with values from /cmd_vel
    def movement_callback(self, data):
        self.linear_velocity = data.linear.x
        self.angular_velocity = data.angular.z

    # Prints all the required values 
    def report_values(self):
        rospy.loginfo('Distance between robot and obstacle (d): %.3f meters', self.d)
        rospy.loginfo('Allowable tracking error distance (e): %.3f meters', self.e)
        rospy.loginfo('Normalized error (e_bar): %.3f meters', self.e_bar)
        rospy.loginfo('Orientation from obstacle (alpha): %.3f degrees', self.orientation_angle)
        rospy.loginfo('Linear velocity of lidar wrt a (x) avl1: %.3f m/s', self.avl1)
        rospy.loginfo('Linear velocity of lidar wrt a (y) avl2: %.3f m/s', self.avl2)
        rospy.loginfo('Linear velocity (v): %.3f meters/sec', self.linear_velocity)
        rospy.loginfo('Angular velocity (omega): %.3f degrees/sec', self.angular_velocity)

    def data_reporter(self):
        # Initialize node, subscriber and publisher
        rospy.init_node('data_reporter', anonymous=False)
        rospy.Subscriber('/cmd_vel', Twist, self.movement_callback)
        rospy.Subscriber('sensed_object', Pose, self.variables_callback)

        rate = rospy.Rate(2) # 2 Hertz
        while not rospy.is_shutdown():
            self.report_values()
            rate.sleep()

# main function
if __name__ == '__main__':
    try:
        # dr is the instance of class DataReporter
        rep = Reporter()
        # calling function data_reporter()
        rep.data_reporter()
    except rospy.ROSInterruptException:
        pass
