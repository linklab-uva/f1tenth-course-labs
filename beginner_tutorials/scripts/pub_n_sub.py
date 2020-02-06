#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32

varS=None

def fnc_callback(msg):
    global varS
    varS=msg.data
   
if __name__=='__main__':
    rospy.init_node('pub_n_sub')
   
    sub=rospy.Subscriber('rand_no', Int32, fnc_callback)
    pub=rospy.Publisher('sub_pub', Int32, queue_size=1)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        if varS<= 2500:
            varP=0
        else:
             varP=1
   
        pub.publish(varP)
        rate.sleep()
