#  Files: Calculator.py
#
# Description: evaluates postfix and infix expressions
#
# Student's Name: Zach Tidwell
#
# Student's UT EID: zt659
#
# Course Name: CS 313E 
#
# Date Created: 09 / 30 / 11
#
# Date Last Modified: 09 / 30 / 11
########################################

from stack import*

stack=Stack()
limits='()'
Ops='+-*/'
prec = {}
prec['*']=3
prec['/']=3
prec['+']=2
prec['-']=2
prec['(']=1

def testinput(str):
	if str == '':
		return False
	for i in str.split():
		if (not i.isdigit()) and Ops.find(i)==-1 and limits.find(i)==-1:
			return False
	return True
		
def infixToPostfix(instr):
	oStr=''
	postList=[]
	opStack=Stack()
	tokenList = instr.split()
	for token in tokenList:
		if token.isdigit():
			postList.append(token)
		elif token=='(':
			opStack.push(token)
		elif token==')':
			Top = opStack.pop()
			while Top!='(':
				postList.append(Top)
				Top = opStack.pop()
		else:
			while not opStack.isEmpty() and prec[opStack.peek()]>=prec[token]:
				postList.append(opStack.pop())
			opStack.push(token)
	while not opStack.isEmpty():
		postList.append(opStack.pop())
	return postList
		
def operate(arg2,arg1,operator):
	return str(eval(arg1+operator+arg2))

def postEval(postList):
	for char in postList:
		if char.isdigit():
			stack.push(char)
		elif Ops.find(char)!=-1:
			if stack.len()<2:
				return 'Ill formed input!'
			else:
				arg2=stack.pop()
				arg1=stack.pop()
				result=operate(arg2,arg1,char)
				stack.push(result)
	return stack.pop()
	
def main():
	print ('This simple calculator has infix and postfix mode. enter in "postfix" \n into the prompt to trigger postfix mode. Enter "quit" to exit')
	
	while True:
		try:
			str = input('please enter an infix expression:\n')
			if str == 'postfix':
				str = input('please enter an postfix expression:\n')
				print (testinput(str))
				if testinput(str):
					x = str.split()
					print(str, ' = ', postEval(str))
				else:
					raise
			elif str == 'quit':
				quit()
			elif testinput(str):
				x = infixToPostfix(str)
				print(str , ' = ', postEval(x))
			else:
				raise RuntimeError
		except (RuntimeError):
			print('Ill formed input, try again or enter "quit" to exit.')	
main()
					
	