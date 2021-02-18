from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
	students = ["Amit","Ajay","Ankit","Anwar"]
	return render_template("try.html",ok=students)