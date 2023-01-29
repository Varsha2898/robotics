#!/usr/bin/env python

## This node publishes the values detected by the sensor to 
## topic name 'sensed_object' of type Pose at rate 10 Hz 
## This node subscribes to topic name '/scan' of type LaserScan
# Import required libraries
import numpy as np
import rospy
from geometry_msgs.msg import Pose
from sensor_msgs.msg import LaserScan

# Initializing L,e_max, Kp, e_bar values at the top for testing with different values
global L, e_max, Kp, e_bar, pose
L = 1  # length (m) at which the robot circumvents
e_max = 0.3  # Maximum allowable error (m)
Kp = 0.14  # Positive parameter
e_bar = 1
capture = Pose()

# Define lidar sensing function
def lidar_sensing(msg):
    
    ranges = msg.ranges

    # convert to numpy array to be able to use numpy functions
    npranges = np.array(ranges)
    # compute minimum distance and its corresponding angles with respect to scanner's frame
    d = np.nanmin(npranges)
    alpha = np.reshape( np.argwhere(npranges == d) , -1)
    e = d - L # Calculate error
    # returning these values
    return (d, alpha, e)

# Define lidar callback function
def callback(msg):
    try:
        ranges = msg.ranges
        # convert to numpy array to be able to use numpy functions
        npranges = np.array(ranges)
        # convert values out of range to 'NaN' to be ignored in calculation
        npranges[npranges > msg.range_max] = float('NaN')
        npranges[npranges < msg.range_min] = float('NaN')
        # Calculate d, alpha, e, e_bar, a_L, b_L
        d, alpha, e = lidar_sensing(msg)
        # given condition
        if e >= e_max:
            e_bar=1
        if (-e_max) < e and e < e_max:
            e_bar = e/e_max
        if e <= (-e_max):
            e_bar=-1
        a_L = Kp * e_bar
        b_L =  Kp*(1-abs(e_bar))
        c_L = (msg.angle_min + (alpha*msg.angle_increment))
        capture.position.x = d
        capture.position.y = e
        capture.position.z = e_bar
        capture.orientation.z = float(c_L)
        capture.orientation.x = a_L
        capture.orientation.y = b_L
        
        #publishing the values
        pub.publish(capture)
    except Exception as e:
        print()


# Initialize node and subscriber, publisher 
rospy.init_node('sensed_object', anonymous=False)
pub = rospy.Publisher('sensed_object', Pose, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)

while not rospy.is_shutdown():
    rate=rospy.Rate(10) #publishing rate being set to 10 Hz
    # rospy.spin()
    pub.publish(capture)
    rate.sleep()

