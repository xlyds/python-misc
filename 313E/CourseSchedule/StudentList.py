#  File: StudentList.py
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

from Student import*
class StudentList:
	''' A map of student names to student objects. represents enrolled students.'''
	
	def __init__(self):
		self._students = {}
		
	def isEmpty(self):
		return self._students == {}
		
	def isEnrolled(self, student):
		return (student in self._students)
		
	def getStudent(self, student):
			return self._students[student]
			
	def addStudent(self, student, studentObject):
		self._students[student] = studentObject
		
	def __str__(self):
		if self.isEmpty():
			return 'no students currently enrolled'
		else:
			for student in self._students:
				print(type(student)) 
		