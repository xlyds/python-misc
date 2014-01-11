#  Files: Widget.py
#
#  Description: Defines the widget class
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 10/8/11
#
#  Date Last Modified: 10/10/11
#############################################
class Widget:
	'''Creates a widget with the properties:color, costumer name, quantity and postiional number'''
	def __init__(self, colors, name, quantity, orderNum):
		self._color = colors
		self._name = name
		self._quantity = quantity
		self._orderNum = orderNum
		
	def getColor(self):
		return self._color
	
	def getName(self):
		return self._name
		
	def getNumber(self):
		return self._quantity
	def getorderNum(self):
		return self._orderNum
		
	def __str__(self):
		if self._quantity==1:
			return '1 ' + self._color + ' widget for ' + self._name + ' (order number:' +str(self._orderNum)+')'
		else:
			return str(self._quantity)+' '+self._color+' widgets for '+self._name + ' (order number:' +str(self._orderNum)+')'
		
	