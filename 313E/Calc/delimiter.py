#delimiter.py
'''process a string and returns true if delimiters match up. valid delimiters: ([{}])'''
from stack import*
def matches(top,char):
	if top=='(':
		return char==')'
	elif top=='[':
		return char==']'
	elif top=='{':
		return char=='}'
		
def delimiter(str, stack):
	for char in str:
		if (char=='(' or char=='{' or char=='['):
			stack.push(char)
		elif (char==')' or char=='}' or char==']'):
			if stack.isEmpty():
				return False
			else:
				top=stack.pop()
				if not matches(top, char):
					return False
		else:
			pass
	return stack.isEmpty()
def main():
	str = input('enter input:\n')
	stack=Stack()
	print(delimiter(str,stack))

main()