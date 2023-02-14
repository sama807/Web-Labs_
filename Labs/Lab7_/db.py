import pymysql
from user import user
from contact import contact
from myException import *

class myDB:

        def __init__(self, host, user, password, database):
            self.host = host
            self.user = user
            self.password = password
            self.database = database
            self.connection=None
            self.mycursor=None
            try:
                self.connection = pymysql.connect(host = self.host, user = self.user, password = self.password, database = self.database)
                self.mycursor= self.connection.cursor()
            except Exception as e:
                print(str(e))

        def insertuserData(self, user):
            try:
                query = "INSERT Into user(email,password)  VALUES(%s,%s)"
                args = (user.email, user.password)
                self.mycursor.execute(query, args)
                # r= self.mycursor.fetchall()
                # print(r)
                self.connection.commit()
            except Exception as e:
                print(str(e))

        def isNameDuplicate(self,name):
           query = "SELECT Name from contacts"
           self.mycursor.execute(query)
           result = self.mycursor.fetchall()
           for i in result:
               if i == name:
                   return False
               else:
                   return True

        def insertContact(self,contact):
            try:
                query= "INSERT Into contacts(Name,MobileNo,City,Profession)  VALUES(%s,%s,%s,%s)"
                args= (contact.Name, contact.MobileNo, contact.City, contact.Profession)
                self.mycursor.execute(query,args)
                # r= self.mycursor.fetchall()
                # print(r)
                self.connection.commit()
            except Exception as e:
                print(str(e))

        def show_contacts(self):
            try:
                query = "SELECT * FROM contacts"
                self.mycursor.execute(query)
                result = self.mycursor.fetchall()
                contctlist = []
                for i in result:
                    contctlist.append(i)
                return contctlist
            except Exception as e:
                print(str(e))

        def loginvalidity(self,name,password):
            try:
                query="Select Name Password from contacts"
                self.mycursor.execute(query)
                result = self.mycursor.fetchall()
                print(result)

            except Exception as e:
                print(str(e))



db= myDB('localhost','root','SAMA786000','addressbook2')
# a= db.loginvalidity()
s=db.isNameDuplicate("Sama")

print(s)
# db.insertContact()
#db.findContactName()
