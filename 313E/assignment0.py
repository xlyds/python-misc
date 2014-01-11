#  File: Assignment0.py
#
# Description:
#
# Student's Name: Zach Tidwell
#
# Student's UT EID: zt659
#
# Course Name: CS 313E 
#
# Unique Number: 52295
#
# Date Created: sep 8
#
# Date Last Modified: sep 8

#########################################

#some preliminary stuff
alpha = 'abcdefghijklmnopqrstuvwxyz'
cipherstr = ''
dict = {}
#populate dictionary
for i in alpha:
	dict[i]=0
	
def display(instr,dict,cipherstr):
	print('in lowercase : ',instr.lower())
	print('in uppercase : ',instr.upper())
	print('the input conatins the following characters:')
	i2 = instr.lower()
	for char in i2:
		if char.isalpha():
			dict[char]+=1
	for key in dict:
		print('   ', key, ' : ', dict[key])
	for char in i2:
		if char.isalpha():
			cipherstr+=chr(97+((alpha.find(char)+1)%26))
		else:
			cipherstr+=char
	print (cipherstr)

def main():
	instr = input("user's input :")
	display(instr,dict,cipherstr)
	
main()