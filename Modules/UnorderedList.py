#UnorderedList.py
from Node import*
class UnorderedList:

	def __init__(self):
		self._head = None
		self._tail = None
		
	def __str__(self):
		output = '['
		ptr = self._head
		while ptr != None:
			output += str(ptr.getData())+' '
			ptr = ptr.getNext()
		return output + ']'
		
	def get(self,index):
		if index < 0 or index >= self._length:
			print ('index of of range')
			return None
		cursor = self._head
		for i in range(index):
			cursor = cursor.getNext()
		return cursor.getData()
		
	def isEmpty(self):
		return self._head == None 
		
	def add(self, item):
		temp = Node(item)
		if self._head == None:
			self._head = temp
			self._tail = self._head
		elif self._head == self._tail:
			self._tail = temp
			self._head.setNext(self._tail)
		else:
			self._tail.setNext(temp)
			self._tail = temp
			
		
	def remove(self, item):
		current= self._head
		previous = None
		found = False
		while not found and current != None:
			if current.getData()==item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if current == None:
			return
		elif previous == None:
			self._head = current.getNext()
		else:
			previous.setNext(current.getNext())
		
	def search(self, item):
		current = self._head
		while current!=None:
			if current.getData()==item:
				return True
			else:
				current = current.getNext()
		return False
			
	def length(self):
		current = self._head
		count = 0
		while current != None:
			count+=1
			current = current.getNext()
		return count
		
	
		