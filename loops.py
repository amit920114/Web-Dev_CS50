from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
	names = ["Amit","Alice","Anil"]
	return render_template("loops.html", names=names)