#!/usr/bin/env python

## This node publishes the values to topic name '/cmd_vel' of type Twist
## This node subscribes to topic name 'sensed_object' of type Pose
## Rate is set to 10 Hz
# Import required libraries
import rospy
import math
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

# defining the class Navigate_bot
class Navigate_bot():
    def __init__(self):
        # Initializing the node
        rospy.init_node('drive_robot', anonymous=False)
        
    # Fetches the values from sensed_object and assigns it to variables
    def speed_of_robot(self, msg):

        global pose
        self.pose = msg
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.alpha=self.pose.orientation.z
        self.vx=self.pose.orientation.x
        self.vy=self.pose.orientation.y
        self.d= self.pose.position.x
        self.e= self.pose.position.y
        self.e_bar=self.pose.position.z
        self.xl=-0.032 #Obtained from sub divisionn a
        self.yl=0 #Obtained from sub divison a
        self.theta=0.0 #Obtained from sub division a

        # Initialize self.vel_msg = Twist message
        self.vel_msg = Twist()
        print(self.d)
        # Check if object is within sensing range and stop when sensed value is 'inf'
        if self.d<float('inf'):

            # Calculating linear and angular velocities            
            self.vel_msg.linear.x = self.vx*math.cos(self.theta+self.alpha)+self.vx*(self.yl/self.xl)*(math.sin(self.theta+self.alpha))+self.vy*(-math.sin(self.theta+self.alpha))+self.vy*(self.yl/self.xl)*(math.cos(self.theta+self.alpha))
            self.vel_msg.angular.z = self.vx*(1/self.xl)*(math.sin(self.theta+self.alpha))+self.vy*(1/self.xl)*(math.cos(self.theta+self.alpha))
    
        else:
            # Stop robot if no object is within sensing range
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = 0
        rospy.Rate(10) # 10 Hz
        self.pub.publish(self.vel_msg)


def drive_robot():
    # nr is the instance of class Navigate_bot
    nr = Navigate_bot()
    # Initialize subscriber and publisher
    sub = rospy.Subscriber('sensed_object', Pose, nr.speed_of_robot)
    rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()


# Main function
if __name__ == '__main__':
    try:
        # calling drive_robot() function
        drive_robot()
    except rospy.ROSInterruptException:
        pass
        
