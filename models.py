from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Railway(db.Model):
	__tablename__ = "railway"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)

class Passenger (db.Model):
	__tablename__ = "passenger"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable=False)
	railway_id = db.Column(db.Integer, db.ForeignKey("railway.id"), nullable=False)
	