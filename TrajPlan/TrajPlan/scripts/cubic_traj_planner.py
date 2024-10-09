#!/usr/bin/env python3

from __future__ import print_function
import rospy
import sys
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj

def callback(data):
	rospy.loginfo('p0=%f,pf=%f,v0=%f,vf=%f,t0=%f,tf=%f', data.p0, data.pf, data.v0, data.vf, data.t0, data.tf)
	a0,a1,a2,a3 = compute_cubic_coeffsC(data.p0,data.pf,data.v0,data.vf,data.t0,data.tf)
	t0 = data.t0
	tf = data.tf
	cubic_traj_planner(a0,a1,a2,a3,t0,tf)

def listener():#listening out for any new messages from the ROS publisher with the name "points_generator"
	rospy.init_node('planner', anonymous=True)
	rospy.Subscriber('points_generator', cubic_traj_params, callback)
	rospy.spin()#prevents python from exiting until this node is stopped
	
def cubic_traj_planner(a0,a1,a2,a3,t0,tf):#sending the coefficients and initial and final times to the plotter node so it can be visualised
	pblsh = rospy.Publisher('cubic_traj', cubic_traj_coeffs, queue_size=15)
	rate = rospy.Rate(0.05) # 0.05hz
	rospy.loginfo('a0=%f, a1=%f, a2=%f, a3=%f, t0=%f, tf=%f', a0,a1,a2,a3,t0,tf)
	pblsh.publish(a0,a1,a2,a3,t0,tf)

def compute_cubic_coeffsC(p0,pf,v0,vf,t0,tf):
	rospy.wait_for_service('compute_cubic_trajec')#makes sure that service is available
	compute_cubictraj = rospy.ServiceProxy('compute_cubic_traj', compute_cubic_traj)#service that computes the coefficients from position and velocity data
	res = compute_cubictraj(p0,pf,v0,vf,t0,tf)
	return res.a0, res.a1, res.a2, res.a3#return 4 coefficients 
	
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
