#!/usr/bin/env python

# ROS imports
import rospy
import actionlib
from rospy import client

# ROS messages imports
from gripper_control import GripperControl
import geometry_msgs.msg
from geometry_msgs.msg import PointStamped

        
class GripperControlServer():

    def __init__(self):
        """Node to manipulate gripper"""

        # Launch Client and wait for server
        #self._action_name = "look_to_point_server"
        #self._as = actionlib.SimpleActionServer(self._action_name, PointHeadAction, execute_cb=self.execute_cb, auto_start = False)
        #self._as.start()


    def run(self, arm_side, action): #earlier was (self,point)
	gripper_right = GripperControl(arm_side)
	gripper_right.run(action)
	rospy.sleep(4)
	rospy.loginfo("Closed gripper")

if __name__ == "__main__":
    rospy.init_node("gripper_control")
    rospy.loginfo("gripper_control server started")
    
    gripper_control_server = GripperControlServer()
    gripper_control_server.run('left', 'close')
    gripper_control_server.run('right', 'close')	

    while not rospy.is_shutdown():
        rospy.sleep(1)
