#planeGeometry.py
import math
from turtle import*
import time
class rectangle():
	def __init__(self,width,height,center):
		"""defines a rectangle in R X R, with center, an ordered pair"""
		self._height = height
		self._width = width
		self._center = center
		
	def getWidth(self):
		return self._side
		
	def getCenter(self):
		return self._center
		
	def getHeight(self):
		return self._height
		
	def getArea(self):
		return self._width*self._height
		
	def contains(self,point):
		supx = self._center[0]+(.5)*(self._width)
		infx = self._center[0]-(.5)*(self._width)
		supy = self._center[1]+(.5)*(self._height)
		infy = self._center[1]-(.5)*(self._height)
		return infx<=point[0]<=supx and infy<=point[1]<=supy
		
	def __str__(self):
		return 'rectangle with width '+str(self._width)+' and height '+str(self._height)+', centered at '+str(self._center) 
		
	def translate(self,dx,dy):
		"""translates to point=(x,y)"""
		new_center=(self._center[0]+dx,self._center[1]+dy)
		self._center = new_center
		return 'moved to point ('+str(new_center[0])+','+str(new_center[1])+')'
		
		
	def draw(self):
		x = self._center[0]
		y = self._center[1]
		t = Turtle()
		t.up()
		t.goto(x+((.5)*(self._width)),y+((.5)*(self._height)))
		t.down()
		t.setheading(90)
		for i in range(3):
			t.left(90)
			t.forward(self._width)
			t.left(90)
			t.forward(self._height)
		t.up()
		t.goto(x,y)
		
class square(rectangle):
	"""extension of rectangel class, special case: square"""
	def __init__(self,side,center):
		self._width = side
		self._height = side
		
	def __str__(self):
		return 'square of length '+str(self._width)+', centered at '+str(self._center)
		
def circle():
	"""circle in R X R, center is an ordered pair"""
	def __init__(self,radius,center):
		self._radius = radius
		self.center = center
		
	def Circumference(self):
		return 2*math.pi()*self._radius
		
	def Area(self):
		return math.pi()*(self._radius**2)
		
	def contains(self,point):
		"""point is an ordered pair"""
		x_0 = self._center[0]
		y_0 = self._center[1]
		x = point[0]
		y = point[1]
		metric = math.sqrt((x_0-x)**2+(y_0-y)**2)
		return metric<=self._radius
		
	def draw(self):
		x = self._center[0]
		y = self._center[1]
		t = Turtle()
		t.up()
		t.goto(x+radius,y)
		arc = (2*math.pi*self._radius)/360
		t.down()
		for i in range(360):
			t.forward(arc)
			t.left(1)
		t.up()
		t.goto(x,y)
			
		def __str__(self):
			return 'Circle with radius '+str(self._radius)+', centered at '+str(self._center)
		
	
		