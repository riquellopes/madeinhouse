#coding: utf-8
from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object("settings")

@app.route("/")
def home():
	return render_template("index.html")