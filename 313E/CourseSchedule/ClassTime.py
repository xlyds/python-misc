#  File: ClassTime.py
#
#  Description: object that represents the temporal coordinates of the course class
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 10/29/11
# 
#  Date Last Modified: 10/29/11
############################
class ClassTime:
	'''Represents the days of the week and time of day for a course'''
	def __init__(self,days,hours):
		self._days = days
		self._hours = hours
		
	def getDays(self):
		return self._days
		
	def getHours(self):
		return self._hours
		
	def hourTostring(self):
		return str(self._hours)
		