import pymysql

class myDB:

        def __init__(self, host, user, password, database):
            self.host = host
            self.user = user
            self.password = password
            self.database = database

        def viewStdProfile(self):
            mydb = None
            mydbCursor = None
            try:
                mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                # Get cursor object
                mydbCursor = mydb.cursor()
                sql = "Select* from student"
                mydbCursor.execute(sql)
                myresults = mydbCursor.fetchall()

                print("ID\t" "Semest\t" "CGPA\t" "Major\t" "User Id\t")
                for r in myresults:
                  print(r[0],"\t" ,r[1],"\t\t" ,r[2],"\t" ,r[3],"\t" ,r[4])
            except Exception as e:
                print(str(e))
            finally:
                if mydbCursor != None:
                    mydbCursor.close()
                if mydb != None:
                    mydb.close()
        def viewFacProfile(self):
            mydb = None
            mydbCursor = None
            try:
                mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                # Get cursor object
                mydbCursor = mydb.cursor()
                sql = "Select* from faculty"
                mydbCursor.execute(sql)
                myresults = mydbCursor.fetchall()

                print("ID\t" "Designation\t\t" "Subject\t\t" "User Id")
                for r in myresults:
                    print(r[0], "\t", r[1], "\t\t", r[2],"\t\t", r[3])
            except Exception as e:
                print(str(e))
            finally:
                if mydbCursor != None:
                    mydbCursor.close()
                if mydb != None:
                    mydb.close()
        def insertStudentData(self,Stu):
            mydb = None
            mydbCursor = None
            try:
                mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                # Get cursor object
                mydbCursor = mydb.cursor()
                sql = "insert into student(semester,cgpa,major)  values(%s,%s,%s)"
                args=(Stu.semester, Stu.cgpa, Stu.major)
                mydbCursor.execute(sql,args)
                myresults = mydbCursor.fetchall()

                print("ID\t" "Designation\t\t" "Subject\t\t" "User Id")
                for r in myresults:
                    print(r[0], "\t", r[1], "\t\t", r[2], "\t\t", r[3])
            except Exception as e:
                print(str(e))
            finally:
                if mydbCursor != None:
                    mydbCursor.close()
                if mydb != None:
                    mydb.close()
        def editStuProfile(self):
            pass
        def editFacProfile(self):
            pass
        def deleteStuProfile(self):
            pass
        def deletFacProfile(self):
            pass

#
# db= myDB('localhost','root','SAMA786000','fcit')
# db.viewStdProfile()
# print("-------------------------")
# db.viewFacProfile()