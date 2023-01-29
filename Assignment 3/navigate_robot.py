#!/usr/bin/env python

## Subscribes to topic /location of type Pose2D
## Subscribes to topic /odometry/filtered of type of Odometry

## Importing the dependencies or necesarry libraries to the node

import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Pose2D,Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import pow,sqrt

# Initializing values to variables

roll = pitch = yaw = 0.0

# Intriducing variables and assigning values according to the question
global e,buffer_dist,closest_dist, E,flag,yaw_val 
yaw_val = 0
flag=0
e=0.7
E=0.35
global total_distance, destination
# Initializing destination = False and total_distance = 0
destination = False 
total_distance = 0

print('Distance at which the robot runs = 0.7m')
print('Distance at which the husky should stop after circumventing the object = 0.35m')
print('A small buffer distance is added along with these values')

## Defining the HuskyDriver class
class HuskyDriver:

    def callodom(self, position):
        global orient
        orient=position.pose.pose.orientation
        orientlist=[orient.x , orient.y ,orient.z , orient.w]
        global roll,pitch,yaw
        (roll,pitch,yaw)= euler_from_quaternion (orientlist)
        # prints the yaw value of the husky
        print ("yaw value: ", yaw)

    # this function stops sensing
    def stop_sensing(self):
        rospy.signal_shutdown("ROS has stopped")  

    # this function is used to move the robot/husky and publishes the cmd_vel
    def move_my_bot(self, msg):
        global pose, total_distance, destination
        pose=msg
        publi=rospy.Publisher('/husky_velocity_controller/cmd_vel',Twist,queue_size=10)
        global go_bot
        go_bot=Twist()
        # buffer value of 0.3 is added to the value 0.7 and 0.1 to 0.7 for stopping distance
        buffer_dist = e + 0.30
        closest_dist = e + 0.1 
        # if this condn is satisfied the husky moves forward
        if pose.x>buffer_dist and not destination:
            self.move_straight()
        
        # if this condn is satisfied the husky rotates/turns
        elif pose.x <= buffer_dist and pose.x > closest_dist and not destination:
            self.turn_bot()
        if destination:
            print(pose.theta, pose.x)
            # the conditions are written for -3 to +3 range of sensing
            if pose.theta > -3 and pose.theta < 3 and pose.x <= E:
                print ('first condition')
                go_bot.linear.x = 0
                go_bot.linear.z = 0
                publi.publish(go_bot)
                self.stop_sensing()
            # the conditions are written for -1 to +1 range of sensing
            if pose.theta > -1 and pose.theta < 1 and pose.x > E:
                print ('second condition')
                go_bot.linear.x = 0.3
                go_bot.linear.z = 0
            elif pose.theta < -3 and pose.x >= E:
                print ('third condition')
                go_bot.linear.x = 0.8
                go_bot.linear.z = 0.3
                self.stop_sensing()
            elif pose.theta > 3 and pose.x >= E:
                print ('fourth condition')
                go_bot.linear.x = 0
                go_bot.linear.z = 0.3
        # if pose.x is less than 1.5, calculate the total distance travelled by the husky
        if pose.x < 1.5:
            total_distance += go_bot.linear.x
            if total_distance >= 360 and total_distance <370:
                print ('--------------')
                go_bot.linear.x = 0.0
                go_bot.angular.z = -0.3
                print ('***************')
                destination = True
                
        publi.publish(go_bot) 

    # function to move the husky straight
    def move_straight(self):
        buffer_dist = e + 0.5
        closest_dist = e + 0.25 
        if (pose.theta>1 and pose.x>e):
            go_bot.angular.z=-0.5
            go_bot.linear.x=0.15
        elif (pose.theta<-1 and pose.x>e):
            go_bot.angular.z=0.5
            go_bot.linear.x=0.15
        elif (pose.theta<=1 and pose.theta>=-1 and pose.x>e):
            go_bot.linear.x=0.5
            go_bot.angular.z=0.0

    #function to turn the husky
    def turn_bot(self):
        go_bot.angular.z=0.3
        go_bot.linear.x=0.0
    
        # range of sensing is set to 87 deg to 93 deg
        if pose.theta>87 and pose.theta<93 and pose.x<=e:
            go_bot.linear.x=0.0
            go_bot.angular.z=0.2

        if pose.theta>93 and pose.x<e:
                go_bot.linear.x=0.0
                go_bot.angular.z=-0.2
        if pose.theta<87 and pose.x<e:
                go_bot.linear.x=0.0
                go_bot.angular.z=0.2
        if pose.theta>87 and pose.theta<93 and pose.x==e:
                go_bot.linear.x=0.2
                go_bot.angular.z=0.0    

    def final(self):
        rospy.init_node('navigate_robot', anonymous=False)
        rospy.Subscriber('/location', Pose2D, self.move_my_bot)
        rospy.Subscriber('/odometry/filtered', Odometry , self.callodom)
        rospy.spin()

# main function
if __name__ == '__main__':
   hd = HuskyDriver()
   hd.final()

