from flask import Flask, render_template, request
from contact import contact
from db import myDB
from controller import contactController

app = Flask(__name__)


@app.route('/')
def displayForm():
        return render_template("create_contact.html")


@app.route('/save_data',methods=["POST"])
def create_contact():

    name= request.form["name"]
    no= request.form["Mobile no"]
    city= request.form["City"]
    profession= request.form["Profession"]
    contct= contact(name,no,city,profession)
    cc= contactController()
    status= cc.validatename(name)
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
    return render_template("searc_contacts.html", data = contactList)

if __name__ == '__main__':
    app.run()
