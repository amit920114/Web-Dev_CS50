import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:114920@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def indexapp():
	Railway = db.execute("SELECT * FROM Railway").fetchall()
	return render_template("indexapp.html", Railway=Railway)
	
@app.route("/book", methods=["POST"])
def book():
	""" BOOK A Railway """
	#Get Form Information

	name = request.form.get("name")
	try:
		railway_id = int(request.form.get("railway_id"))
	except ValueError:
		return render_template("error.html", message="Invalid Railway Number.")
	#Make Sure the Railway Exists
	if db.execute("SELECT * FROM Railway WHERE id=:id",{"id": railway_id}).rowcount == 0:
		return render_template("error.html", message="No Such Railway with this id.")
		

	db.execute("INSERT INTO passenger (name, railway_id) VALUES (:name, :railway_id)",
		{"name": name, "railway_id": railway_id})


	db.commit()
	return render_template("sucess.html")

@app.route("/railways")
def railways():
	'''List All Railway'''
	railways=db.execute("SELECT * FROM Railway").fetchall()
	return render_template("railways.html", railways=railways)

@app.route("/railways/<int:railway_id>")
def railway(railway_id):
	'''List Details about Single Railway'''

	#Make Sure the Railway Exists
	railway=db.execute("SELECT * FROM Railway WHERE id=:id",
		{"id":railway_id}).fetchone()
	if railway is None:
		return render_template("error.html", message="No Such Railway")
	#Get All Passeger

	passengers=db.execute("SELECT name FROM passenger WHERE railway_id=:railway_id",
		{"railway_id":railway_id}).fetchall()
	return render_template("railway.html", railway=railway, passengers=passengers)
