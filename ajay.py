from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
	headline = "Hello, World!"
	return render_template("ajay.html", headline=headline)