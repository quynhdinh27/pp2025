class Course:
    def __init__(self):
        self.__id=""
        self.__name=""

    def input(self):
        self.__id=input("Course ID:")
        self.__name = input("Course name:")
    
    def getName(self):
        return self.__name
    def getID(self):
        return self.__id