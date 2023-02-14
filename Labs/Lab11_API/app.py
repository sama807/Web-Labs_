from flask import Flask, jsonify,request,render_template
from flask_restful import Api,Resource
from database import db
from resources import routes


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/inventory'
}
api=Api(app)
db.initialize_db(app)
routes.initalize_routes(api)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("chat.html")


@app.route('/showContacts')
def showContacts():  # put application's code here
    return render_template("showContacts.html")

@app.route('/showInventory')
def showInventory():  # put application's code here
    return render_template("showInventory.html")

@app.route('/addInventory')
def addInventory():  # put application's code here
    return render_template("showHtmlData.html")

if __name__ == '__main__':
    app.run()
