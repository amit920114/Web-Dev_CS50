from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:114920@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db.init_app(app)

@app.route("/")
def indexapp():
	railways = Railway.query.all()
	return render_template("indexapp.html",Railway=Railway )
@app.route("/book", methods=["POST"])
def book():

	name=request.form.get("name")
	try:
		railway_id = int(request.form.get("railway_id"))
	except ValueError:
		return render_template("error.html", message="Invali Railway no")
	#Make Sure The File Exists

	railway = RAilway.query.get(railway_id)
	if railway is None:
		return render_template("error.html", message="No such file")

	#Add Passengers

	passenger= Passenger(name=name, railway_id=railway_id)
	db.session.add(passenger)
	return render_template("sucess.html")
