from .entity import Entity

class Student(Entity):
    def __init__(self):
        super().__init__()
        self.__dob=""
        

    def input(self):
        super().input()
        self.__dob = input("DoB:")
    
    
    def print(self):
        super().print
        print("DoB is:",self.__dob)
        

