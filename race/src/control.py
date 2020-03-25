#!/usr/bin/env python

import rospy
from race.msg import pid_input
from ackermann_msgs.msg import AckermannDrive

kp = 14.0
kd = 0.09
servo_offset = 0	# zero correction offset in case servo is misaligned. 
prev_error = 0.0 
vel_input = 25.0	# arbitrarily initialized. 25 is not a special value. This code can accept input desired velocity from the user.

pub = rospy.Publisher()
# setup a publisher to publish to the /car_x/offboard/command topic for your racecar.

def control(data):
	global prev_error
	global vel_input
	global kp
	global kd

	## Your code goes here
	# 1. Scale the error 
	# 2. Apply the PID equation on error to compute steering
	# 3. Make sure the steering value is within bounds
 	

	## END

	msg = drive_param();
	msg.velocity = vel_input	
	msg.angle = angle
	pub.publish(msg)

if __name__ == '__main__':
	global kp
	global kd
	global vel_input
	print("Listening to error for PID")
	kp = input("Enter Kp Value: ")
	kd = input("Enter Kd Value: ")
	vel_input = input("Enter Velocity: ")
	rospy.init_node('pid_controller', anonymous=True)
	rospy.Subscriber("error", pid_input, control)
	rospy.spin()
