from flask import Flask 

app=Flask(__name__)
@app.route("/string:name")
def hello(name):
	return f"My name is {name}!"