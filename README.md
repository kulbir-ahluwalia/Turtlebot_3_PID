# Turtlebot3
ROS package to simulate Turtlebot 3 Waffle/ Burger in Gazebo. The turtlebot starts at a random position and goes to the goal position input by the user.

The following packages need to be installed first:-
```
$ sudo apt-get install ros-kinetic-ar-track-alvar
$ sudo apt-get install ros-kinetic-ar-track-alvar-msgs
```

Go to the source folder of the catkin_ws workspace:-
```
cd ~/catkin_ws/src/ 
```

Then, clone the following repositories into your workspace:-
```
 
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git   
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git   
git clone https://github.com/ROBOTIS-GIT/turtlebot3_applications_msgs.git  
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git  
git clone https://github.com/ROBOTIS-GIT/turtlebot3_applications.git  
```

Change the working directory to catkin_ws and then use catkin_make:-
```
cd ~/catkin_ws && catkin_make 
```

Reference - ROS Robot Programming book - Page 285 - https://www.pishrobot.com/wp-content/uploads/2018/02/ROS-robot-programming-book-by-turtlebo3-developers-EN.pdf

Run final.py by going into:-
```
~/catkin_ws/src/Turtlebot3/control_bot/src$
```



Install these packages:-
```
sudo apt-get install ros-kinetic-teleop-twist-keyboard  
sudo apt-get install ros-kinetic-turtlebot3
sudo apt-get install ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
```
Source the catkin workspace:-
```
source devel/setup.bash
```

Then, export the type of Turtlebot3 that you want.
```
export TURTLEBOT3_MODEL=waffle #for waffle  
export TURTLEBOT3_MODEL=burger #for burger  
```
To open empty world in gazebo with Turtlebot3 in it:-
```
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch  
```








