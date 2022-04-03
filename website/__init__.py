from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("inicio.html")	

	return app