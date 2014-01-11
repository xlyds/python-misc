#  Files: Node.py
#
#  Description: Node class
#
#  Students' Name: Zach Tidwell
#
#  Students' UT EID: zt659	
#
#  Course Name: CS 313E 
#
#  Date Created: 10/23/11
#
#  Date Last Modified:10/24/11
class Node:
	
	def __init__(self,iDat):	
		self._data = iDat
		self._next = None
	
	def getData(self):
		return self._data
		
	def getNext(self):
		return self._next
		
	def setData(self,newData):
		self_.data = newData
		
	def setNext(self, nextNode):
		self._next = nextNode

		
	