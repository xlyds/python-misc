#  File: Assignment6.py
#
#  Description: Binary Tree Class
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 11/28/11
#
#  Date Last Modified:
########################################

class BinaryTree:
	''' the Binary tree class is simply a pointer to a BinaryTreeNode class'''
	def __init__(self,root=None):
		self._root = root
		
	def isEmpty(self):
		return self._root == None
		
	def getRoot(self):
		return self._root
		
		
		