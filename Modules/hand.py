#  Files: Hand.py
#
# Description: hand class
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
from deck import*

S = {}
R = {}
class hand:
	'''creates a hand of five cards'''
	def __init__(self, deck):
		'''creates the hand; takes argument: deck'''
		self._hand = []
		if len(deck)<5:
			deck=deck()
		else:
			for card in range(5):
				c = deck.deal()
				self._hand.append(c)

	def __str__(self):
		result = ''
		for card in self._hand:
			result+=str(card)+'\n'
		return result

	def processHand(self,S,R):
		for i in card.suit:
			S[i]=0
		for j in card.rank:
			R[j]=0
		for k in self._hand:
			S[k.getsuit()]+=1
			R[k.getrank()]+=1
			
	def hasPair(self,R):
		for key in R:
			if R[key]==2:
				return True
			pass
		return False
		
	def hasTwoPair(self,R):
		a=0
		for key in R:
			if R[key]==2:
				a+=1
		return a==2
		
	def hasThreeOfAKind(self,R):
		for key in R:
			if R[key]==3:
				return True
			pass
		return False
		
	def hasStraight(self,R):
		for i in range(1,9):
			if R[i]==1 and R[i+1]==1 and R[i+2]==1 and R[i+3]==1 and R[i+4]==1:
				return True
			pass
		return False
				
				
	def hasFlush(self,S):
		for key in S:
			if S[key]==5:
				return True
			pass
		return False
	
	def hasFullHouse(self,R):
		for i in range(1,13):
			if R[i]==2 or R[i]==3:
				result = R[i]
				for j in range(i+1,14):
					if R[j]==5-result:
						return True
					pass
			return False
				
	def hasFourOfAKind(self,R):
		for key in R:
			if R[key]==4:
				return True
			pass
		return False
			
	def hasStraightFlush(self,S,R):
		for key1 in S:
			if S[key1]==5:
				for i in range(1,9):
					if R[i]==1 and R[i+1]==1 and R[i+2]==1 and R[i+3]==1 and R[i+4]==1:
						return True
					pass
		return False
				
	def hasRoyalFlush(self,S,R):
		a = 0
		for key in S:
			if S[key]==5:
				for i in range(10,14):
					if R[i]==1:
						a+=1
						return (a==4 and R[1]==1)
						
	def evaluateHand(self):
		self.processHand(S,R)
		if self.hasRoyalFlush(S,R):
			return "Royal Flush"
		elif self.hasStraightFlush(S,R):
			return "Straight Flush"
		elif self.hasFourOfAKind(R):
			return "Four of a kind"
		elif self.hasFullHouse(R):
			return "Full House"
		elif self.hasFlush(S):
			return "Flush"
		elif self.hasStraight(R):
			return "Straight"
		elif self.hasThreeOfAKind(R):
			return "Three of a kind"
		elif self.hasTwoPair(R):
			return "Two pair"
		elif self.hasPair(R):
			return "Pair"
		else:
			return "Nothing"
