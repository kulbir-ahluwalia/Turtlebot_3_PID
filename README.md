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






