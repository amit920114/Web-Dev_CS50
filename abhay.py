from flask import Flask, render_template,request,session


app = Flask(__name__)

app.secret_key = "hello"


notes=[]

@app.route("/", methods=["GET","POST"])
def abhay():
	if request.method=="POST":
		note=request.form.get("note")
		notes.append(note)
	return render_template("abhay.html",notes=notes)