from flask import Flask, render_template, url_for, request
from config import DevelopmentConfig
from app.models.user import db, User
from flask_bootstrap import Bootstrap
from validate_email import validate_email
from flask_wtf import CSRFProtect

import json
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

app = Flask(__name__, template_folder="app/templates/", static_folder="app/static")
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)



@app.route("/user/create", methods=["GET","POST"])
def user_create():
	title = "Create User"
	return render_template("view/user/create.html", title=title)

@app.route("/user/insert", methods=["POST"])
def user_insert():
	
	if request.method == "POST":

		username = request.form.get("username")
		email = request.form.get("email")
		password = request.form.get("password")

		if username is None or  username is '':
			response = {"res":0,"msg":"The username is not valid"}
			return json.dumps(response)

		
		if email is None or  email is '' or validate_email(email) == False:
			response = {"res":0,"msg":"The email is not valid"}
			return json.dumps(response)

		if password is None or  password is '':
			response = {"res":0,"msg":"The password is not valid"}
			return json.dumps(response)

		user = User(username = username, email = email, password = password)
		db.session.add(user)
		db.session.commit()

		response = {"res":1,"msg":"The user was created correctly"}
		return json.dumps(response)
	else:
		response = {"res":0,"msg":"has occurred a error, try it later"}
		return json.dumps(response)

@app.route("/user/index", methods=["GET","POST"])
@app.route("/user", methods=["GET","POST"])
def user_index():
	title = "Home User"
	return render_template("view/user/index.html", title=title)

@app.route("/user/user_list", methods=["GET","POST"])
def user_list():
	title = "Home User"
	data = User.query.limit(1).all()

	return json.dumps(data)



@app.route("/")
def index():
	pass

if __name__ == "__main__":
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(port = 8800)