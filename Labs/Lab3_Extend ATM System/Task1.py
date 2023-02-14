import pymysql
class user:
    def __init__(self,accountNo, password, balnc):
        self.__accountNo= accountNo
        self.__password= password
        self.__accountBalance= balnc

    @property
    def accountNo(self):
        return self.__accountNo

    @accountNo.setter
    def accountNo(self, a):
        self.__accountNo = a
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, a):
        self.__password = a
    @property
    def accountBalance(self):
        return self.__accountBalance
    @accountBalance.setter
    def accountBalance (self,b):
        self.__accountBalance = b

class dbhandler(Exception):
    pass
class Database:
    def __init__(self,host,user,password,port,database):
        self.host=host
        self.user = user
        self.port=port
        self.password=password
        self.database=database
    def print(self):
        mydb = None
        mydbCursor=None
        try:
            # Get DB Connection
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            mydbCursor = mydb.cursor()
            mydbCursor.execute("Select* from users")
            users = mydbCursor.fetchall()
            for user in users:
                print(user)

        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()
            if mydb != None:
                mydb.close()

class ATM(user):
    def __init__(self,accountNo, password, balnc):
        user.__init__(accountNo, password, balnc)

    def registerAccount(self,accountNo, password):
        self.accountNo=accountNo
        self.password=password
a= user("123",123,100)
a.accountNo="123"
print(a.accountNo)
a= Database('localhost','root','SAMA786000',3306,'new_schema1')
a.print()