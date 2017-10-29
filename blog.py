from flask import Flask, render_template,  request, session, redirect, url_for
import os, sqlite3, csv
from utils import DBbuild
myapp = Flask(__name__)

myapp.secret_key = os.urandom(32)
DBbuild.createTABLE()


@myapp.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title = "Login")

@myapp.route('/home/', methods = ['GET','POST'])
def home():
    if bool(session) != False:
        return render_template("listUsers.html", USER = session['user'])
    user = request.form['username']
    print user
    password = hash(request.form['inputPassword3'])
    print password
    if request.form['up'] == "Sign up":
        for entry in DBbuild.listUsers("users", False, ""):
            if (user == entry[0]):
                return redirect(url_for('error'))
        DBbuild.insertintoTABLE('users', user, password)
        session['user'] = user
        session['pass'] = password
        return render_template('listUsers.html', USER = session['user'])
    if request.form['in'] == "Log In":
        if not (user in DBbuild.listUsers("users", False, "")):
            return redirect(url_for('error'))
        if password == hash(listUsers("users", True, user)[0]):
            return render_template('listUsers.html', USER = session['user'])
       
@myapp.route('/error/', methods = ['GET','POST'])
def error():
 #   if bool(list) == False:
    return render_template ('error.html')

@myapp.route('/logout/', methods= ['GET', 'POST'])
def logout():
    session.pop('user')
    session.pop('pass')
    return redirect(url_for('root'))
if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
