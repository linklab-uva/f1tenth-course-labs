#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from random import randint

#a function to generate the random number
def generate_random_number():
    rnd= randint(0,5000)
    return rnd

if __name__=='__main__':
    rospy.init_node('random_number')
    pub=rospy.Publisher('rand_no', Int32, queue_size=10)
    rate= rospy.Rate(5)

    while not rospy.is_shutdown():
        rnd_gen=generate_random_number()
       
        if rnd_gen<=2500:
         rospy.loginfo("The number generated is lower than 2500: %s", rnd_gen)
         pub.publish(rnd_gen)
        else:
         rospy.loginfo("The number generated is higher than 2500: %s", rnd_gen)
         pub.publish(rnd_gen)

rate.sleep()
