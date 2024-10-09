#!/usr/bin/env python3
from ar_week5_test.msg import cubic_traj_coeffs
from std_msgs.msg import Float64
import rospy

def callback(info):
	rospy.loginfo('a0=%f,a1=%f,a2=%f,a3=%f,t0=%f,tf=%f', info.a0, info.a1, info.a2, info.a3, info.t0, info.tf)
	t0 = info.t0
	tf = info.tf
	a0 = info.a0
	a1 = info.a1
	a2 = info.a2
	a3 = info.a3
	print(info.a0, info.a1, info.a2, info.a3, info.t0, info.tf)
	plot_traj(a0,a1,a2,a3,t0,tf)

	
def plot_traj(a0,a1,a2,a3,t0,tf):
	v = rospy.Publisher('Vel', Float64, queue_size = 10)
	p = rospy.Publisher('Pos', Float64, queue_size = 10)
	a = rospy.Publisher('Acc', Float64, queue_size = 10)
	
	rate = rospy.Rate(100/tf)
	for t in range(0,100):
		vel=a1+2*a2*(t/100)*tf+3*a3*(t/100)*tf*(t/100)*tf
		v.publish(vel)
		pos = a0+a1*(t/100)*tf+a2*(t/100)*tf*(t/100)*tf+a3*(t/100)*tf*(t/100)*tf*(t/100)*tf
		p.publish(pos)
		acc = 2*a2+6*a3*(t/100)*tf
		a.publish(acc)
		
		rate.sleep()
		
def listener():
	rospy.init_node('plotter', anonymous=True)
	rospy.Subscriber('cubic_traj', cubic_traj_coeffs, callback)
	rospy.spin()
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
