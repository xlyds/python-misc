#  Files: Assignment5.py
#
#  Description: Preforms radix sort on an array of random ints
#
#  Students' Name:Zach Tidwell
#
#  Students' UT EID:zt659	
#
#  Course Name: CS 313E 
#
#  Date Created:10/24/11
#
#  Date Last Modified:10/25/11


#################################################

from LinkedList import*
import random

def getEmptyBins():
	return [LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList()]

def printBins(binList):
	#use to debug radix algorithm.
	for j in range(10):
		print( str(j) + ' : '),print(binList[j])
			
def PrintList(input, linecount):
	print('[',end=''),
	counter=0
	for i in input:
		print('%3i'%i,end=' '),
		counter+=1
		if counter==linecount:
			print('\n',end=' ')
			counter = 0
	print(']')
	
def computeBin(num,r):
	if r==0:
		return num%10
	else:
		if num < (10**r):
			return 0
		else:
			shiftnum = num//(10**r)
			return shiftnum%10
	
def radixsort(input,k=3):
	for i in range(k):
		binList = getEmptyBins()
		for num in input:
			BinNum = computeBin(num,i)
			binList[BinNum].add(num)
		#printBins(binList)
		input = []
		for list in binList:
			for h in range(list.length()):
				input.append(list.get(h))
	return input
	
def main():
	input = [ random.randint(0,999) for i in range(200)]
	print('The Unsorted list is:')
	PrintList(input,20)
	print('The Sorted list is:')
	sort = radixsort(input,k=3)
	PrintList(sort,20)
	
main()