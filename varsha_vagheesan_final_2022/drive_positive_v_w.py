#!/usr/bin/env python

# Publishes linear and angular velocities to topic 'turtle1/cmd_vel' of type Twist
# Publishes at the rate of 10 Hz

# Import the necessary modules
import rospy
from geometry_msgs.msg import Twist
val = Twist()

# This function initializes the node and publisher
def drive_positive_v_w():
    global val
    rospy.init_node('drive_positive_v_w',anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Publishing velocity set to 10 Hz
    rate = rospy.Rate(10)  

    # Update_Velocity_Positive() called
    positive_driver = Update_Velocity_Positive()

    # when node not shutdown
    while not rospy.is_shutdown():
        pub.publish(positive_driver)
        rate.sleep()

# This function is used to set the linear and angular velocity values
def Update_Velocity_Positive():
    val.linear.x = 0.5  # m/s
    val.angular.z = 0.5  # rad/s
    return val

# main function 
if __name__ == '__main__':
    try:
        # drive_positive_v_w() function called
        drive_positive_v_w()
    except rospy.ROSInterruptException:
        pass
        
