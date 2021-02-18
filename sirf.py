from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "hello"

@app.route("/", methods=["GET","POST"])
def sirf():
	if session.get("notes") is None:
		session["notes"]=[]
	if request.method=="POST":
		note=request.form.get("note")
		session["notes"].append(note)
	return render_template("sirf.html", notes=session["notes"])