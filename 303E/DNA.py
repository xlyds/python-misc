#DNA.py:
#  File: DNA.py

#  Description: computes common dna substrings given two strands

#  Student Name:Zach Tidwell

#  Student UT EID: ZT659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 7/22/11

#  Date Last Modified: 7/22/11

#########################################################################################################

'''
modus operandi: first we will determine the shortest string, call it small. Then we will generate a list of substrings of small, however, substrings of small will only
make the list if they are also found in the larger string and if they are greater than two. If there are no common substrings, the user is notified. Then we will 
determine the length of the largest substring and then we will print all substrings in our list that are equal to this length.'''

def main():

  while True:
    try:
      a = raw_input('enter strand 1:')                                   #input loops for the two strands. Checks in place to insure valid DNA sequences are entered
      for char in a:
        if (char!='A' and char!='C' and char!='G' and char!='T'):
          raise
	pass
      break		
    except (ValueError, TypeError, NameError):
      print 'please enter a DNA sequence'

  while True:
    try:
      b = raw_input('enter strand 2:')
      for char in b:
	if (char!='A' and char!='C' and char!='G' and char!='T'):
	  raise
	pass
      break
    except (ValueError, TypeError, NameError):
      print 'please enter a DNA sequence'

  small = min(a,b)                                                  
  big = max(a,b)
  comsublist=[]                                                      #initializes the list in which we will place the substrings of the small entry

  for i in range(len(small),0,-1):                                #beginning of loop to generate common substring list
    for j in range(0,len(small)-i+1):
      if (big.find(small[j:j+i])!=(-1) and len(small[j:j+i])>1):  #places the substrings in the sublist, given that the conditions are met.
        comsublist.append(small[j:j+i])                             

  if comsublist==[]:
    print "no common DNA substring, try again"
    main()

  for x in range(len(comsublist)):                                   #loop to determine the length of the greatest common strings
    m = len(comsublist[0])
    if (len(comsublist[x])>max):
      m = len(comsublist[x])

  for item in comsublist:                                            #prints out the common substrings
    if len(item)==m:
      print item

  while True:                                                     #prompts the user to restart the program.
    try:
      ag = raw_input('Again? y/n?')
      if (ag=='y' or ag=='yes'):
	main()
      elif (ag=='n' or ag=='no'):
	print 'goodbye!'
	quit()
      raise
    except (ValueError, NameError, TypeError, SyntaxError):
      print 'Invalid. Please enter y or n'

main()
	




		
		
		
