#!/usr/bin/env python3

from __future__ import print_function
import rospy
import numpy as np
from ar_week5_test.srv import compute_cubic_traj, compute_cubic_trajResponse

def compute_cubic_coeffs():
	rospy.init_node('compute_cubic_coeffs')
	s = rospy.Service('compute_cubic_traj', compute_cubic_traj, CFout)#create new service that takes data from service file compute_cubic_traj and updates the results
	rospy.spin()#prevents python from exiting

def CFout(req):#calculates coefficients using a=(M^-1)*C
    M = np.array([[1, req.t0, req.t0**2, req.t0**3],[0, 1, 2*req.t0, 3*req.t0**2],[1, req.tf, req.tf**2, req.tf**3],[0, 1, 2*req.tf, 3*req.tf**2]])
    M_inv = np.linalg.inv(M)#Inverse matrix
    c = np.array([req.p0, req.pf, req.v0, req.vf])
    res = np.matmul(M_inv, c)#multiply
    return compute_cubic_trajResponse(res[0],res[1],res[2],res[3])#return to service that requested it
        

if __name__ == '__main__':
    try:
        compute_cubic_coeffs()
    except rospy.ROSInterruptException:
        pass
