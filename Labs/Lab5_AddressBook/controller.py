
from contact import contact
from db import myDB
import app

class contactController:
    # def __init__(self):
    #     self.contact = contact(None, None, None, None)

    def validatename(self, contactName):
        dbObj = myDB('localhost','root','SAMA786000','addressbook')
        status = dbObj.checknameDuplication(contactName)
        if status:
            return True
        else:
            return False
    def create_contactValidation(self,mobileNo):
        if(mobileNo[0]=='+'):
            return True
        else:
            return False



