class Student:
	def __init__(self,id,name,dob):
		self.__id=id
		self.__name=name
		self.__dob = dob

	def getName(self):
		return self.__name
	def getID(self):
		return self.__id
class  Course:
	def __init__(self,id, name):
		self.__id = id
		self.__name = name
	def getID(self):
		return self.__id
	def getName(self):
		return self.__name

class School:

	def __init__(self,list_student,list_courses,list_mark):
		self.__list_student = list_student
		self.__list_courses = list_courses
		self.__list_mark= list_mark
	def list_student(self):
		return self.__list_student
	def list_courses(self):
		return self.__list_courses
	def list_all_marks(self):
		message =''
		for i in range(len(self.__list_student)):
			for j in range (len(self.__list_courses)):
				student = self.__list_student[i]
				course = self.__list_courses[j]
				key = (student.getID(),course.getID())
				marks = self.__list_mark.get(key, "N/A")
				message += f"{student.getName()}-{course.getName()}:{marks}\n"
		return message
s1=Student("1","Lily","1/1/2006")
s2=Student("2","Lala","2/2/2005")
s3=Student("3","Hihi","3/3/2008")
student=[s1,s2,s3]

c1 = Course("Calculus","01")
c2 = Course("OOP","02")
course=[c1,c2]
marks={}
marks[s1.getID(), c1.getID()]=18
marks[s3.getID(), c2.getID()]=15
marks[s2.getID(), c2.getID()]=19
school = School(student,course, marks)
print(school.list_all_marks())

