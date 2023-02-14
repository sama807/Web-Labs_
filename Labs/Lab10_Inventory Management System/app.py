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
def webPage():  # put application's code here
    return render_template("webPage.html")

@app.route('/updateInventory')
def update():  # put application's code here
    return render_template("update.html")

@app.route('/showInventory')
def showInventory():  # put application's code here
    return render_template("showInventory.html")

@app.route('/addInventory')
def addInventory():  # put application's code here
    return render_template("addInventory.html")

if __name__ == '__main__':
    app.run()
