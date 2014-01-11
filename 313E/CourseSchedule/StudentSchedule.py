
#  File: StudentSchedules.py
#
#  Description: Allows user to query a dictionary of course objects
#
#  Student's Name: Zach Tidwell
#
#  Student's UT EID: zt659
#
#  Course Name: CS 313E 
#
#  Date Created: 11/1/11
#
#  Date Last Modified: 11/2/11

###############################
from StudentList import*
from CourseList import*
def printHelp():
	print("""
     help
        see a useful list of available commands

     catalog
        see list of available courses

     info COURSENAME
        give all information about the course
  
     info UNIQUENUMBER
        give all information about the course 

     courses department DEPTID
        list all courses for a given department

     courses days DAYS
        list all courses on given days (e.g., TT, MWF)

     courses time TIME 
        list all courses that begin at a specific time 
        (must specify am or pm [all classes start on the hour])
		
	 enroll STUDENT
        add a student to the Students Database with empty schedule

     add STUDENT COURSENAME
        assuming the student exists in the database, add the course to that
        student's schedule

     schedule STUDENT
        print information on the student named
		
     stop or quit or exit
        exit the system\n""")
		
def createCourseList():
	courseDatabase = Courselist()
	# this is just the sample file I used for development. I wasn't sure if I was to specify are file path.
	input = open('Sample.txt','r')
	for line in input:
		input = line.split(':')
		#the following reassignments are for the human user:
		unique = input[0]
		dept = ''
		for char in input[1]:
			if char.isalpha():
				dept+=char
			else:
				break
		num = input[1]
		purenum = input[1].strip(dept)
		name = input[2]
		days = input[3]
		meetTime = input[4]
		loc = input[5]
		instr = input[6].strip('\n')
		course = Course(unique,dept,purenum,name,loc,instr,ClassTime(input[3],input[4]))
		print('Adding course', course.getDepartment()+course.getCourseNumber())
		courseDatabase.addcourse(num, course)
	return courseDatabase
		
def interface(courseDatabase, studentDatabase):
	while True:
		try:
			n = input('Query database: ')
			if n == 'stop' or n == 'quit' or n== 'exit':
				break
			n = n.split(' ')
			if len(n)==1:
				if n[0] == 'catalog':
					courseDatabase.listCourses()
				elif n[0] == 'help':
					printHelp()
				else:
					raise
			elif len(n)==2 and n[0]=='info':
				if n[1].isdigit():
					print(courseDatabase.searchByUniqueNumber(n[1]))
				else:
					p = n[1].upper()
					courses = courseDatabase.searchByCourseNumber(p)
					for course in courses:
						print(course)					
			elif len(n)==2 and n[0] == 'enroll':
				if studentDatabase.isEnrolled(n[1]):
					print('Student is already enrolled!')
				else:
					print('enrolling: ', n[1])
					studentObject = Student(n[1])
					studentDatabase.addStudent(n[1],studentObject)	
			elif len(n)==2 and n[0] == 'schedule':
				if studentDatabase.isEnrolled(n[1]):
					print('Fetching schedule for: ',n[1])
					studentObject = studentDatabase.getStudent(n[1])
					scheduleObject = studentObject.getSchedule()
					scheduleObject.listCourses()
				else:
					print('student is not registered for any classes')
			elif len(n)==3 and n[0]=='courses':
				if n[1]=='department':
					p = n[2].upper()
					courses = courseDatabase.searchBydepartment(p)
					for course in courses:
						print(course)
				elif n[1] == 'days':
					p = n[2].upper()
					courses = courseDatabase.searchBydays(p)
					for course in courses:
						print(course)
				elif n[1]== 'time'	:
					time=''
					if int(n[2].strip('amp'))>23:
						print('not a valid time of day')
						interface(courseDatabase)
					elif 'pm' in n[2]:
						time = str((int(n[2].strip('pm'))%12)+11)
					elif n[2]=='12am':
						time = '23'
					elif 'am' in n[2]:
						time = str((int(n[2].strip('am'))-1)%12)
					else:
						raise
					courses = courseDatabase.searchBytime(time)
					for course in courses:
						print(course)
				else:
					raise	
			elif len(n)==3 and n[0]== 'add':
				p = n[2].upper()
				if studentDatabase.isEnrolled(n[1]):
					if courseDatabase.courseListed(p):
						print('Adding course: ', p, ' to schedule')
						studentObject = studentDatabase.getStudent(n[1])
						courseObject = courseDatabase.getCourse(p)
						studentObject.addCourse(p,courseObject)
					else:
						print ('Course ',p,' is not offered at this time')
				else:
					print ( n[1] ,' is not enrolled')
			else:
				raise
		except (ValueError,RuntimeError):
			print ('command not recognized')
			printHelp()
		
def main():
	courseDatabase = createCourseList()
	studentDatabase = StudentList()
	interface(courseDatabase, studentDatabase)
main()