#!/usr/bin/env python

""" 
Created on 06-01-2021

@Author: Stefan Bonhof

look_to_point.py contains... a class that uses 
the point_head_action server to make tiago look to 
a point (currently any tf link) using the action
instead of publishing to the  
/head_controller/point_head_action/goal topic 
"""

# ROS imports
import rospy
import actionlib
from rospy import client
import tf.transformations
from look_to_point import LookToPoint

# ROS messages imports
from control_msgs.msg import PointHeadActionGoal, PointHeadAction
import geometry_msgs.msg
from geometry_msgs.msg import PointStamped

        
class LookToPointServer():

    def __init__(self):
        """Node to look at certain points"""

        # Launch Client and wait for server
        #self._action_name = "look_to_point_server"
        #self._as = actionlib.SimpleActionServer(self._action_name, PointHeadAction, execute_cb=self.execute_cb, auto_start = False)
        #self._as.start()


    def run(self): #earlier was (self,point)
	point = geometry_msgs.msg.Point()
        point.x = 1.0
        point.y = 0.0
        point.z = 1.0
	head_control = LookToPoint()
	rospy.sleep(1.0)
	
	point.y = -0.7	
	head_control.run(point)
	
	rospy.sleep(1.0)
	
	point.y = 0.7
	head_control.run(point)
	
	rospy.sleep(1.0)

	point.y = 0.0
	point.z = 0.0
	head_control.run(point)	

	rospy.sleep(1.0)
	
	point.z = 1.5
	head_control.run(point)	

	rospy.sleep(1.0)

	point.z = 1.0
	head_control.run(point)

if __name__ == "__main__":
    rospy.init_node("look_to_point")
    rospy.loginfo("look_to_point server started")
    
    head_control_server = LookToPointServer()
    head_control_server.run()	

    while not rospy.is_shutdown():
        rospy.sleep(1)
