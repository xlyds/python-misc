#Pascal's Triangle
from math import factorial as f
class PT:
	"""pascal's triangle using modular arithmetic"""
	'''def build_PT(rows,modi):
		previous=[0]
		for i in range(rows):
			current=[0]*i
			for j in range(i):
				current[j] = (previous[j]-previous[j-1])%modi  #C. Pickover
			previous=current'''
	
	
	def __init__(self,rows,mod_index):
		self._modi = mod_index
		self._rows = rows
		previous=[0]
		for i in range(self._rows+1):
			current=[0]*i
			for j in range(i+1):
				current[j] = (previous[j]-previous[j-1])%self._modi  #C. Pickover
			previous=current
	
		
	def getEntry(self,col,row):
		return f(row)/(f(col)*f(row-col))
	#def getRow(self,row):
		