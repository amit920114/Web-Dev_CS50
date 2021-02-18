from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index(): #function name--> it's up to you not compulsory
	return render_template("index.html")