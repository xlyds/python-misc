#  File: Goldbach.py

#  Description: Creates goldbach partitions given an even int

#  Student Name:Zach Tidwell

#  Student UT EID: zt659

#  Course Name: CS 303E

#  Unique Number: 91245

#  Date Created: 7/17/11

#  Date Last Modified: 7/17/11



########################################################################################################################

# GoldBach.py

def isPrime (n):
  limit = int (n ** 0.5 + 1)
  for i in range (2, limit):
    if (n % i == 0):
      return False
  return True

primelist = []           

for i in range(2,100):
  if isPrime(i):
   primelist.append(i)   #generates a list a primes from 2 to 100 which will be the backbone of main().
  
''' the modus operandi for main() is as follows. We traverse primelist and test the items by picking two and summing them. If they sum
to the target value, m, we append them into a sublist of primelist, prime_sublist. To avoid repeats in prime_sublist we check
to see if it has already been used by comparing each new test item to every element in prime_sublist. The list will only be appended by newly
encountered pairs from primelist that sum to m. Each time the sublist is appended, each item is converted into a string and concatenated and 
used to update the string, gold_part, which contains all of the unique Goldbach partitions for m. gold_part is printed when primelist is exhausted.
the process is repeated until a full list of unique goldbach partitions for every even integer from 4 to 100 is generated.'''

def main():
             
  for m in range(4, 101, 2):           
    prime_sublist = []                 #initializes the sublist with the empty list.   
    gold_part = str(m)                 #intializes the output string with the current m.
    for i in primelist:
      for j in primelist:
        if (m == i+j):
          used = False               #the used boolean will determine if i and j make the sublist
          for k in prime_sublist:    
            if (i==k or j==k):
       	      used = True
       	  if (not used):
            prime_sublist.append(i)                      
            prime_sublist.append(j)	
            gold_part += ' = ' + str(i) + ' + ' + str(j)   #when we construct gold_part this way, we can be sure that the result is of the form 
                                                             #m = a1+b1=...=ak+bk with ai<=bi because primelist is traversed in ascending order.		  		  
    print gold_part
          
main()

					
		    
		    
		