#!/usr/bin/env python

import rospy
import math
from visualization_msgs.msg import Marker

def talker():
	pub = rospy.Publisher('telemetry', Marker, queue_size=100)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(90)
	count = 0
	while not rospy.is_shutdown():
		marker = Marker()
   		marker.header.frame_id = "map"
		marker.type = marker.SPHERE
		marker.action = marker.ADD
		marker.scale.x = 3
		marker.scale.y = 3
		marker.scale.z = 3
		marker.color.a = 1.0
		marker.color.r = 1.0
		marker.color.g = 1.0
		marker.color.b = 0.0
		marker.pose.orientation.w = 1.0
		marker.pose.position.x = 4*math.cos(2*math.pi*count/900.0)
		marker.pose.position.y = 4*math.sin(2*math.pi*count/900.0) 
		marker.pose.position.z = count/900.0 - 1 
		count = count + 1
		pub.publish(marker)
		rate.sleep()
		count %= 1800
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
