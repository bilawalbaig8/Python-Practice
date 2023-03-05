'''
Class
constructor
atleast one private data member
one static variable and function
more than one object functions

create two objects to demonstrate the working of classes

'''

class students:

    schoolName = "ABC Public school"
    @staticmethod
    def showSchoolName():
        print ("\nThis is a data of" , students.schoolName)

    def __init__(self,id, name, studyclass, section):
        self.id = id
        self.name = name
        self.studyclass = studyclass
        self.section = section

    def showStudentData(self):
        print("\nStudent ID : " , self.id)
        print("Student Name : ", self.name)
        print("Student Class : ", self.studyclass)
        print("Student Section : ", self.section)

students.showSchoolName()

std1 = students("1","Bilawal Baig" , "8" , "B")
std1.showStudentData()

std2 = students("2","Asim" , "8" , "A")
std2.showStudentData()