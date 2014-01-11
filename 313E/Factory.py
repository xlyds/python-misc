#  Files: WidgetWorks.py
#
#  Description: Places and processes widget orders
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 10/8/11
#
#  Date Last Modified: 10/10/11

###################################################

from Queue import*
from Widget import*

shoppingCart = Myqueue()
oNum=0	   #will be used to determine the order number property of each widget created.
def placeOrder(c,n,q,oNum):
	Order = Widget(c,n,q,oNum)
	shoppingCart.enqueue(Order)
	print('Order confirmed! Please shop with us again!\n')
def processOrder(shoppingCart):
	print('\nprocessing orders now')
	while len(shoppingCart)>0:
		i = shoppingCart.dequeue()
		print('  Order shipped:    Order Number ',i.getorderNum(),': Customer ', i.getName(), ' requests ', i.getNumber(), i.getColor(), ' widgets.')
	else:
		print('Queue is empty')
def main(oNum):
	print('Welcome to the Waskelly Wabbit Widget Works automated ordering system!\n')
	while True:
		try:
			n = input("  Please enter the customer's name: ")
			if n == 'exit':
				processOrder(shoppingCart)
				quit()
			elif n.isdigit():
				raise
			break
		except RuntimeError:
			print('that does not appear to be a valid name. Order cancelled')
			main(oNum)
	while True:
		try:
			c = input("  Please select deisred widget color (red, white, blue): ")
			if c!='blue' and c!='red' and c!='white':
				raise
			break
		except RuntimeError:
			print(' We do not offer this color. Order cancelled\n')		
			main(oNum)
	while True:
		try:
			q = input("  Please select the number of " + str(c)+ " Widgets you would like: ")
			if int(q)<=0:
				raise
			oNum+=1
			break
		except (RuntimeError, ValueError):
			print(' Bad quantity. Order cancelled')
			main(oNum)
	placeOrder(c,n,q,oNum)
	main(oNum)
main(oNum)