#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
"""
This module is for the Point at function from Pepper inside a ROS Environment.
It uses code from https://github.com/suturo16/ros_pepper
"""


from knowrob_pepper_openease_msgs.srv import *
from geometry_msgs.msg import PoseStamped
import tf
import rospy
import qi
import argparse
import sys
import os
from thread import start_new_thread

# This is just a variable which says which arm pepper will use.
ARM = "RArm" # can be RArm, LArm or Arms
# The frame, can be 0=torso, 1=world or 2=robot.
FRAME = 0
# Fraction max speed, no idea what it is or what it does
MAX_SPEED = 0.8
# The pepper services
trackerService = None
tts = None
listener = None

# This method gets the String from our SRV File and uses the Text to Speech from Pepper
# to say the text given in the request. Until now we will only return Complete.
# We are using TF to transform the point we get to Torso frame from Pepper.
def pepper_point_at(req):
    rospy.loginfo('Received point at request')
    return PepperPointAtResponse(PepperPointAtResponse.COMPLETED)

# This method gets the String from our SRV File and uses the Text to Speech from Pepper
# to say the text given in the request. Until now we will only return Complete.
def pepper_say(req):
    rospy.loginfo('Received say request')
    return PepperSayResponse(PepperSayResponse.COMPLETED)


# The server announces the service to our ROSCORE and stays open until the Core is closed or the Node is manually
# terminated.
def pepper_oe_server():
    rospy.init_node('pepper_oe_server')
    # initializing our transformer!
    global listener
    listener = tf.TransformListener()
    s = rospy.Service('pepper_point_at', PepperPointAt, pepper_point_at)
    s = rospy.Service('pepper_say', PepperSay, pepper_say)
    rospy.spin()


# We are using the NAO API from Aldebaran, we start the session with the given IP address. And save the TTS as
# a global variable in this script. That is the best way of getting it inside the Say Method.
if __name__ == "__main__":
    pepper_oe_server()