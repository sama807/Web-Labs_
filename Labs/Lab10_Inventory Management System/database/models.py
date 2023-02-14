from .db import db

class inventory(db.Document):
    name=db.StringField(required=True)
    description=db.StringField(required=True)
    price=db.IntField(required=True)

class Contacts(db.Document):
    name=db.StringField(required=True)
    mobile=db.StringField(required=True)
    phone = db.StringField()
    city = db.StringField()
    web= db.StringField()
    insta= db.StringField()
    fb = db.StringField()