#  Files: MyQueue.py

#  Description: Defines the My Queue class
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
####################################################
class Myqueue:
	
	def __init__(self):
		self._items=[]
		
	def isEmpty(self):
		return self._items==0	
		
	def __str__(self):
		string=''
		if Myqueue.isEmpty(self):
			return 'Queue is empty!'	
		for item in self._items:
			string+=item.__str__()+' '
		return '[' + string + ']'
		
	def __len__(self):
		return self._items.__len__()
		
	def getPosition(self,item):
		position=(len(self._items)-self._items.index(item))
		return position
		
	def enqueue(self, item):
		self._items.insert(0,item)
		
	def dequeue(self):
		return self._items.pop()
		
	def peek(self):
		return self._items[len(self._items)-1]
	
	
	
		
	
		
		