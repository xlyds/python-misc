#  Files: Card.py
#
# Description: card class
#
# Student's Name:Zach Tidwell
#
# Student's UT EID: zt659
#
# Course Name: CS 313E 
#
# Date Created: 09/20/11	
#
# Date Last Modified:09/22/11
#######################################################
class card:
	'''creates a card with rank a and suit b'''
	
	#class attributes
	rank = (1,2,3,4,5,6,7,8,9,10,11,12,13)
	suit = ('Clubs','Hearts','Spades','Diamonds')
	
	def __init__(self,rank,suit):
		self._rank=rank
		self._suit=suit
		
	def getrank(self):
		return self._rank
		
	def getsuit(self):
		return self._suit
		
	def __str__(self):
		r = self._rank
		if r == 1:
			myrank = 'Ace'
		elif r == 11:
			myrank = 'Jack'
		elif r == 12:
			myrank = 'Queen'
		elif r== 13:
			myrank = 'King'
		else:
			myrank = str(r)
		return myrank + ' of ' + self._suit
			