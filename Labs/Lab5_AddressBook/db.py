import pymysql
from contact import contact
from myException import DuplicateName
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


        def findContactName(self,contactName):
            try:
                query= "SELECT* from contacts where Name=%s "
                args=contactName
                self.mycursor.execute(query,args)
                result= self.mycursor.fetchall()
                if(len(result)==0):
                    return True
                else:
                     raise DuplicateName("duplicate name")
            except DuplicateName as e:
                      return False
            except Exception as e:
                print(str(e))

        def show_contacts(self):
            try:
                query = "SELECT * FROM contacts"
                self.mycursor.execute(query)
                result = self.mycursor.fetchall()
                contctlist=[]
                for i in result:
                    contctlist.append(i)
                return contctlist
            except Exception as e:
                print(str(e))


db= myDB('localhost','root','SAMA786000','addressbook')
db.show_contacts()
# db.insertContact()
#db.findContactName()
