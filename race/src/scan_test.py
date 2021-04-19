#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    print data.ranges[540]

# Make sure to rename the node to <team_name>_scan_test, e.g. team_alpha_scan_test
rospy.init_node("team_name_scan_test", anonymous=False)
# Replace team_name in the topic below with your team's name: e.g. team_alpha
sub = rospy.Subscriber("/team_name/scan", LaserScan, callback)
rospy.spin()
