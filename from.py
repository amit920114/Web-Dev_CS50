from flask import Flask 

app = Flask(__name__)

@app.route("/")
def amit():
	return "my name is khan"