#  File: Cipher.py

#  Description: Hail Caeser cipher!

#  Student Name: Zach Tidwell

#  Student UT EID: zt659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 7/30/11

#  Date Last Modified: 7/31/11

#########################################################################################################################
#cipher.py
#intermediatry strings. We'll use look up the indice values and use
#them to adjust the plaintext characters to ciphertext.
alphl = 'abcdefghijklmnopqrstuvwxyz'
alphu = alphl.upper()
nums = '0123456789'

def inf():
	#input file loop
	import os
	while True:
		try:
			pathin = raw_input('enter input file name \n(must be in current working directory):\n')
			#we need to see if it actually exists
			if os.path.exists(pathin):
				infile = open(pathin,'r')
				return infile
				break
		except:
			print 'Invalid name, please try again (ex. file.txt)'
	

def outf():
	#output file loop
	while True:
		try:
			outfile = open(raw_input('enter output file name\n(must be in current working directory):\n'),'w')
			return outfile
			break
		except (IOError, SyntaxError):
			print 'Invalid name, please try again (ex. file.txt)'
	

def shift():
	#parameter value loop
	while True:
		try:
			shift = int(input('please enter the postive integer shift parameter\nuse integers that are not multiples\nof 10 or 26 for best encryption:\n'))
			if shift>=1:
				return shift
				break
			raise
		except (ValueError, NameError, TypeError, SyntaxError):
			print 'Invaild shift parameter. please enter a postive integer!'
			
def encrypt():
	infile = inf()
	outfile = outf()
	n = shift()
	for line in infile:
		for char in line:
		#We'll find the ACSII value for char. This will telll us what kind of charater it is. 
		#We'll find the it's index value in on of the lists define at the beginning and add the
		#shift parameter then divide by the number of characters in the appropriate string. The 
		#result of this computation will be the ASCII value for the cipher charater.
			if (ord(char)>=48 and ord(char)<=57):
				#compute the cipher character.
				ciphChar = chr(48+(((nums.find(char))+n)%10))
				outfile.write(ciphChar)
			elif (ord(char)>=65 and ord(char)<=90):
				ciphChar = chr(65+(((alphu.find(char))+n)%26))
				outfile.write(ciphChar)
			elif (ord(char)>=97 and ord(char)<=122):
				ciphChar = chr(97+(((alphl.find(char))+n)%26))
				outfile.write(ciphChar)
			else:
				outfile.write(char)
				
	print 'Sucess! your ciphertext file has been created!'
	outfile.close()
	infile.close()
	

def decrypt():
	infile = inf()
	outfile = outf()
	n = shift()
	for line in infile:
		for char in line:
			#same as encrypt(), but now we subtract the shift parameter.
			if (ord(char)>=48 and ord(char)<=57):
				ciphChar = chr(48+(((nums.find(char))-n)%10))
				outfile.write(ciphChar)
			elif (ord(char)>=65 and ord(char)<=90):
				ciphChar = chr(65+(((alphu.find(char))-n)%26))
				outfile.write(ciphChar)
			elif (ord(char)>=97 and ord(char)<=122):
				ciphChar = chr(97+(((alphl.find(char))-n)%26))
				outfile.write(ciphChar)
			else:
				outfile.write(char)
	print 'Sucess! your plaintext file has been created!'
	outfile.close()
	infile.close()
	
#Bringing it all together.
def main():
	import os
	#tells the user where they are.
	cwd = os.getcwd()
	print 'current working directory:', cwd
	while True:
		try:
			mode = raw_input('Would you like to decrypt or encrypt(E/D):\n')
			if (mode == 'E'):
				print 'Encryption mode active'
				encrypt()
				break
			elif (mode == 'D'):
				print 'Decryption mode active'
				decrypt()
				break
			else:
				raise
		except:
			print 'Error: Bad input. Goodbye!'
			quit()
			
main()
		