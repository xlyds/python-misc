#  Files: Deck.py
#
# Description: deck class
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
##################################################
import random
from card import*

class deck:+

	'''creates a deck of cards'''
	def __init__(self):
		self._cards = []
		for suit in card.suit:
			for rank in card.rank:
				c = card(rank,suit)
				self._cards.append(c)
	
	def shuffle(self):
		random.shuffle(self._cards)
		
	def deal(self):
		if len(self)==0:
			return None
		else:
			return self._cards.pop(0)
	def __len__(self):
		return len(self._cards)
		
	def __str__(self):
		result = ''
		for c in self._cards:
			result+=str(c) + '\n'
		return result
		
