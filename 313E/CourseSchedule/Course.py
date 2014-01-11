#  File: Courses.py
#
#  Description: Object that represents a course
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

################################

from ClassTime import*

class Course:
	'''Course have the following attributes:
		1) Unique number
		2) Course department
		3) Course Number
		4) Course Name
		5) Time
		6) Location
		7) instructor'''
		
	def __init__(self, unique, dept, num, name, loc, instr, ClassTime):
		self._unique = unique
		self._dept = dept
		self._num = num
		self._name = name
		self._instr = instr
		self._loc = loc
		self._days = ClassTime.getDays()
		self._time = ClassTime.getHours()
		self._tempcoord = ClassTime
	def getUnique(self):
		return self._unique
		
	def getDepartment(self):
		return self._dept
		
	def getCourseNumber(self):
		return self._num
		
	def getCourseName(self):
		return self._name
		
	def getTime(self):
		return self._tempcoord.getHours()
		
	def getDays(self):
		return self._tempcoord.getDays()
		
	def getLocation(self):
		return self._loc
		
	def getInstructor(self):
		return self._instr
		
	def __str__(self):
		timeAdjust ='' 
		if int(self._time)<11:
			timeAdjust=str(int(self._time)+1)+'am'
		elif int(self._time)==11:
			timeAdjust='12pm'
		else:
			timeAdjust=str((int(self._time)+1)%12)+'pm'
		return(self._unique+' : '+self._dept+self._num+' ('+self._name+') '+' '+self._days+' '+timeAdjust+' '+self._loc+' '+self._instr)
	
		