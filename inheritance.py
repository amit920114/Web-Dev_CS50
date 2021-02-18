from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def sublime():
	return render_template("sublime.html")

@app.route("/text")
def text():
	return render_template("text.html")