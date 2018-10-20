from flask import Flask, render_template, session, redirect,url_for

from flask_wtf import Form
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
class Test(db.Model):
	id = db.Column(db.Integer, primary_key=True)

class StudentInputForm(Form):
	secondName = StringField('Прізвище', validators=[DataRequired()] )
	firstName = StringField('Ім\'я', validators=[DataRequired()])
	midName = StringField('По батькові', validators=[DataRequired()])
	rate = FloatField('Бал', validators=[DataRequired()])
	submit = SubmitField('Submit')

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(30),unique = False)
	midName = db.Column(db.String(30), unique = False)
	lastName =  db.Column(db.String(30), unique = False)
	rate =  db.Column(db.Integer, unique=False)

	def __repr__(self):
		return '<Прізвище %r>' % self.lastName

class Students(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(30),unique = False)
	midName = db.Column(db.String(30), unique = False)
	lastName =  db.Column(db.String(30), unique = False)
	rate =  db.Column(db.Integer, unique=False)

	def __repr__(self):
		return '<Прізвище %r>' % self.lastName



@app.route('/', methods=['GET', 'POST'])
def index():
	firstName=None
	midName=None
	secondName=None
	rate=None
	form = StudentInputForm()
	known=True
	if form.validate_on_submit():
		secondName=form.secondName.data
		firstName=form.firstName.data
		midName=form.midName.data
		rate=form.rate.data
		student = Students.query.filter_by(lastName=form.secondName.data)
		
		if student is None:
			student=Students(lastName=secondName,firstName=firstName,midName=midName,rate=rate)
			db.session.add(student)
			db.session.commit()
			known=False
		

		form.secondName.data=''
		form.firstName.data=''
		form.midName.data=''
		form.rate.data=None
	return render_template('index.html',form=form, 
		known=known)

	
@app.route('/table/', methods=['GET', 'POST'])
def table():
    return render_template('table.html')
    

if __name__ == '__main__':
	app.run()
