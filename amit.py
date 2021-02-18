from flask import Flask 

app = Flask(__name__)
@app.route("/")
def index():
	return "Hello, World!"

@app.route("/amit")
def hello():
	return "Hello, Amit"


