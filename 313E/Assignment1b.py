#  Files: Assignment1a.py
#
#  Description: Draws a house
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Unique Number: 52295
#
#  Date Created: 9/14/11
#
#  Date Last Modified:9/14/11

###############################################
from turtle import *
import time

def Kochcurve(turtle, x):
# x means length
	if x<3:
		turtle.forward(x)
		return
	else:
		Kochcurve(turtle, x/3.0)
		turtle.left(60)
		Kochcurve(turtle, x/3.0)
		turtle.right(120)
		Kochcurve(turtle, x/3.0)
		turtle.left(60)
		Kochcurve(turtle, x/3.0)
#creates the outer flake
def Kochflake1(turtle,x):
	for i in range(3):
		Kochcurve(turtle,x)
		turtle.left(120)
#creates the center flake
def Kochflake2(turtle,x):
	for i in range(3):
		Kochcurve(turtle,x)
		turtle.right(120)
		
ttl = Turtle()
ttl.speed(0)
ttl.up()
ttl.goto(-150,125)	
ttl.down()
ttl.color('purple')
Kochflake2(ttl, 300)
ttl.up()
ttl.goto(-50,0)
ttl.down()
ttl.color('red')
Kochflake1(ttl,100)
ttl.hideturtle()
exitonclick()