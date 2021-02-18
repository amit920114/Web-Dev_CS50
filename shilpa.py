from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def cry():
	return render_template("cry.html")
#yha pta nhi q function name or .html file name same
# hone p hi chl rhi h
#jabki aisa nhi hota {check application.py for more...}
@app.route("/guru")
def guru():
	return render_template("guru.html")