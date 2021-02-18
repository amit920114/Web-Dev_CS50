from flask import Flask, url_for, render_template 
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:// :114920@localhost:5432/Databases'

db = SQLAlchemy(app)


def main():
    Railway = db.execute("SELECT origin, destination, duration FROM Railway").fetchall()
    for railway in Railway:
        print(f"{Railway.origin} to {Railway.destination}, {Railway.duration}minutes.")

app.debug = True



@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()