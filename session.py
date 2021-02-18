from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "session"

app.config["SESSION_PERMANENT"] =False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["GET","POST"])
def run():
	if session.get("notes") is None:
		session["notes"] = []
	if request.method=="POST":
		note=request.form.get("note")
		session["notes"].append(note)
	return render_template("run.html", notes=session["notes"])