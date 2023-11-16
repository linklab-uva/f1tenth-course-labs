#!/usr/bin/env python

# Import necessary libraries
import rospy
import sys
import math
import atexit
import os
import csv
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

# Retrieve car name, trajectory name, and visualization flag from command line arguments
car_name        = str(sys.argv[1])
trajectory_name = str(sys.argv[2])
visualize       = bool(sys.argv[3])

# Global variables for path tracking and waypoint logging
global seq
global prev_x
global prev_y

plan            = []
frame_id        = 'map'
seq             = 0
prev_x          = 0.0
prev_y          = 0.0
path_resolution = 0.1
# path_resolution is the the minimum distance the car needs to travel in order to log a new waypoint

# Initialize a ROS publisher for path visualization if enabled
if visualize:
    # Topic for visualizing the path in Rviz
    path_pub        = rospy.Publisher('/trajectory_builder/visualize_path', Path, queue_size = 1)
    path            = Path()
    visualize_resolution = 0.5

def save_plan():
    # Function to save the planned path into a CSV file
    # Modify the file path below to match the path on the racecar
    file_path = os.path.expanduser('/home/maxwell/catkin_ws/src/f1tenth_purepursuit/path/{}.csv'.format(trajectory_name))
    with open(file_path, mode = 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)
        for index in range(0, len(plan)):
            csv_writer.writerow([plan[index][0],
                                 plan[index][1],
                                 plan[index][2],
                                 plan[index][3]])

# Register the save_plan function to be called on exit
atexit.register(save_plan)

def odom_callback(data):
# Callback function for odometry updates

    global seq
    global prev_x
    global prev_y

    # Round current position to two decimal places
    curr_x = round(data.pose.position.x, 2)
    curr_y = round(data.pose.position.y, 2)

    # Log new waypoint if the distance from the previous waypoint is greater than the path_resolution
    if math.sqrt(math.pow(curr_x - prev_x, 2) + math.pow(curr_y - prev_y, 2)) > path_resolution:
        point = []
        point.append(curr_x)
        point.append(curr_y)
        point.append(0.0)
        point.append(1.0)
        plan.append(point)
        prev_x = curr_x
        prev_y = curr_y
        rospy.loginfo('pose logged')

    # Visualize the path if enabled
    if visualize:
        path.header.seq = seq
        path.header.stamp = rospy.Time.now()
        path.header.frame_id = frame_id

        # Populate the Path message with waypoints for visualization
        if len(plan) > 0:
            for index in range(0, len(plan)):
                waypoint = PoseStamped()
                waypoint.header.frame_id    = frame_id
                waypoint.pose.position.x    = plan[index][0]
                waypoint.pose.position.y    = plan[index][1]
                waypoint.pose.orientation.z = plan[index][2]
                waypoint.pose.orientation.w = plan[index][3]
                path.poses.append(waypoint)

        seq = seq + 1
        path_pub.publish(path)
    

if __name__ == '__main__':
    try:
        rospy.init_node('trajectory_builder', anonymous = True)
        rospy.Subscriber('/{}/particle_filter/viz/inferred_pose'.format(car_name), PoseStamped, odom_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
