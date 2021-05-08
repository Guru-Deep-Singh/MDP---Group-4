#!/usr/bin/env python

from hold_basket import Holdbasket
from pick import Pick
from place import Place
import rospy
from move_base_server import MoveBaseServer
from  look_to_point_server import LookToPointServer
from gripper_control import GripperControl
import geometry_msgs.msg

if __name__ == "__main__":
    rospy.init_node("demo")
    hb = Holdbasket()
    pick = Pick()
    place = Place()
    move = MoveBaseServer()
    head = LookToPointServer()
    gripper_left = GripperControl("left")
    gripper_right = GripperControl("right")
    
    hb.run()
    rospy.sleep(1.0)
    gripper_left.run("close")
    rospy.sleep(1.0)
    goal_pose = geometry_msgs.msg.Pose()
    goal_pose.position.x = 0.75
    goal_pose.position.y = 0.0
    goal_pose.position.z = 0.0
    goal_pose.orientation.x = 0.0
    goal_pose.orientation.y = 0.0
    goal_pose.orientation.z = 0.0
    goal_pose.orientation.w = 1.0
    move.run(goal_pose)
    rospy.sleep(1.0)
    head.run()
    rospy.sleep(1.0)
    pick.run()
    rospy.sleep(1.0)
    gripper_right.run("close")
    rospy.sleep(1.0)
    place.run()
    rospy.sleep(1.0)
    gripper_right.run("open")
    rospy.sleep(1.0)





