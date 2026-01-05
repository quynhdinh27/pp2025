from .student import Student
from .course import Course
from .mark import Mark

class School:
    def __init__(self):
        self.__students = []
        self.__courses=[]
        self.__mark=[]
    
    def inputStudent(self):
        n = int(input("Number of student:"))
        for _ in range(n):
            s = Student()
            s.input()
            self.__students.append(s)
    def sortStudent(self):
        self.__students.sort()

    def inputCourses(self):
        n = int(input("Number of Courses:"))
        for _ in range(n):
            c= Course()
            c.input()
            self.__courses.append(c)
    def inputMarks(self):
        for s in self .__students:
            for c in self.__courses:
                score = float(input(f"Mark of {s.getName()} for {c.getName()}:"))
                m = Mark(s,c,score)
                self.__mark.append(m)
    def inputSchool(self):
        for s in range(self.__students):
            for c in range(self.__courses):
                score = float(input(
                f"Mark of {s.getName()} for {c.getName()}: "))
            self.__marks.append((s.getID(), c.getID(), score))

    def calculateGPA(self, student_id):
        total = 0
        count = 0
        for m in self.__mark:

            if m.getStudent().getID() == student_id:
                total += m.getScore()
                count += 1

            if count == 0:
                return 0

        return total/count


    def printGPA(self):
        for s in self.__students:
            gpa = self.calculateGPA(s.getID())
            print("GPA of", s.getName(), "is:", gpa)


                    