#turtleSquare.py

from turtle import*

def drawSquare(turtle, x, y, l):
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	for i in range(4):
		turtle.lt(90)
		turtle.forward(l)
		
turtle=Turtle()
x=100
y=-50
l=100
drawSquare(turtle, x, y, l)