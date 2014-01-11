#  File: Schedule.py
#
#  Description: Schedule class
#
#  Student's Name: Zach Tidwell	
#
#  Student's UT EID: ZT659
#
#  Course Name: CS 313E 
#
#  Date Created: 11/15/11
#
#  Date Last Modified:
##################################
from CourseList import*
class Schedule(Courselist):
	
	def __init__(self,studentName):
		self._name = studentName
		self._courses = {}
		
	def addCourse(self, courseName, courseObject):
		self._courses[courseName] = courseObject
		
	