#  File: Books.py

#  Description: performs linguistic analysis on two different books

#  Student Name: Zach Tidwell

#  Student UT EID: ZT659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 8/9/11

#  Date Last Modified: 8/12/11


########################################################################

#Books.py

def create_word_dict():
	word_dict={}
	words = open('words.txt','r')
	for line in words:
		line=line.rstrip()
		word_dict[line]=1
	return word_dict
#populate the dictionary	
word_dict = create_word_dict()

#for comments on functions 1-5, see body of function getWordFreq(bookx)(line107)

#1
def histogram(bookx):
	hist={}
	for line in bookx:
		line = parse_string(line)
		for item in line.split(' '):
			if item not in hist:
				hist[item]=1
			else:
				hist[item]+=1
	#so we don't count empty strings
	del hist['']
	bookx.close()
	return hist
	
#2
def listUppercase(hist):
	ulist=[]
	for key in hist:
		if key[:1].isupper():
			ulist.append(key)
		else:
			pass
	return ulist
	
#3	
def remove_uppercase(hist,ulist):
	for item in ulist:
		if item in hist:
			del hist[item]
	return hist
	
#4	
def upper_in_hist(hist,ulist,word_dict):
	for item in ulist:
		if item.lower() not in hist:
			try:
				#checks existence in english word list
				if word_dict[item.lower()]==1:
					hist[item.lower()]=1
				else:
					pass
			except:
				pass
		else:
			hist[item.lower()]+=1
	return hist
	
#5
def cleansuffices(hist):
	if hist.has_key('o'):
		del hist['o']
	elif hist.has_key('ve'):
		del hist['ve']
	elif hist.has_key('re'):
		del hist['re']
	elif hist.has_key('s'):
		del hist['s']
	elif hist.has_key('t'):
		del hist['t']
	return hist
	
#give a nice, clean string that's easy to process
def parse_string(line):
	new_str = ''
	line = line.rstrip('\n')
	line = line.replace('-',' ')
	line = line.replace("'"," ")
	for char in line:
		if char.isalpha() or char.isspace():
			new_str+=char
	return new_str
	
def getWordFreq(bookx):
	#generates a crude word histogram
	hist = histogram(bookx)
	#creates a list of words begining with uppercase letters
	ulist = listUppercase(hist)
	#removes the items in the uppercase list from the histogram and returns hist
	hist = remove_uppercase(hist,ulist)
	#checks the existence of lowercase version of ulist items in hist. 
	#if they do exsist, frequency is counted. if they don't but are in the 
	#english word list, they are added to hist.
	hist = upper_in_hist(hist,ulist,word_dict)
	ofile=open('histogram-return.txt','w')
	hist = cleansuffices(hist)
	return hist
	
#computes unique words, total words and relative frequency of words	
def statistics(hist,author):
	print author,':\n'
	distinct = len(hist)
	print 'Total distinct words = ', distinct
	word_sum=0
	for key in hist:
		word_sum+=hist[key]
	print 'Total words (including duplicates) = ', word_sum
	ratio = float(distinct)/(float(word_sum))*100
	print 'relative frequency = ', ratio
	print '\n'
	return word_sum
	
def wordComparison(authorx,bookx,authory,booky):
	#get histograms, build word sets
	hist1 = getWordFreq(bookx)
	s1 = []
	for key in hist1:
		s1.append(key)
	s1=set(s1)
	
	hist2 = getWordFreq(booky)
	s2 = []
	for key in hist2:
		s2.append(key)
	s2 = set(s2)
	
	#displays unique words, totals and relative frequencies
	sumx = statistics(hist1,authorx)
	sumy = statistics(hist2,authory)
	
	#displays word differences, and  more (different) relative frequencies.
	print authorx, 'used', len(s1-s2), 'words that', authory, 'did not use'
	print 'Relative frequency of words used by', authorx, 'but not used by', authory, ' = ', (float(len(s1-s2))/sumx)*100,'\n'
	print authory, 'used', len(s2-s1), 'words that', authorx, 'did not use'
	print 'Relative frequency of words used by', authory, 'but not used by', authorx, ' = ', (float(len(s2-s1))/sumy)*100,'\n'
	
#we can use the dictionary of english words as a filter for proper names.
def main():
	while True:
	#input loops
		try:
			book1 = raw_input('Enter the name of the first book:\n')
			book1 = open(book1,'r')
			break
		except(TypeError, IOError):
			print 'Something went wrong, please try again'
	while True:
		try:
			book2 = raw_input('Enter the name of the second book:\n')
			book2 = open(book2,'r')
			break
		except(TypeError, IOError):
			print 'Something went wrong, please try again'	
	#no try and except statement here, because the author names don't really effect the processing. The user can call them whatever they like.
	author1 = raw_input('Please enter the author of the first book:\n')
	author2 = raw_input('please enter the author of the second book:\n')
	print '\n'
	#the heart of the program				
	wordComparison(author1,book1,author2,book2)
	
main()
	

