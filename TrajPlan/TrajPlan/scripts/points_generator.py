#!/usr/bin/env python3
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
import rospy
import random

ompute_cubic_trajec
def points_generator():
	pblsh = rospy.Publisher('points_generator', cubic_traj_params, queue_size=10)
	rospy.init_node('points', anonymous=True)
	rate = rospy.Rate(0.05) # 0.05hz
	while not rospy.is_shutdown():
		dt = random.uniform(5, 10) 
		p0 = random.uniform(-10, 10) 
		pf = random.uniform(-10, 10)
		v0 = random.uniform(-10, 10)
		vf = random.uniform(-10, 10)
		t0 = 0
		tf = t0 + dt
		rospy.loginfo('pf=%f,,vf=%f,v0=%f,t0=%f,tf=%f,p0=%f', p0,pf,v0,vf,t0,tf)
		pblsh.publish(p0,pf,v0,vf,t0,tf)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		points_generator()
	except rospy.ROSInterruptException:
		pass

