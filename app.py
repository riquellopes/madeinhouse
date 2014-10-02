#coding: utf-8
import datetime
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)

class Photo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(100))
	path = db.Column(db.String(200))
	
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	descriptions = db.Column(db.String(400))
	price_total = None
	price_cost = None
	markup = None
	date_created = db.Column(db.DateTime, default=datetime.now)
	date_last_update = db.Column(db.DateTime, onupdate=datetime.now)
	status = None
	
	def __repr__(self):
		return "{0} R$ {1}".format(self.name, self.price_total)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(120), unique=True)
	profile_url = db.Column(db.String(200))
	access_token = db.Column(db.String(200))
	date_created = db.Column(db.DateTime, default=datetime.now)
		
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Product, methods=['GET', 'POST', 'PUT'])

@app.route("/")
def home():
	return render_template("index.html")