#!/usr/bin/env python

# Publishes linear and angular velocities to topic 'turtle1/cmd_vel' of type Twist
# Publishes at the rate of 10 Hz

# Import the necessary modules
import rospy
from geometry_msgs.msg import Twist
val = Twist()

# This function initializes the node and publisher
def drive_negative_v_w():
    global val
    rospy.init_node('drive_negative_v_w',anonymous=False)
    pub_to_turtle1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Publishing velocity set to 10 Hz
    rate = rospy.Rate(10)  

    # Update_Velocity_Negative() called
    negative_driver = Update_Velocity_Negative()

    # when node not shutdown
    while not rospy.is_shutdown():
        pub_to_turtle1.publish(val)
        pub.publish(val)
        rate.sleep()

# This function is used to set the linear and angular velocity values
def Update_Velocity_Negative():
    val.linear.x = -0.5  # m/s
    val.angular.z = -0.5  # rad/s
    return val

# main function 
if __name__ == '__main__':
    try:
        # drive_negative_v_w() function called
        drive_negative_v_w()
    except rospy.ROSInterruptException:
        pass
        
