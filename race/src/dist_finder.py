#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input
# Import whatever else you think is necessary

# Some useful variable declarations.
angle_range = 0		# sensor angle range of the lidar
car_length = 1.5	# distance (in m) that we project the car forward for correcting the error. You may want to play with this.
desired_trajectory = 1	# distance from the wall (left or right - we cad define..but this is defined for right). You should try different values
vel = 20 		# this vel variable is not really used here.
error = 0.0

# publish to the topic /team_name/error e.g. /team_alpha/error
pub = rospy.Publisher('/team_name/error', pid_input, queue_size=10)

##	Input: 	data: Lidar scan data
##			theta: The angle at which the distance is requried
##	OUTPUT: distance of scan at angle theta

def getRange(data,theta):
# Find the index of the arary that corresponds to angle theta.
# Return the lidar scan value at that index
# Do some error checking for NaN and ubsurd values
## Your code goes here

	return

def callback(data):
	theta = 50;
	a = getRange(data,theta)
	b = getRange(data,0)	# Note that the 0 implies a horizontal ray..the actual angle for the LIDAR may be 30 degrees and not 0.
	swing = math.radians(theta)

	## Your code goes here to compute alpha, AB, and CD..and finally the error.




	## END

	msg = pid_input()
	msg.pid_error = error		# this is the error that you want to send to the PID for steering correction.
	msg.pid_vel = vel		# velocity error is only provided as an extra credit field.
	pub.publish(msg)


if __name__ == '__main__':
	print("Laser node started")
	# name your node team_name_dist_finder e.g. team_alpha_dist_finder
	rospy.init_node('team_name_dist_finder',anonymous = True)

	# subscribe to the correct /team_name/scan topic for your team's car..
	rospy.Subscriber("/team_name/scan",LaserScan,callback)

	rospy.spin()
