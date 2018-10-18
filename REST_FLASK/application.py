from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Test(db.Model):
	id = db.Column(db.Integer, primary_key=True)

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(30),unique = False)
	midName = db.Column(db.String(30), unique = False)
	lastName =  db.Column(db.String(30), unique = False)
	rate =  db.Column(db.Integer, unique=False)

	def __repr__(self):
		return '<Прізвище %r>' % self.lastName


if __name__ == '__main__':
	app.run()
