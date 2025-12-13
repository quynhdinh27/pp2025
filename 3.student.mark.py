import math
import numpy as np



class Student:
	def __init__(self, sid, name, dob):
		self.__id = sid
		self.__name = name
		self.__dob = dob


	def getID(self):
		return self.__id


	def getName(self):
		return self.__name




class Course:
	def __init__(self, cid, name, credit):
		self.__id = cid
		self.__name = name
		self.__credit = credit


	def getID(self):
		return self.__id


	def getName(self):
		return self.__name


	def getCredit(self):
		return self.__credit




class School:
	def __init__(self, students, courses, marks):
		self.__students = students 
		self.__courses = courses 
		self.__marks = marks 

	def studentGPA(self, student_id):
		total_weight = 0.0 #weight=score*credit
		total_credit = 0.0

		for c in self.__course:
			key = (student_id, c.getID())
			if key in self.__marks:
				mark = self.__mark[key]
				total_weight += mark *c.getCredit()
				total_credit +=c.getCredit()
			if total_credit ==0:
				return 0.0
			return total_weight/toal_credit


	def sortGPA(self):
		def gat_gpa(Student):
			return self.studentGPA(student.getID())
		return sorted(self.__students, key=get_gpa, reverse = True)
		
	def all_marks(self):
		out =""
		for s in self.__students:
			for c in self.__course:
				key = (s.getID(), c.getID())
				mark = self.__marks.get(key, "N/A")
				out += f"{s.getNAme()}-{c.getName()} : {mark}\n"
		return out
# Students
s1 = Student("1", "Lily", "1/1/2006")
s2 = Student("2", "Lala", "2/2/2005")
s3 = Student("3", "Hihi", "3/3/2008")
students = [s1, s2, s3]


# Courses (id, name, credit)
c1 = Course("01", "Calculus", 3)
c2 = Course("02", "OOP", 4)
courses = [c1, c2]


# Marks (rounded down to 1 decimal using math.floor)
marks = {}
marks[("1", "01")] = math.floor(18.78 * 20) / 20
marks[("3", "02")] = math.floor(15.96 * 20) / 20
marks[("2", "02")] = math.floor(19.24 * 20) / 20


# Convert marks to numpy array (for demo purpose)
mark_array = np.array(list(marks.values()))


school = School(students, courses, marks)
school.all_marks()


print("Students sorted by GPA :")
for s in school.sortGPA():
	gpa = school.studentGPA(s.getID())
	print(f"{s.getName()} - GPA: {gpa:.2f}")
