#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    print data.ranges[540]

rospy.init_node("scan_test", anonymous=False)
sub = rospy.Subscriber("/car_1/scan", LaserScan, callback)
rospy.spin()
