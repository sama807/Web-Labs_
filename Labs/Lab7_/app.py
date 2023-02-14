from flask import Flask,render_template,request,session,make_response
from flask_session import sessions
from db import myDB
from user import user
from contact import contact
from controller import controller
app = Flask(__name__)


@app.route('/')
def signup():
    return render_template("signup.html")

@app.route('/signup',methods=["POST"])
def signupformdata():
    mail=request.form["email"]
    password=request.form["password"]
    userobj=user(mail,password)
    contobj=controller()
    status= contobj.isPassValid(password)
    if(status):
        dbobj = myDB('localhost', 'root', 'SAMA786000', 'addressbook2')
        dbobj.insertuserData(userobj)
        return render_template("create_contact.html",msg="Signup successfully")
    else:
        return render_template("signup.html",msg="Password must be greater than 8")


@app.route('/save_data',methods=["POST"])
def create_contact():

    name= request.form["name"]
    no= request.form["Mobile no"]
    city= request.form["City"]
    profession= request.form["Profession"]
    contct= contact(name,no,city,profession)
    cc=controller()
    status= cc.validateName(name)

    if status:
        tempDb = myDB('localhost', 'root', 'SAMA786000', 'addressbook')
        tempDb.insertContact(contct)
        return render_template("create_contact.html", msg="Registration successfull")
    else:
        return render_template("create_contact.html",msg="Name already exist")

@app.route('/show')
def show_contacts():
    dbObj = myDB('localhost','root','SAMA786000','addressbook')
    contactList = dbObj.show_contacts()
    return render_template("show_contact.html", data = contactList)

@app.route('/login',methods=["POST"])
def login():
    name=request.form["username"]
    password=request.form["password"]
    dbObj = myDB('localhost', 'root', 'SAMA786000', 'addressbook')
    status= dbObj.loginvalidity(name,password)
    if status:

        return render_template("show_contact.html")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()
