from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def form():
	return render_template("form.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
	if request.method=="GET":
		return "Please Fill the Form First"
	else:
		name = request.form.get("name")#this name is from.html
		#inside the input command
		return render_template("hello.html", name=name)