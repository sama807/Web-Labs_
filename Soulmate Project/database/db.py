from flask_mongoengine import MongoEngine

db=MongoEngine()
def initializeDB(app):
    db.init_app(app)