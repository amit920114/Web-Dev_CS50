from flask import Flask, render_template

app= Flask(__name__)
@app.route("/")
def index():
	name = ["Alice","Burbey","caterina","Zampa"]
	return render_template("try1.html",custom=name)