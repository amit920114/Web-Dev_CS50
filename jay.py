from flask import Flask 

app = Flask(__name__)

@app.route("/")
def my():
	return "My name is Amit Kumar"

@app.route("/<string:name>")
def hello(name):
	return f"my name is {name}!"