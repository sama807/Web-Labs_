
#while login, if user enters wrong account number
class AccountNotFound(Exception):
    pass

#While withdrawing money more than balance
class InsufficientBalance(Exception):
    pass

#While setting up pin, it should be exactly 4 digit numerical value,
class InvalidPin(Exception):
    pass

def registerAnAccount(accountNumber, accountBalance = 100):
    i = int(accountNumber)
    #i= i + 1
    print(i)
    if len(str(i)) == 1:
        tempAccountNumber = "ATM00"+str(i)
    elif len(str(i)) == 2:
        tempAccountNumber = "ATM0" + str(i)
    elif len(str(i)) >= 3:
        tempAccountNumber = "ATM" + str(i)
    accNum = tempAccountNumber
    flag = True
    while flag == True:
        try:
            password = input("Enter password: ")
            pswd = int(password)
            if len(str(pswd)) != 4:
                raise InvalidLength("Password should only contain 4 digits")
                flag = True
            else:
                flag = False
        except InvalidPin as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    with open("atmData.txt", "a") as f:
        f.write(str(tempAccountNumber))
        f.write(",")
        f.write(str(pswd))
        f.write(",")
        f.write(str(accountBalance))
        f.write("\n")

def Login():
    flag = True
    listdata = []
    i = 0
    while flag == True:
        try:
            aNum = input("Enter Account number: ")
            with open("atmData.txt", "r") as f:
                f.seek(0)
                for filedataRecord in f.readlines():
                    listdata.append(filedataRecord)
                    listfiledata = filedataRecord.split(",")
                    filedata = listfiledata[0]
                    print(aNum)
                    print(filedata)
                    if aNum == filedata:
                        pswd = input("Enter Password: ")
                        filedatapass = listfiledata[1]
                        if pswd == filedatapass:
                            print("Login succesfully ")
                            #Check Balance
                            print(listfiledata[2])
                            flag1 = True
                            while flag1 == True:
                                try:
                                    amount = print("Enter Amount to widthDarw")
                                    if amount < 0:
                                        raise InsufficientBalance("Balance is negative")
                                    elif amount > listfiledata[2]:
                                        raise InsufficientBalance("amount can not exceed from balance")
                                    else:
                                        listdata[i] = {aNum+",", pswd+",", listfiledata[2] - amount}
                                        flag = False
                                except InsufficientBalance as e:
                                    print(str(e))
                        else:
                            raise InvalidPin("Please Enter Correct Pin")
                        flag = False

        except InvalidPin as e:
            print(str(e))
        i = i + 1
try:

    registerAnAccount("1")
    registerAnAccount("3")
except Exception as e:
    print(str(e))




