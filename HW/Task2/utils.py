from view import studentView
from view import facultyView
from controller import controller
from myDB import myDB

print("---------------WELCOME TO STUDENT MANAGEMENT SYSTEM-----------------")
print("1- Register\n" "2-Login\n" "3-View Profile\n" "4-Edit Profile\n" "5-Delete Profile\n")
n = int(input("Enter 1-5 to coninue: "))
stdView= studentView()
facView= facultyView()
con = controller()
db=myDB()
if(n==1):
    reg = int(input("Register as student or faculty? Enter 1 for student and 2 for faculty: "))
    if reg == 1:
        stdView.registerStudent()
    else:
        facView.registerFaculty()
elif(n==2):
    stdView.login()
elif(n==3):
    prof=int(input("Enter 1 to view student profile and 2 to view faculty profile"))
    if(prof==1):
        con.viewStdProfile()
    else:
        con.viewFacProfile()
elif(n==4):
    prof=int(input("Enter 1 to edit student profile and 2 to faculty: "))
    if(prof==1):
        db.editStuProfile()
    else:
        db.editFacProfile()
elif(n==5):
    prof= int(input("Enter 1 to delete student profile and 2 to faculty: "))
    if(prof==1):
        db.deleteStuProfile()
    else:
        db.deletFacProfile()














