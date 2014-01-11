#  Files: stack.py
#
# Description: stack ADT
#
# Student's Name: Zach Tidwell
#
# Student's UT EID: zt659
#
# Course Name: CS 313E 
#
# Date Created: 09 / 25 / 11
#
# Date Last Modified: 09 / 30 / 11
#################################################

class Stack:
	'''Define a Stack ADT with operations: Stack, isEmpty,
      push, pop, peek, and size.'''
	
	def __init__(self):
		self._items=[]
		
	def isEmpty(self):
		return self._items==[]
		
	def push(self,item):
		self._items.append(item)
	
	def pop(self):
		if self.isEmpty():
			return "stack is empty"
		return self._items.pop()
		
	def peek(self):
		return self._items[len(self._items)-1]
		
	def len(self):
		return len(self._items)
	
	def __str__(self):
		result = '['
		for i in self._items:
			result+=' '+i.__str__()
		return result+' ]'
			
			
	