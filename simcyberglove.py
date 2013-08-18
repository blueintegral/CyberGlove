#!/usr/bin/env python

import select
import serial
import os
import time
#import signal
import sys
import tty
import termios

os.system("clear")

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
'''
def signal_handler(signal, frame):
    print '\nExiting...'
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
'''

def print_stuff():
	os.system("clear")
	print bcolors.OKBLUE+"""
	   ______      __              ________              
	  / ____/_  __/ /_  ___  _____/ ____/ /___ _   _____ 
	 / /   / / / / __ \/ _ \/ ___/ / __/ / __ \ | / / _ \\
	/ /___/ /_/ / /_/ /  __/ /  / /_/ / / /_/ / |/ /  __/
	\____/\__, /_.___/\___/_/   \____/_/\____/|___/\___/ 
	     /____/                                          
	  _____ _                 __      __           __
	  / ___/(_)___ ___  __  __/ /___ _/ /____  ____/ /
	  \__ \/ / __ `__ \/ / / / / __ `/ __/ _ \/ __  / 
	 ___/ / / / / / / / /_/ / / /_/ / /_/  __/ /_/ /  
	/____/_/_/ /_/ /_/\__,_/_/\__,_/\__/\___/\__,_/   
							  
	    ______    ___ __  _             __
	   / ____/___/ (_) /_(_)___  ____  / /
	  / __/ / __  / / __/ / __ \/ __ \/ / 
	 / /___/ /_/ / / /_/ / /_/ / / / /_/  
	/_____/\__,_/_/\__/_/\____/_/ /_(_)   

	""" + bcolors.ENDC
	print bcolors.WARNING + "For when you don't have $30,000 gloves but still want to make Atlas's hands move!" + bcolors.ENDC
	print ""
	print ""
	print ""

right_command_close = "rosservice call /sandia_hands/r_hand/simple_grasp ' { grasp: { name: \"cylindrical\", closed_amount: 1} }'"

right_command_open = "rosservice call /sandia_hands/r_hand/simple_grasp ' { grasp: { name: \"cylindrical\", closed_amount: 0} }'"

left_command_close = "rosservice call /sandia_hands/l_hand/simple_grasp ' { grasp: { name: \"cylindrical\", closed_amount: 1} }'"

left_command_open = "rosservice call /sandia_hands/l_hand/simple_grasp ' { grasp: { name: \"cylindrical\", closed_amount: 0} }'"

right_status = 0
left_status = 0

while(1):
	os.system("clear")
	print_stuff()
	if right_status:
		print "Right hand is closed. Press \'p\' to open it."
	else:
		print "Right hand is open. Press \'p\' to close it."
	if left_status:
		print "Left hand is closed. Press \'q\' to open it."
	else:
		print "Left hand is open. Press \'q\' to close it."

	key = raw_input(" ")
	if key == "p":
		if right_status:
			os.system(right_command_open)
			right_status = 0
		else:
			os.system(right_command_close)
			right_status = 1
	if key == "q":
		if left_status:
			os.system(left_command_open)
			left_status = 0
		else:
			os.system(left_command_close)
			left_status = 1











		
