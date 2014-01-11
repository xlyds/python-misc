#  Files: Assignment1a.py
#
#  Description: Draws a house
#
#  Student's Name: Zach Tidwell		
#
#  Student's UT EID: ZT659
#
#  Course Name: CS 313E 
#
#  Unique Number: 52295
#
#  Date Created: 09/14/11
#
#  Date Last Modified:09/14/11

###############################################
from turtle import *
import math
import time
def drawrect(turtle, x, y, length, width):

	turtle.up()
	turtle.goto(x, y)
	turtle.setheading(-90)
	turtle.down()
	for count in range(2):
		turtle.forward(length)
		turtle.right(90)
		turtle.forward(width)
		turtle.right(90)

def DrawEqTri(turtle, x, y, base, theta):
	turtle.up()
	turtle.goto(x,y)
	hypo = ((base/2)/(math.cos(theta)))
	turtle.setheading(180-math.degrees(theta))
	turtle.down()
	turtle.forward(hypo)
	turtle.left(2*math.degrees(theta))
	turtle.forward(hypo)
	
def DrawChimney(turtle, x, y, length, width):
	turtle.up()
	turtle.goto(x, y)
	turtle.setheading(90)
	turtle.down()
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(length-(width*math.tan(math.pi/6)))
ttl = Turtle()
ttl.pencolor('red')
drawrect(ttl, 275, 125, 400, 600)
ttl.pencolor('blue')
drawrect(ttl, 225, 0, 175, 125)
drawrect(ttl, 225, 0, 100, 125)
drawrect(ttl, 220, -5, 90, 115)
drawrect(ttl, 220, -100, 70, 115)
drawrect(ttl, -150, 0, 175, 125)
drawrect(ttl, -150, 0, 100, 125)
drawrect(ttl, -155, -5, 90, 115)
drawrect(ttl, -155, -100, 70, 115)
ttl.pencolor('brown')
drawrect(ttl, 50, 25, 300, 150)
drawrect(ttl, 45, 20, 295, 140)
drawrect(ttl, 20, -5, 130, 40)
drawrect(ttl, -30, -5, 130, 40)
drawrect(ttl, 20, -155, 100, 40)
drawrect(ttl, -30, -155, 100, 40)
ttl.pencolor('black')
DrawEqTri(ttl, 275, 125, 600, ((math.pi)/6))
DrawChimney(ttl, -225, 182.735, 175, 100)
ttl.hideturtle()
time.sleep(20)

