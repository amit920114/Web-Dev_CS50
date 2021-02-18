from flask import Fkask, render_template

app = flask(__name__)
@app.route("/")
def index():
	return render_template("much.html")

@app.route("/more")
def more():
	return render_template("more.html")