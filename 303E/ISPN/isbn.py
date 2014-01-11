#  File: ISBN.py

#  Description: Checks the validity of a list of ISPN #'s

#  Student Name: Zach Tidwell

#  Student UT EID: zt659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 8/4/11

#  Date Last Modified:8/4/11

########################################################################################
#ISBN.py

#test the reduced string to see if it is the correct length
def length(rstr):
	if len(rstr)==10:
		return True
	else:
		return False
		
#test the first 9 charaters in the string to see if they are digits		
def digits(rstr):
	while True:
		try:
			n = int(rstr[:-1])
			return True
		except:
			return False
			
#Test the ensure the rstr has the correc ending		
def endX(rstr):
	if (ord(rstr[-1])>=48 and ord(rstr[-1])<=57):
		return True
	elif rstr[-1]=='x' or rstr[-1]=='X':
		return True
	else:
		return False
		
#converts x's into 10's so that the last partial sum can be conputed.		
def changeEnd(rstr):
	if rstr.endswith('x') or rstr.endswith('X'):
		return 10
	elif ord(rstr[-1])>=48 and ord(rstr[-1])<=57:
		return int(rstr[-1])
		
# computes the first list of partial sums.
def sum1(rstr,last):
	s1=[]
	sum=0
	for char in rstr[:-1]:
		i=int(char)
		sum+=i
		s1.append(sum)
	s1.append(s1[-1]+last)
	return s1
	
#computes the second list of partial sums with the first.	
def sum2(s1):
	sum=0
	s2=[]
	for item in s1:
		sum+=item
		s2.append(sum)
	return s2
	
def main():
	infile = open('ispn.txt','r')
	outfile = open('isbnOut.txt','w')
	for line in infile:
		#we'll make a reduced string, rstr. We'll strip then slipt at the hyphens
		rstr=''
		for i in (line.rstrip()).split('-'):
			rstr+=i
		#if the necessary conditions are met, s1 and s2 are computed.
		if length(rstr) and digits(rstr) and endX(rstr):
			last = changeEnd(rstr)
			s1 = sum1(rstr,last)
			s2 = sum2(s1)
			#final condition of validity is verified
			if s2[-1]%11==0:
				outfile.write(line.rstrip()+'  valid \n')
			else:
				outfile.write(line.rstrip()+'  invalid \n')
		else:
			outfile.write(line.rstrip()+'  invalid \n')
	infile.close()
	outfile.close()
	print 'Tests complete! Open isbnOut.txt in the folder containing\nisbn.py to view the results!'
main()
		
		
		
	