from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chutiya():
	you = "i'm not a terrorist(bsdk) kurkure#@%^#"
	return render_template("anil.html", fuck=you)

if __name__ == "__main__": #this is the code for auto run 
	app.run(debug=True) #flask run in Background
