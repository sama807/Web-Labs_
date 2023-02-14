
from user import user
from db import myDB

class controller:
    def validateName(self,name):
        dbobj=myDB('localhost','root','SAMA786000','addressbook2')
        status= dbobj.isNameDuplicate(name)
        if status:
            return True
        else:
            return False

    def isPassValid(self,password):
        if(len(password)>=8):
            return True
        else:
            return False



