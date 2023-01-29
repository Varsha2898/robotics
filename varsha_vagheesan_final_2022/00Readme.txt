*****Creating a package*****

1) Navigate to the path where you need to create the package (inside the src folder in this case) using the command
Command : cd ~/catkin_ws/src  

2) Create the package with the command 
catkin_create_pkg <package_name> [depend1] [depend2] [depend3] ...

In this case, our package name is varsha_vagheesan_final_2022 and the dependencies on which our package depends is rospy std_msgs geometry_msgs turtlesim
Command : catkin_create_pkg varsha_vagheesan_final_2022 rospy std_msgs geometry_msgs turtlesim

The package on creation gets created with CmakeLists.txt, package.xml files and an src folder.

3) The next step after creating the package is to 'Build'
We can either build the whole workspace or the specific package alone
Now navigating to the cd ~/catkin_ws directory by using the cd .. command to traverse back,
Command to build the whole workspace : catkin build
Command to buildthe specific package : catkin build <package_name>

For faster and more efficient results, I have built the specific package that I created using,
Command: catkin build varsha_vagheesan_final_2022
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
I have created three nodes - drive_positive_v_w.py, drive_negative_v_w.py, velocity_reporter.py using VS Code

3) A launch file (an xml file) is also created and saved to the Launch folder created inside the created package varsha_vagheesan_final_2022. 
The name of the launch file is varsha_vagheesan_final_2022.launch

4) To make the node files executable, use the command by getting to the directory where the python files are

cd catkin_ws/src/course_dir/varsha_vagheesan_final_2022/src
chmod +x <file_name1.py> <file_name2.py> <file_name3.py>
Command: chmod +x drive_positive_v_w.py drive_negative_v_w.py velocity_reporter.py 

cd catkin_ws/src/course_dir/varsha_vagheesan_final_2022/Launch
Command: chmod +x varsha_vagheesan_final_2022.launch

5) To check whether these are executable files, enter the command
ls -al
If the files are displayed in green colour, they are executable; if not they are not

6) Now, since we have added the node files or the python files and the launch file to the package, we need to re-build and re-source the package. 

7) Build the package again by navigating to the workspace using cd ~/catkin_ws and type the command 
catkin build <package_name> to build the specific package
Command : catkin build varsha_vagheesan_final_2022
or to build the whole workspace
Command : catkin build

8) Source the package again using the command 
source ~/catkin_ws/devel/setup.bash


*****Removing Files******

1) To remove a file from the package, go to the folder in which the file exists and remove the file manually.

2) Since the package is altered, re-build the package using catkin build <package_name> to build the specific package
Command : catkin build varsha_vagheesan_final_2022

3) Source the package again using the command 
Command: source ~/catkin_ws/devel/setup.bash

*****To Launch the Gazebo, Spawn two instances of Turtlesim, Spawn Turtlebot3, rqt_graph and Run the nodes using the launch file*****

1) An xml file with .launch extension is created, which saved in the Launch folder created inside the package varsha_vagheesan_final_2022 

2) When this launch file is launched, it launches gazebo, spawns two instances of turtlesim, spawns turtlebot3 of model 
type burger, rqt_graph and runs all three nodes drive_positive_v_w.py, drive_negative_v_w.py and velocity_reporter.py
Command: roslaunch <package_name> <launch_file_name.launch>
Command: roslaunch varsha_vagheesan_final_2022 varsha_vagheesan_final_2022.launch

*****Test conditions*****

1) In this condition, the default value of simulate_with_turtlesim is 1. Hence, two instances of turtlesim are spawned and they follow drive_positive_v_w.py. One turtlesim acts as turtlesim_node_leader.
This is the main node, which will be the required node. If this node is killed the other turtlesim and rqt_graph will be killed. The other turtlesim instance is the turtlesim_node_follower.
This follower node gets respawned multiple times until the leader node is killed.
Command: roslaunch varsha_vagheesan_final_2022 varsha_vagheesan_final_2022.launch

2) In this condition, the gazebo is launched along with turtlebot3 and it follows drive_negative_v_w.py node. The turtlebot3 gets spawned by default at (x,y) = (5,5) position (as per the question). 
Command: roslaunch varsha_vagheesan_final_2022 varsha_vagheesan_final_2022.launch simulate_with_turtlesim:=0

3) In this condition, the user can enter x and y positions where the turtlebot3 is to be spawned by entering the following command
Command: roslaunch varsha_vagheesan_final_2022 varsha_vagheesan_final_2022.launch simulate_with_turtlesim:=0 x_tbot3:= <value> y_tbot3:= <value>
Example: roslaunch varsha_vagheesan_final_2022 varsha_vagheesan_final_2022.launch simulate_with_turtlesim:=0 x_tbot3:= 3 y_tbot3:= 3

4) To better understand the communication between the nodes, we can display a dynamic graph.
The dynamic graph displays what ROS nodes communicate with what other nodes and the topics too. This gets launched with the launch file as well.

