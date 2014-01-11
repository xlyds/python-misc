#  File: Student.py
#
#  Description: student class
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
from Schedule import*
class Student:
	
	def __init__(self, name):
		self._name = name
		self._schedule = Schedule(self._name)
	
	def isEmpty(self):
		return self._schedule=={}
		
	def getName(self):
		return self._name
	
	def getSchedule(self):
		return self._schedule
		
	def hasCourse(self, courseNumber):
		return len(self._schedule.searchbyCourseNumber(courseNumber))==1
		
	def addCourse(self, courseName, courseObject):
		self._schedule.addCourse(courseName, courseObject)
		
	def getClass(self, courseName):
		return self._schedule[courseName]
	
	def __str__(self):
		if self._schedule.isEmpty():
			return 'student is not currently enrolled'
		else:
			 self._schedule.listCourses()