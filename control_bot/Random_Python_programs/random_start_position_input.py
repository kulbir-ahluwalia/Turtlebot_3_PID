#! /usr/bin/python

# generate random Gaussian values
import numpy as np
import rospy
from geometry_msgs.msg import Twist, Point, Quaternion, Pose
from nav_msgs.msg import Odometry
import tf
from tf.transformations import euler_from_quaternion

from tf2_msgs.msg import TFMessage

def odom_callback(odometry):

    global initial_position

    quaternion = tf.transformations.quaternion_from_euler(0,0, initial_position[2])

    position = Pose()

    position.position.x = initial_position[0]
    position.position.y = initial_position[1]

    position.orientation.x = quaternion[0]
    position.orientation.y = quaternion[1]
    position.orientation.z = quaternion[2]
    position.orientation.w = quaternion[3]

    # print("Position is {}".format(position))

    goal_x = initial_position[0]
    goal_y = initial_position[1]

    lin_pos,rot_pos = get_odom()
    velocity = Twist()

    goal_distance = np.sqrt(np.power(goal_x - lin_pos.x, 2) + np.power(goal_y - lin_pos.y, 2))
    distance = goal_distance

    linear_speed = 1

    while distance > 0.05:

        # print("Target is {}".format(goal_x))
        # print(distance)

        lin_pos,rot_pos = get_odom()

        print(lin_pos)

        x_start = lin_pos.x
        y_start = lin_pos.y

        velocity.linear.x = min(linear_speed * distance, 0.1)
        velocity.linear.y = 0
        # velocity.linear.z = 0
        # velocity.angular.x = 0
        # velocity.angular.y = 0
        velocity.angular.z = 0

        distance = np.sqrt(np.power((goal_x - x_start), 2) + np.power((goal_y - y_start), 2))

        vel_pub.publish(velocity)

    # print("Velocity is {}".format(velocity))

def get_odom():
    try:
        (trans, rot) = tf_listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))
        rotation = euler_from_quaternion(rot)

    except (tf.Exception, tf.ConnectivityException, tf.LookupException):
        rospy.loginfo("TF Exception")
        return
 
    return (Point(*trans), rotation[2])


if __name__ == '__main__':
    # try:
    #     self.tf_listener.waitForTransform(self.odom_frame, 'base_footprint', rospy.Time(), rospy.Duration(1.0))
    #     self.base_frame = 'base_footprint'
    # except (tf.Exception, tf.ConnectivityException, tf.LookupException):
    #     try:
    #         self.tf_listener.waitForTransform(self.odom_frame, 'base_link', rospy.Time(), rospy.Duration(1.0))
    #         self.base_frame = 'base_link'
    #     except (tf.Exception, tf.ConnectivityException, tf.LookupException):
    #         rospy.loginfo("Cannot find transform between odom and base_link or base_footprint")
    #         rospy.signal_shutdown("tf Exception")

    initial_position = 0

    print("Please enter the lower range for generating x and y coordinates for the starting position of Turtlebot")
    lower = input()

    print("Please enter the upper range for generating x and y coordinates for the starting position of Turtlebot")
    upper = input()

    print("Random initial X and Y coordinates of the Turtlebot are:-")

    coord = np.random.uniform(lower, upper, 2) 
    print('Initial X coordinate: ', coord[0])
    print('Initial Y coordinate: ', coord[1])

    print("Please enter the lower range for generating angle wrt x axis for the starting position of Turtlebot in degrees")
    lower_angle = input()

    print("Please enter the upper range for generating angle wrt x axis for the starting position of Turtlebot in degrees")
    upper_angle = input()

    angle = np.random.uniform(lower_angle, upper_angle, 1) 
    print('Initial starting angle Theta wrt +X axis: ', angle[0])

    #initial_position = coord + angle
    initial_position = np.concatenate((coord,angle))

    #print('(X, Y, Theta):' ,coord[0], coord[1], angle[0])
    print('Final pose is:-')
    print('(X, Y, Theta):', initial_position[0], initial_position[1], initial_position[2])

    print(initial_position)



    ### ROS STUFF!


    rospy.init_node('turtlebot3_controller')

    tf_listener = tf.TransformListener()
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/tf', TFMessage, odom_callback)

    rospy.spin()







