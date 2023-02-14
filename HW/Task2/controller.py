
from myDB import myDB
from student import student
from faculty import faculty
from user import user
from view import studentView
from view import facultyView
from myDB import myDB


class controller:
    def controllerregisterStudent(self):
        stdView= studentView()
        st= stdView.registerStudent()
        dB= myDB('localhost','root','SAMA786000','fcit')
        dB.insertStudentData(st)

    #checking semester validity
    def semValidity(self,semester):
        if semester < 1 and semester > 8:
          return False
        return True
   #checking passwordValidity
    def passwordValidity(self,password):
        if(int(len(password))!=5):
            return False
        else:
            return True
        #View Student profile
    def viewStdProfile(self):
        db= myDB('localhost','root','SAMA786000','fcit')
        db.viewStdProfile()

    # View Faculty profile
    def viewFacProfile(self):
        db = myDB('localhost', 'root', 'SAMA786000', 'fcit')
        db.viewFacProfile()
