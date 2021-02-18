from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("naina.html")

texts = ["My Name is Amit Kumar"
"My name is harsh khandelwal lawdis"
"My name is Shashi bakarchod"
]

@app.route("/first")
def first():
	return texts[0]

@app.route("/second")
def second():
	return texts[1]

@app.route("/third")
def third():
	return texts[2]