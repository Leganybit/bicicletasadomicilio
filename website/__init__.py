from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("base.html")
	@app.route("/galeria")
	def galeria():
		return render_template("galeria.html")	

	return app