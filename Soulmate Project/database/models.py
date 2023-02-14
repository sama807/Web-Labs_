from .db import db

class User(db.Document):
    email=db.StringField(required=True)
    username=db.StringField(required=True)
    password=db.StringField(required=True)
    
    firstName=db.StringField(required=True)
    lastName=db.StringField(required=True)
    CNIC=db.StringField(required=True)
    countryCode=db.StringField()
    phoneNumber=db.StringField()

    profilePic=db.StringField()
    gender=db.StringField(required=True)
    height=db.StringField(required=True)
    cast=db.StringField(required=True)
    profession=db.StringField(required=True)
    relegion=db.StringField(required=True)
    city=db.StringField(required=True)
    dob=db.StringField(required=True)
