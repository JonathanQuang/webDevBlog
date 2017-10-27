from flask import Flask, render_template,  request, session, redirect, url_for
import os, sqlite3, csv
from utils import DBbuild
myapp = Flask(__name__)

myapp.secret_key = "vsecret"
db = sqlite3.connect("data/blog.db")
c = db.cursor() 
DBbuild.createTABLE(c)


@myapp.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title = "Login")

@myapp.route('/home/', methods = ['GET','POST'])
def home():
    if bool(session) != False:
        return render_template("home.html", USER = session['user'])
    user = request.form['username']
    print user
    password = request.form['inputPassword3']
    print password
    if request.form['up'] == "Sign up":
        if (user in login_dict):
            return redirect(url_for('error'))
        command = "INSERT INTO users VALUES (%s, %s);"%(user, password)
        c.execute(command)
        db.commit()
        session['user'] = user
        session['pass'] = password
        return render_template('home.html', USER = session['user'])
    if request.form['in'] == "Log In":
        if not (user in c.execute("SELECT name FROM users;")):
            return redirect(url_for('error'))
        if hash(password) == hash(c.execute("SELECT pass FROM users WHERE name = %s;"%(user))):
            return render_template('home.html')

@myapp.route('/error/', methods = ['GET','POST'])
def error():
    if bool(login_dict) == False:
        return render_template ('error.html')

@myapp.route('/logout/', methods= ['GET', 'POST'])
def logout():
    session.pop('user')
    session.pop('pass')
    return redirect(url_for('root'))
if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
