from .student import Student
from .course import Course

class Mark:
    def __init__(self,student,course,score):
        self.__student=student
        self.__course=course
        self.__score=score
    
    def getStudent(self):
        return self.__student
    
    def getCourse(self):
        return self.__course

    def getScore(self):
        return self.__score

    