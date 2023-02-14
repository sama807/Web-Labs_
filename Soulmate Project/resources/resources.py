from flask import request, Response, jsonify,session,render_template
from flask_session import Session
from flask_restful import Resource
from database.models import User
import random,math,os,smtplib

def sendOTP():
    myOTP=""
    digits = "0123456789"
    for i in range(6):
        myOTP += digits[math.floor(random.random() * 10)]
    session["otp"]=myOTP
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("samarafaqat091@gmail.com", "uuldugoyfvfvvxnp")
    s.sendmail('&&&&&&&&&&&', session["signupData"]["email"], myOTP)
    return myOTP

class UserApi(Resource):
    def post(self):
        userData=request.get_json()
        print("apicall")
        error=""
        checkEmail=User.objects(email=userData["email"]).to_json()
        if(len(checkEmail)!=2):
            error=error+"E"
        checkUsername=User.objects(username=userData["username"]).to_json()
        if(len(checkUsername)!=2):
            error=error+"U"
        checkCNIC=User.objects(CNIC=userData["CNIC"]).to_json()
        if(len(checkCNIC)!=2):
            error=error+"C"
        if(userData["password"]!=userData["confirmPassword"]):
            error=error+"P"
        if(error!=""):
            print(error)
            return{'error':error},201
       
        session["signupData"]=userData
        session["otp"]=sendOTP()
        picPath="../static/images/"
        if(session["signupData"]["gender"]=="Male"):
            picPath=picPath+"profile1.jpg"
        else:
            picPath=picPath+"profile2.jpg"
        session["signupData"]["profilePic"]=picPath
        
        return{'id':"123"},200
    
class Verified(Resource):
    def post(self):
        otp=request.get_json()
        if(otp["otp"]==session["otp"]):
            session.pop('otp')
            print("hello")
            user=User(username=session["signupData"]["username"],email=session["signupData"]["email"],password=session["signupData"]["password"],firstName=session["signupData"]["firstName"],lastName=session["signupData"]["lastName"],CNIC=session["signupData"]["CNIC"],countryCode="+92",phoneNumber=session["signupData"]["phoneNumber"],profilePic=session["signupData"]["profilePic"],gender=session["signupData"]["gender"],height=session["signupData"]["height"],cast=session["signupData"]["cast"],profession=session["signupData"]["profession"],relegion=session["signupData"]["relegion"],city=session["signupData"]["city"],dob=session["signupData"]["dob"]).save()
            session["login"]="1"
            return {'id':str(user.id)},200
        print("bye")

        return{'error':"OTP is not verified"},200