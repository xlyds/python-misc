#  File: Assignment8.py
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
########################################\

from stack import*
from Trees import*



def isOperator(token):
	ops = '+-*'
	return ops.find(token)!=-1
	
def postfixToTree(postfix):
	stack = Stack()
	tokens = postfix.split()
	#print (tokens)
	for token in tokens:
		if token.isdigit() or (token[0]=='-' and token[1:].isdigit()):
			node = BinaryTreeNode(token)
			stack.push(node)
		elif isOperator(token):
			if stack.len()<2:
				return('Ill formed expression')
			else:
				rChild = stack.pop()
				lChild = stack.pop()
				node = BinaryTreeNode(token, rChild, lChild)
				stack.push(node)
		else:
			return('operation " '+token+' " not supported')	
	if stack.len()>1:
		return('Ill formed input')
	else:
		return BinaryTree(stack.pop())
		
def applyOp (op, arg1, arg2):
    if op == "+":
        return arg2 + arg1
    elif op == "*":
        return arg2 * arg1
    elif op == "-":
        return arg2 - arg1
    else:
        print ("Operator " + op + " not recognized")
	
def compile(postfix):
	tokens = postfix.split()
	instructions = []
	for token in tokens:
		if token.isdigit() or (token[0]=='-' and token[1:].isdigit()):
			instructions.append('PUSH '+str(token))
		elif token == '+':
			instructions.append('ADD')
		elif token == '-':
			instructions.append('SUB')
		elif token == '*':
			instructions.append('MULT')
	return instructions
	
def interperateAux(command, evalStack):
	arg2 = int(evalStack.pop())
	arg1 = int(evalStack.pop())
	if command=='ADD':
		sum = arg1 + arg2
		evalStack.push(str(sum))
	elif command=='SUB':
		diff = arg1 - arg2
		evalStack.push(str(diff))
	elif command=='MULT':
		prod = arg1 * arg2
		evalStack.push(str(prod))
		
def interperate(commands):
	evalStack = Stack()
	for command in commands:
		command = command.split()
		if command[0] == 'PUSH':
			evalStack.push(command[1])
		else:
			interperateAux(command[0], evalStack)
	print (evalStack.pop())
			
def evalAux(node):
	if node.isLeafNode():
		return int(node.getValue())
	else:
		leftArg = evalAux(node.getLeft())
		rightArg = evalAux(node.getRight())
		return applyOp(node.getValue(), leftArg, rightArg)
		
def evaluate(tree):
	if tree.isEmpty():
		print('Tree is empty!')
		return None
	else:
		return evalAux(tree.getRoot())		

def interface():
	while True:
		try:
			postfix = input('enter a postfix expression: \n >>> ')
			if postfix == 'exit':
				quit()
			tree = postfixToTree(postfix)
			if isinstance(tree,str):
				print(tree)
				raise
			else:
				print('  You entered : ',end=' '), tree.inorder()
			print('  This expression has value : ',evaluate(tree), '\n')
			instr = compile(postfix)
			print('  This leaves the following instructions:')
			for command in instr:
				print('    ',command)
			print('  Which leaves the following value on the stack:',end=' ')
			interperate(instr)
			print('\n')
		except (RuntimeError):
			print('\n')
		
def main():
	print('\n')
	print('Enter a legal postfix expression with integers and \noperators (+, +, -).  Use blanks to separate tokens:\n')
	interface()
	
main()
	