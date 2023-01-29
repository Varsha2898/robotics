#!/usr/bin/env python

## Uses the LiDAR sensor to sense the distance and the angle between 
## the husky and the obstacle relative to the scanner's reference frame
## when the LiDAR sensor is enabled

## Publishes to topic /location of type Pose2D
## Publishes at the rate of 2 Hz
## Subscribes to topic /scan of type LaserScan 

## Importing the dependencies or necessary libraries to the node

import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Pose2D

global x,theta
position_location=Pose2D()

def callback(msg):
    global position_location
    ranges = msg.ranges

    # converting numpy functions to numpy array
    numpyranges = np.array(ranges)

    # initializing NaN to more than and less than ranges of the sensor values
    numpyranges[numpyranges > msg.range_max] = float('NaN')
    numpyranges[numpyranges < msg.range_min] = float('NaN')

    # calculating the ditance from husky and the minimum distance of the object and the angle between the orientation of the husky and the obstacle
    minimum_distance = np.nanmin(numpyranges)
    angle = np.reshape( np.argwhere(numpyranges == minimum_distance) , -1)

    # assigning the distance and theta values to position_location.x, position_location.theta
    position_location.x = minimum_distance
    position_location.theta = float(((angle*msg.angle_increment)+msg.angle_min)*180.0/np.pi)
    rospy.loginfo('Minimum distance = %7.3f meters, Angles = %7.3f degrees', position_location.x , position_location.theta)
    
    # Publishing values of datatype Pose2D to the topic /location and size 1
    pub=rospy.Publisher('/location',Pose2D,queue_size=1)
    pub.publish(position_location)

def main_called():

    # initializing node sensed_object
    # anonymous = False stops duplicate publishers with the same name followed by unique numbers 
    rospy.init_node('sensed_object', anonymous=False)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

    # when the rospy is not shutdown, publish the data
    while not rospy.is_shutdown():
        # setting the publishing rate 2 Hz
        rate=rospy.Rate(2)
        pub.publish(position_location)
        # rate.sleep regulates and helps maintain the rate at which the data is publlished
        rate.sleep()

if __name__ == '__main__':
    try:
        main_called()
    except rospy.ROSInterruptException:
        pass
    