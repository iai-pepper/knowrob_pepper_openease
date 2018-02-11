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
    # the description of what pepper is pointing at:
    description = req.description
    # the TF transformer
    pointPS = listener.transformPose("/torso", req.point)
    point = [float(pointPS.pose.position.x), float(pointPS.pose.position.y), float(pointPS.pose.position.z)]
    # so that pepper will say something before pointing at it.
    tts.say("There.")
    # now let's point somewhere!
    #pointAt(const std::string& Effector, const std::vector<float>& Position, const int& Frame, const float& FractionMaxSpeed)
    trackerService.pointAt(ARM, point, FRAME, MAX_SPEED)
    pointPS = listener.transformPose("/torso", req.point)
    point = [float(pointPS.pose.position.x), float(pointPS.pose.position.y), float(pointPS.pose.position.z)]
    trackerService.lookAt(point, FRAME, MAX_SPEED, True)

    if description and description.strip():
        tts.say(description)

    return PepperPointAtResponse(PepperPointAtResponse.COMPLETED)

# This method gets the String from our SRV File and uses the Text to Speech from Pepper
# to say the text given in the request. Until now we will only return Complete.
def pepper_say(req):
    tts.say(req.str)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default= os.environ['NAO_IP'],
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    # this will give us some light if something breaks while starting the service.
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port)
               + ".\n" + "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    global tts
    global trackerService
    # Get the service ALTracker.
    trackerService = session.service("ALTracker")
    # Get the text to speech.
    tts = session.service("ALTextToSpeech")
    pepper_oe_server()