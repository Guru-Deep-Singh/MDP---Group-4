#!/usr/bin/env python

import actionlib
import rospy
import geometry_msgs.msg
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class MoveBaseServer(object):
    def __init__(self):
        # Launch Client and wait for server
        self.client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        rospy.loginfo('Waiting for server...')
        self.client.wait_for_server()
        
        #self._clear_octomap_srv = rospy.ServiceProxy(
        #    '/clear_octomap', Empty)
        #self._clear_octomap_srv.wait_for_service()

    def run(self, goal_pose):
    
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose = goal_pose

        rospy.loginfo('Sending move base goal...')
        self.client.send_goal(goal)
        self.client.wait_for_result()

        #self._clear_octomap_srv()
        rospy.loginfo('Navigation finished')
        

if __name__ == "__main__":
    rospy.init_node("move_base_server")
    rospy.loginfo("move_base_server started")

    move_base = MoveBaseServer()
    goal_pose = geometry_msgs.msg.Pose()
    goal_pose.position.x = 1.0
    goal_pose.position.y = 0.0
    goal_pose.position.z = 0.0
    goal_pose.orientation.x = 0.0
    goal_pose.orientation.y = 0.0
    goal_pose.orientation.z = 0.0
    goal_pose.orientation.w = 1.0
    move_base.run(goal_pose)

    while not rospy.is_shutdown():
        rospy.sleep(1)
