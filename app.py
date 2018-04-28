from flask import *
from data import *
from flask_pymongo import PyMongo
import bcrypt
from datetime import datetime
import pyrebase

config = {
    "apiKey": "AIzaSyBhGg8sI0G-GbEmbBJgzBUZHOKjLicVItE",
    "authDomain": "myflaskproject-1ab63.firebaseapp.com",
    "databaseURL": "https://myflaskproject-1ab63.firebaseio.com",
    "projectId": "myflaskproject-1ab63",
    "storageBucket": "myflaskproject-1ab63.appspot.com",
    "messagingSenderId": "418872657426",
    "serviceAccount":r"C:\Users\Admin\Downloads\myflaskproject-1ab63-firebase-adminsdk-p4445-22108b6773.json"
    }
firebase =pyrebase.initialize_app(config)
storage=firebase.storage()

y=storage.child("images\example.jpg").get_url("")
print(y)


app =Flask(__name__)

app.config['SECRET_KEY'] = 'redsfsfsfsfis'

app.config['MONGO_DBNAME']='web'

mongo=PyMongo(app)

Articles=Articles()


@app.route('/')
def index():
	if 'username' in session:
		return(render_template('home.html'))
	return(render_template('home.html'))

@app.route('/profile/<username>')
def profile(username):
	return(render_template('index.html',name=username))


@app.route('/articles')
def articles():
	return(render_template('articles.html', articles=Articles))

@app.route('/article/<id>/')
def article(id):
	return(render_template('article.html',id=id))


@app.route('/shopping')
def shopping():
	users=mongo.db.users
	food=users.find()
	asd = []
	for i in food:
		print (i)
		asd.append(i['name'])
	return(render_template('shopping.html',food=asd))

@app.route('/register')
def art():
	return(render_template("registe.html"))


@app.route('/registe',methods=['POST','GET'])
def got():
	if request.method=='POST':
		users=mongo.db.users
		existing_user=None

		if existing_user is None:
			hasspas=bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
			users.insert({'name':request.form['username'],'password':hasspas})
			session['username']=request.form['username']
			return(redirect(url_for('index')))
		
		return(" user already exist")

	return(render_template('registe.html'))

@app.route('/log')
def log():
	return(render_template('login.html'))


@app.route('/login',methods=['POST','GET'])
def login():
	users=mongo.db.users
	login_users= users.find_one({'name':request.form['username']})
	
	if login_users:
		#if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_users['password'].encode('utf-8')) == login_users['password'].encode('utf-8'):
		session['username'] = request.form['username']
		return(render_template('index1.html',naam=login_users['name'], image=y))

	return('Invalid usrname/password combination')

@app.route('/logout')
def logout():
	return render_template('home.html')

@app.route('/news')
def news():
	return("https://timesofindia.indiatimes.com/defaultinterstitial.cms")

if __name__=='__main__':
	app.config['SESSION_TYPE'] = 'mongodb'
	app.run(debug=True)