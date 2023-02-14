
from student import student
from faculty import faculty
from user import user
from myException import invalidPin
from myException import invalidSemester
from myDB import myDB
from controller import controller


con = controller()
class studentView:

    #REGISTER STUDENT
    def registerStudent(self):
        name=input("Enter username: ")
        password=0
        try:
            password = input("Enter password containing 5 digts : ")
            if not con.passwordValidity(password):
                raise invalidPin("password length should be 5 only ")
        except Exception as e:
            print(str(e))

        major = input("Enter major: ")
        cgpa= (input("Enter cgpa: "))
        semester=0
        try:
            semester= int(input("Enter semester that should be 1 to 8: "))
            if not con.semValidity(semester):
                raise invalidSemester("should be 1 to 8")
        except Exception as e:
            print(str(e))
        std= student(name,password,semester,cgpa,major)
        return std

        #LOGIN
    def login(self):
        n= input("Enter username: ")
        password= input("Enter password: ")


class facultyView:

    #REGISTER FACULTY
    def registerFaculty(self):
        name = input("Enter username: ")
        password=0
        try:
            password = input("Enter password containing 5 digts : ")
            if not con.passwordValidity(password):
                raise invalidPin("password length should be 5 only ")
        except Exception as e:
            print(str(e))
        designation= input("Enter designation: ")
        subject= input("Enter subject: ")
        fac= faculty(name,password,designation,subject)
        return fac


# sv= studentView()
# sv.registerStudent()


