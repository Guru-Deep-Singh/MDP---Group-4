#!/usr/bin/env python
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import JointState

class Pick(object):
    def __init__(self):
        self.client = actionlib.SimpleActionClient("/arm_right_controller/follow_joint_trajectory",FollowJointTrajectoryAction)
        self.client.wait_for_server()
        rospy.wait_for_message("joint_states",JointState)
        self.joint_names = ["arm_right_1_joint","arm_right_2_joint","arm_right_3_joint","arm_right_4_joint","arm_right_5_joint","arm_right_6_joint","arm_right_7_joint"]
        
        
    def run(self):
        trajectory = JointTrajectory()
        trajectory.joint_names = self.joint_names
        trajectory.points.append(JointTrajectoryPoint())
        index = 0
        trajectory.points[index].positions = [0.93,0.19,1.39,1.40,-1.83,0.73,-1.27]
        trajectory.points[index].velocities = [1.0 for i in self.joint_names]
        trajectory.points[index].time_from_start = rospy.Duration(2.0)

        rospy.loginfo("picking...")

        goal = FollowJointTrajectoryGoal()
        goal.trajectory = trajectory
        goal.goal_time_tolerance = rospy.Duration(0.0)

        self.client.send_goal(goal)
        rospy.loginfo(self.client.wait_for_result(rospy.Duration(3.0)))

        '''index = 1
        trajectory.points[index].positions = [-1.11,1.50,2.85,1.70,0.0,0.0,0.0]
        trajectory.points[index].velocities = [1.0 for i in self.joint_names]
        trajectory.points[index].time_from_start = rospy.Duration(2.0)

        rospy.loginfo("Holding basket")

        goal = FollowJointTrajectoryGoal()
        goal.trajectory = trajectory
        goal.goal_time_tolerance = rospy.Duration(0.0)

        self.client.send_goal(goal)
        rospy.loginfo(self.client.wait_for_result(rospy.Duration(3.0)))'''

'''if __name__ == "__main__":
    rospy.init_node("pick")
    pick = Pick()
    pick.run()

    rospy.loginfo("Successfully holded basket")'''
    