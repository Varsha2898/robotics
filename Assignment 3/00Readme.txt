*****Creating a package*****

1) Navigate to the path where you need to create the package (inside the src folder in this case) using the command
Command : cd ~/catkin_ws/src  

2) Create the package with the command 
catkin_create_pkg <package_name> [depend1] [depend2] [depend3] ...

In this case, our package name is assignment3_pkg and the dependencies on which our package depends is rospy sensor_msgs geometry_msgs nav_msgs
Command : catkin_create_pkg assignment3_pkg rospy sensor_msgs geometry_msgs nav_msgs

The package on creation gets created with CmakeLists.txt, package.xml files and an src folder.

3) The next step after creating the package is to 'Build'
We can either build the whole workspace or the specific package alone
Now navigating to the cd ~/catkin_ws directory by using the cd .. command to traverse back,
Command to build the whole workspace : catkin build
Command to buildthe specific package : catkin build <package_name>

For faster and more efficient results, I have built the specific package that I created using,
Command: catkin build assignment3_pkg 
in the cd ~/catkin_ws directory

If we need to build multiple packages at once, the command to do it is as follows,
catkin build <package_name1> <package_name2>

4) The next step after building is to 'Source'
The command to source is 
Command: source ~/catkin_ws/devel/setup.bash

******Adding Files******

1) Now, we need to add the python files that contains the code to the created directory.
The python files are to be added inside the src folder inside our created package.

2) I used Visual Studio Code as the Development environment to develop the python files and save them to the src folder of the created package.
I have created two nodes - sensed_object.py, navigate_robot.py using VS Code

3) Now, since we have added the node files or the python files to the package, we need to re-build and re-source the package. 

4) Build the package again by navigating to the workspace using cd ~/catkin_ws and type the command 
catkin build <package_name> to build the specific package
Command : catkin build assignment3_pkg 
or to build the whole workspace
Command : catkin build

5) Source the package again using the command 
source ~/catkin_ws/devel/setup.bash

6) To make the node files executable, use the command
chmod +x <file_name1.py> <file_name2.py>
Command: chmod +x sensed_object.py navigate_robot.py 

7) To check whether these are executable files, enter the command
ls -al
If the files are displayed in green colour, they are executable; if not they are not

*****Removing Files******

1) To remove a file from the package, go to the folder in which the file exists and remove the file manually.

2) Since the package is altered, re-build the package using catkin build <package_name> to build the specific package
Command : catkin build assignment3_pkg

3) Source the package again using the command 
Command: source ~/catkin_ws/devel/setup.bash

*****To launch the Husky*****

1) To enable the LiDAR sensor, use the following command in a new terminal
Command : export HUSKY_LMS1XX_ENABLED=1

2) To spawn/launch the Husky in a new window , we need to enter a command.
Command : roslaunch husky_gazebo husky_empty_world.launch
Husky gets spawned in the Gazebo environment

3) Pick and place any obstacle from the environment and use the following command to check the working of the LiDAR sensor
Command : rostopic echo -n 1 /scan

4) To view the sensed object, launch rviz and observe the outline of the sensed object
Command : rviz

*****Running a node*****

1) Make sure that the husky gazebo has been started using the command 
roslaunch husky_gazebo husky_empty_world.launch

3) To run the sensed_object node:
To run a node, open a new terminal and navigate to the workspace using cd ~/catkin_ws command and enter the following
rosrun <package_name> <node_name>
Command : rosrun assignment3_pkg sensed_object.py

4) To run the navigate_robot node:
To run a node, navigate to the workspace using cd ~/catkin_ws command and enter the following
rosrun <package_name> <node_name>
Command : rosrun assignment3_pkg navigate_robot.py

6) After all the nodes are run, observe the outputs in the (navigate_robot) node terminals.

7) Note the husky move as per the inputs given, in the gazebo window.

8) To better understand the communication between the nodes, we can display a dynamic graph.
The dynamic graph displays what ROS nodes communicate with what other nodes and the topics too
Command : rosrun rqt_graph rqt_graph 
or 
Command : rqt_graph

*****Miscellaneous*****

1) To list all the files inside a node,
Command : rosnode list

2) To stop the node from running, enter the following command
Command : rosnode kill /node_name