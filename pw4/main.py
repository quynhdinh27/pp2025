from domain.school import School


def main():
    school = School()
    
    school.inputStudent()
    school.inputCourses()
    school.inputMarks()
    school.printGPA()

 

if __name__=="__main__":
    main()

