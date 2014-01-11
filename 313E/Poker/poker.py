#  Files: Poker.py
#
# Description: generates and evaluates N poker hands
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
#########################################
from hand import*
	
def play(n):
	for i in range(1,n+1):
		#creates a new deck for every iteration
		a=deck()
		a.shuffle()
		print('\n')
		print('hand number', i)
		c=hand(a)
		print(c)
		c.processHand(S,R)
		print(c.evaluateHand())

		
def main():
#loop to test for integer input
	while True:
		try:
			n = input('how many hands would you like to deal?:\n')
			if n.isdigit():
				n=int(n)
				break
			raise
		except:
			print('that is not a valid input. Please enter and positive integer.')
	play(n)
		
main()