#!/usr/bin/python
# -*- coding: utf-8 -*- 
from numpy import *
from pylab import *
import random
intro = """
==============================================================================================================================
### NUMERIC QUIZ v. 1.2 -- Try to guess the number the computer chooses! ###
 
Code written in Python 2.7.3 for Python(x,y) using "Notepad++ v6.3" on a "Windows 7 SP1 x64 Home Premium" environment
(C)2013 EMANUELE BALLARIN & GAMMADECAY DEVELOPEMENT - All rights reserved (email: ehteqx@gmail.com)
 
==============================================================================================================================
"""
print(intro)
print(" ")
print("Get ready!!")
while True:
	try:
		lowlim = int(raw_input("Choose the lower limit of the range in which the chosen number have to be included... "))
		break
	except ValueError:
		print("I'm sorry! The input you gave me isn't an integer. Please, insert a correct integer... ")
while True:
	try:
		upplim = int(raw_input("Choose the upper limit of the range in which the chosen number have to be included... "))
		break
	except ValueError:
		print("I'm sorry! The input you gave me isn't an integer. Please, insert a correct integer... ")
times = 0
casualnum = random.randint(lowlim,upplim)
print "Now I'll choose a number between", lowlim, "and", upplim, "..."
print("And now, try to guess it!")
while True:
	try:
		usernum = int(raw_input("The number I have chosen is... "))
		break
	except ValueError:
		print("I'm sorry! The input you gave me isn't an integer. Please, insert a correct integer... ")
while usernum != casualnum:
	if usernum < casualnum:
		print("I'm sorry! That wasn't the number I have chosen. Try again with a higher number")
		times = times+1
		while True:
			try:
				usernum = int(raw_input("The number I have chosen is... "))
				break
			except ValueError:
				print("I'm sorry! The input you gave me isn't an integer. Please, insert a correct integer... ")
	else:
		print("I'm sorry! That wasn't the number I have chosen. Try again with a lower number")
		times = times+1
		while True:
			try:
				usernum = int(raw_input("The number I have chosen is... "))
				break
			except ValueError:
				print("I'm sorry! The input you gave me isn't an integer. Please, insert a correct integer... ")
if times == 0:
	print "Very good! You guessed the number in only", times+1, "try!!"
else:
	print "Good! You guessed the number in", times+1, "tries!!"
print("Bye bye!!")
