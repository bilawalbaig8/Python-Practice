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

    def recordMarks(self, english, urdu, math):
        self.__english = english
        self.__urdu = urdu
        self.__math = math

    def showTotalMarks(self):
        print("\nMarks of ", self.name)
        print("English : ", self.__english)
        print("Urdu : ", self.__urdu)
        print("Math : ", self.__math)
        print("Total Marks are:" , self.__english + self.__urdu + self.__math)
        print("==================================================")



"""  Creating the objects   """


students.showSchoolName()

std1 = students("1","Bilawal Baig" , "8" , "B")
std1.recordMarks(50,60,70)
std1.showStudentData()
std1.showTotalMarks()

std2 = students("2","Asim" , "8" , "A")
std2.recordMarks(70,50,80)
std2.showStudentData()
std2.showTotalMarks()