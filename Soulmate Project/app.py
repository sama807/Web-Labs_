from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_session import Session
from flask_restful import Api, Resource
from database import db
from resources import routes
from database.models import User
import os, random, math, smtplib
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/soulmate'
}
api = Api(app)
db.initializeDB(app)
routes.initializeRoutes(api)

app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
Session(app)

# sama
global myOTP, email
myOTP = ""
email = " "


def sendOTP():
    myOTP = ""
    digits = "0123456789"
    for i in range(6):
        myOTP += digits[math.floor(random.random() * 10)]
    session["otp"] = myOTP
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("samarafaqat091@gmail.com", "uuldugoyfvfvvxnp")
    s.sendmail('&&&&&&&&&&&', session["signupData"]["email"], myOTP)
    return myOTP


@app.route('/')
def login():
    if "login" in session:
        return render_template("home.html")

    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def saveData():
    if request.method == "GET":
        return redirect("/")

    email = request.form["email"]
    password = request.form["password"]
    userData = User.objects(email=email)
    print(userData)
    print(len(userData))
    if (userData and userData[0]["password"] == password):
        session["signupData"] = userData[0]
        session["login"] = "1"
        return render_template("home.html")
    if not userData:
        return render_template('login.html', password="Invalid email")
    else:
        return render_template('login.html', password="password is incorrect")


@app.route("/logout")
def logout():
    if 'login' in session:
        session.clear()
    return redirect('/')


@app.route("/getEmail")
def getEmailToRecoverAcc():
    if 'login' in session:
        return redirect('/')
    return render_template("getEmailToRecoverAcc.html")


@app.route("/emailData", methods=["POST"])
def PostEmailData():
    try:
        global email
        email = request.form["useremail"]
        user = User.objects(email=email).to_json()

        global myOTP
        if len(user) == 2 or email == "":
            return render_template("getEmailToRecoverAcc.html", msg="Email not exists")
        else:
            digits = "0123456789"
            for i in range(6):
                myOTP += digits[math.floor(random.random() * 10)]

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("samarafaqat091@gmail.com", "uuldugoyfvfvvxnp")
            s.sendmail('&&&&&&&&&&&', email, myOTP)
            return render_template("getOTP.html")
    except Exception as e:
        print(str(e))
        return "exception"


@app.route("/getOtp", methods=["POST"])
def getOTP():
    if 'login' in session:
        return redirect('/')
    userOtp = request.form["otp"]
    if (userOtp == myOTP):
        return render_template("resetPassword.html")
    else:
        return render_template("getOTP.html", msg="Check Otp again")



@app.route("/resetPassword", methods=["POST"])
def resetPassword():
    try:
        newPass = request.form["prePass"]
        confirmPass = request.form["newPass"]
        if (newPass == confirmPass):
            user = User.objects.get(email=email).update(password=newPass)
            return render_template("login.html", password="password changed successfully")
        else:
            return render_template("resetPassword.html", msg="Password doesn't match")

    except Exception as e:
        print(str(e))


# /sama

@app.route('/signup')
def signup():
    if "login" in session:
        return redirect('/')
    return render_template("signup.html")


@app.route('/verify')
def verify():
    if 'otp' in session:
        return render_template("emailVerify.html")
    return redirect('/')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if 'login' in session:
        if (request.method == "GET"):
            pic = session["signupData"]["profilePic"]
            name = session["signupData"]["firstName"] + " " + session["signupData"]["lastName"]
            return render_template("profile.html", pic=pic, name=name, uname=session["signupData"]["username"],
                                   gender=session["signupData"]["gender"], email=session["signupData"]["email"])

        pic = request.files['img']

        if pic.filename == '':
            return redirect("/")

        picname = secure_filename(pic.filename)
        list = picname.split('.')
        type = "jpg"
        for i in list:
            type = i
        picname = session["signupData"]["username"] + "." + type
        pic.save(os.path.join("./static/images", picname))

        session["signupData"]["profilePic"] = "../static/images/" + picname
        User.objects.get(username=session["signupData"]["username"]).update(
            profilePic=session["signupData"]["profilePic"])

        return redirect("/profile")
    return redirect('/')


app.run(debug=True)