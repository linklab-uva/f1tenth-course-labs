#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from std_msgs.msg import Int32

from visualization_msgs.msg import Marker

from tf.transformations import quaternion_from_euler

sphere_marker_pub = rospy.Publisher("/sphere_marker", Marker, queue_size = 2)
arrow_marker_pub = rospy.Publisher("/arrow_marker", Marker, queue_size = 2)
prev_range = 0.0


def callback(data):
    
    global prev_range
    # pick out the middle range value (at index 540 - just an example)
    center = data.ranges[540]

    # If NaN, pipe though the previous non NaN value
    if math.isnan(center):
        center = prev_range
    
    prev_range = center
    mid = "Middle Range %s" % (center)
    rospy.loginfo(mid)


    # SPHERE MARKER

    sphere_marker = Marker()

    sphere_marker.header.frame_id = "car_9_laser"
    sphere_marker.header.stamp = rospy.Time.now()

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
    sphere_marker.type = 2
    sphere_marker.id = 0

    # Set the scale of the marker
    sphere_marker.scale.x = 0.2
    sphere_marker.scale.y = 0.2
    sphere_marker.scale.z = 0.2

    # Set the color
    sphere_marker.color.r = 0.0
    sphere_marker.color.g = 1.0
    sphere_marker.color.b = 0.0
    sphere_marker.color.a = 1.0

    # Set the pose of the marker
    sphere_marker.pose.position.x = center
    sphere_marker.pose.position.y = 0
    sphere_marker.pose.position.z = 0
    sphere_marker.pose.orientation.x = 0.0
    sphere_marker.pose.orientation.y = 0.0
    sphere_marker.pose.orientation.z = 0.0
    sphere_marker.pose.orientation.w = 1.0

    # Convert steering Euler angle (yaw) to quaternion
    #example_steering = 10
    #quaternion = quaternion_from_euler(0,0,example_steering) # args: Roll, Pitch, Yaw
    #sphere_marker.pose.orientation.x = quaternion[0]
    #sphere_marker.pose.orientation.y = quaternion[1]
    #sphere_marker.pose.orientation.z = quaternion[2]
    #sphere_marker.pose.orientation.w = quaternion[3]

    sphere_marker_pub.publish(sphere_marker)

    # ARROW MARKER

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
    arrow_marker = Marker()
    arrow_marker.header.frame_id = "car_9_laser"
    arrow_marker.type = 0
    arrow_marker.header.stamp = rospy.Time.now()
    arrow_marker.id = 1

    arrow_marker.scale.x = data.ranges[540]
    arrow_marker.scale.y = 0.1
    arrow_marker.scale.z = 0.1

    # Set the color
    arrow_marker.color.r = 0.0
    arrow_marker.color.g = 0.0
    arrow_marker.color.b = 1.0
    arrow_marker.color.a = 1.0

    arrow_marker_pub.publish(arrow_marker)

   
if __name__=='__main__':
    rospy.init_node("rviz_test", anonymous=False)   
    sub = rospy.Subscriber("/car_9/scan",LaserScan, callback)
    rospy.spin()

