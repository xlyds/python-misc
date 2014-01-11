#  File: Trees.py
#
#  Description: Related tree classes
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 11/28/11
#
#  Date Last Modified: 11/30/11
########################################
from stack import*
class BinaryTreeNode:
	''' Three fields: an arbitraty value, a left pointer and a right pointer. Both pointers point to other BinaryTreeNode Classes'''
	def __init__(self, value, right = None, left = None):
		self._value = value
		self._right = right
		self._left = left
		
	def getValue(self):
		return self._value
		
	def getRight(self):
		return self._right
		
	def getLeft(self):
		return self._left
		
	def setValue(self, value):
		self._value = value
		
	def setRight(self, right):
		self._right = right
		
	def setLeft(self, left):
		self._left = left
		
	def isLeafNode(self):
		return (self._right==None and self._left==None)
		
class BinaryTree:
	''' the Binary tree class is simply a pointer to a BinaryTreeNode class'''
	def __init__(self,root=None):
		self._root = root
		
	def isEmpty(self):
		return self._root == None
		
	def getRoot(self):
		return self._root
		
	def inorderAux(node):
		if node == None:
			return
		else:
			if node.getLeft()!=None:
				print('(',end=' ')
			BinaryTree.inorderAux(node.getLeft())
			print(node.getValue(), end=' ')
			BinaryTree.inorderAux(node.getRight())
			if node.getRight()!=None:
				print(')',end=' ')
		
	def inorder(self):
		if self.isEmpty():
			return 'Tree is empty!'
		else:
			BinaryTree.inorderAux(self._root)
		print('\n')
	