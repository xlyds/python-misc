
#  File: EasterSunday.py

#  Description: use's Gauss's algorithm for finding the date of easter sunday

#  Student Name: Zach Tidwell

#  Student UT EID: ZT659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 6/27

#  Date Last Modified: 6/29

############################################################################
print "Greetings, user! this program calculates" 
print "the date of Easter Sunday of any common era year."
print "To get started..." 

def again():                        
  i = raw_input('Again? yes/no:\n')  #this function will be called in main()
  if i == 'yes':                     #to prompt the user to run the algo again
    main()                           #or quit.
  elif i == 'no':
    print 'Goodbye!'
  else:
    print 'invalid'
    again()

def main(): 
    y = input("Enter year:\n")     #prompts the user for desired year
    a = y%19                       #begin Gauss's algorithm
    b = y/100
    c = y%100
    d = b/4
    e = b%4
    g = (8*b+13)/25
    h = (19*a+b-d-g+15)%30
    j = c/4
    k = c%4
    m = (a+11*h)/319
    r = (2*e+2*j-k-h+m+32)%7
    n = (h-m+r+90)/25
    p = (h-m+r+n+19)%32            #end Gauss's algorithm
    if n == 3:                     #assigns and conditions month var.
      month = 'March'
    elif n == 4:
      month = 'April'
    else:
      month = 'invalid'
    if y>2011:                     #assigns and conditions tense var.
      tense = 'will be'
    else:
      tense = 'was'
    print 'In', y, 'Easter Sunday', tense, 'on', p, month        #result
    again()                       

main()


