#finalpractice.py
from stack import*


######################################################

"checks to test that delimiters in a string match up"

def match(a,b):
	front = '[{(<'
	end = ']})>'
	return front.find(a)==end.find(b)
	
def checkdelimiter(str):
	front = '[{(<'
	end = ']})>'
	stack = Stack()
	for char in str:
		if front.find(char)!=-1:
			stack.push(char)
		elif end.find(char)!=-1:
			if stack.isEmpty():
				return False
			else:
				a=stack.pop()
				match(a,char)
				if not match(a,char):
					return False
		pass
	return stack.isEmpty()
"""str = '[a+(b-{c/d}-e)+f]/3'			
print(checkdelimiter(str))"""			

####################################################

def isInt(str):
	str = str.strip()
	ls = str.split()
	if len(ls)>1:
		return False
	for i in ls:
		return (i[0]=='-' and i[1:].isdigit()) or i.isdigit()
		
str = '3-2'
#print(isInt(str))

#####################################################
#                   From the quiz                   #
##################################################### 
from Trees import*
import random

n4=BinaryTreeNode(random.randint(0,10))
n5=BinaryTreeNode(random.randint(0,10))
n6=BinaryTreeNode(random.randint(0,10))
n3=BinaryTreeNode(random.randint(0,10),n4,n5)
n2=BinaryTreeNode(random.randint(0,10),n6)
n1=BinaryTreeNode(random.randint(0,10),n2,n3)
tree=BinaryTree(n1)
	
def countNodesAux(node):
	if node==None:
		return 0
	else:
		return 1+countNodesAux(node.getRight())+countNodesAux(node.getLeft())
	
def countNodes(tree):
	if tree.isEmpty():
		return 0
	else:
		return countNodesAux(tree.getRoot())
		
#print(countNodes(tree))

###################################################
#               Simple Class: Kangaroo            #
###################################################

class Kangaroo:
	def __init__(self,content=None):
		if content==None:
			content=[]
		self.pouch_contents = [content]
		
	def put_in_pouch(self,item):
		self.pouch_contents.append(item)
		
	def __str__(self):
		t = '[ '
		for i in self.pouch_contents:
			t+=i.__str__()+' '
		return t +']'
		
######################################################
#                   Market Simulation                #
######################################################
from Myqueue import*
class Customer:
	def __init__(self,num):
		self._customerNum = num
		self._itemCount = random.randint(0,10)
		
	def getCustomerNumber(self):
		return self._customerNum
		
	def getItemCount(self):
		return self._itemCount
		
	def decrementItems(self):
		self._itemCount-=1
		
	def __str__(self):
		return 'Customer '+(self.getCustomerNumber()).__str__()+' has '+(self.getItemCount()).__str__()+' items.' 
		
class Market:
	def __init__(self):
		self._line1=Myqueue()
		self._line2=Myqueue()
		
	def addToLine(self,c,q):
		"""c is an istance of the Customer class and q is the line number"""
		if q==1:
			self._line1.enqueue(c)
		else:
			self._line2.enqueue(c) 
			
	def chooseLine(self):
		"""chooses the shortest line, but will choose randomly if they are of equal length"""
		if len(self._line1)<len(self._line2):
			return 1
		elif len(self._line1)>len(self._line2):
			return 2
		else:
			return random.choice([1,2])
			
	def shouldIAddCustomer(self,k):
		"""the parameter K gives the percent chance of adding a customer during the given clock cycle"""
		return random.randint(0,9)<k
		
	def printMarketState(self):
		print('line 1: ' + self._line1.__str__())
		print('line 2: ' + self._line2.__str__())
		
	def simulate(self,steps,k):
		custNumber = 4
		for i in range(steps):
			print('step number'+i.__str__()+'\n')
			if not self._line1.isEmpty():
				if self._line1.peek().getItemCount()<=1:
					self._line1.dequeue()
				else:	
					self._line1.peek().decrementItems()
			if not self._line2.isEmpty():
				if self._line2.peek().getItemCount()<=1:
					self._line2.dequeue()
				else:	
					self._line2.peek().decrementItems()
			#should i add a new customer?
			if self.shouldIAddCustomer(k):
				NewCustomer=Customer(custNumber)
				custNumber+=1
				lineChoice=self.chooseLine()
				self.addToLine(NewCustomer,lineChoice)
			self.printMarketState()
			
#######################################################################
#               An Examaple of mutual recursion                       #
#######################################################################
			
n=100			
def isEven(n):
	if n==0:
		return True
	else:
		return isOdd(n-1)
def isOdd(n):
	if n==0:
		return False
	else:
		return isEven(n-1)
		
print(isEven(n))
print(isOdd(n))