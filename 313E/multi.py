#multi.py
a = [1,2,3,7]
def multi(a):
	if a==[]:
		return 1
	else:
		return a[0]*(multi(a[1:]))
		
print(multi(a))