#  File: Courselist.py
#
#  Description: hashtable of course objects
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 10/29/11
#
#  Date Last Modified: 11/16/11

##############################
from Course import*
class Courselist:
	'''mapping of course name to course objects'''
	def __init__(self):
		self._courses = {}
		
	def isEmpty(self):
		return self._courses == {}
		
	def courseListed(self, courseName):
		return courseName in self._courses
	
	def getCourse(self, courseName):
		if courseName in self._courses:
			return self._courses[courseName]
		else:
			return str('Course ' + courseName + ' not in catalog')
			
	def addcourse(self, courseName, CourseObject):
		self._courses[courseName] = CourseObject
		
	def listCourses(self):
		if self.isEmpty():
			print('catalog is empty!')
		else:
			for key in self._courses:
				c = self._courses[key]
				print(c)
	
	def searchByUniqueNumber(self, UniqueNumber):
		for key in self._courses:
			if self._courses[key].getUnique()==UniqueNumber:
				return(self._courses[key])
		print('Unique number not found!')
	
	def searchByCourseNumber(self,courseNumber):
		found = []
		for key in self._courses:
			if self._courses[key].getDepartment() + str(self._courses[key].getCourseNumber()) == courseNumber:
				found.append(self._courses[key])
		if found==[]:
			print('Course Number ' + str(courseNumber) + ' not found.')
		return found
		
	def searchBydepartment(self, department):
		found=[]
		for key in self._courses:
			if self._courses[key].getDepartment()==department:
				found.append(self._courses[key])
		if found == []:
			print('Department not found!')
		return found
		
	def searchBydays(self, days):
		found = []
		for key in self._courses:
			if self._courses[key].getDays()==days:
				found.append(self._courses[key])
		if found == []:
			print('No courses meet on these days.')
		return found
	
	def searchBytime(self, time):
		found = []
		for key in self._courses:
			if self._courses[key].getTime()==time:
				found.append(self._courses[key])
		if found == []:
			print('No courses meet at this time.')
		return found
	
		
		