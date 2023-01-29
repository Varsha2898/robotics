#!/usr/bin/env python

# Subscribes from topic 'turtle1/cm_vel' of type Twist and 
# publishes to topic 'velocity_reporter_topic' of type Twist
# Publishes at the rate of 1 Hz

# Import the necessary modules
import rospy
from geometry_msgs.msg import Twist
velocity = Twist()

# defining the class Reporter
class Reporter:
    # this function publishes the values to 'velocity_reporter_topic 
    def velocity_reporter(self):
        global rep,pub
        rep = Reporter()
        pub = rospy.Publisher('/velocity_reporter_topic', Twist, queue_size=10)
        rate = rospy.Rate(1)  # publishing rate = 1 Hz
        pub.publish(velocity)    
    
    # This print_callback() function prints the 
    def print_callback(self, velocity):
        global publish_values,rep
        rep = Reporter()
        # Print the linear and angular velocities obtained from the subscribed topic
        rospy.loginfo("Linear Velocity of the robot: %.3f m/s",velocity.linear.x)
        rospy.loginfo("Angular Velocity of the robot: %.3f rad/s",velocity.angular.z )

        # publish_values calls the velocity_reporter function
        publish_values = rep.velocity_reporter()

# This test() function initiates the node 'velocity_reporter' and subscribes to the '/turtle1/cmd_vel' topic
def test():
    rep = Reporter()
    # Initializing the node
    rospy.init_node('velocity_reporter', anonymous = False)
    # sub listens to the /turtle1/cmd_vel topic
    sub = rospy.Subscriber('/turtle1/cmd_vel', Twist, rep.print_callback)

    # Spin keeps the node running until the node is shut down
    rospy.spin() 

if __name__ == '__main__':
    try:
        # calls test() function
        test()
    except rospy.ROSInterruptException:
        pass
