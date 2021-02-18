from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
	amit = " My name is Amit Kumar"
	return render_template("aman.html", Nora=amit)