from flask import Flask, render_template,  request, session, redirect, url_for
import os

myapp = Flask(__name__)

myapp.secret_key = os.urandom(32)
login_dict = {}

@myapp.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title = "Login")

@myapp.route('/home/', methods = ['GET','POST'])
def welcome():
    if bool(session) != False:
        return render_template("home.html")
    user = request.form['username']
    print user
    password = request.form['inputPassword3']
    print password
    if request.form['up'] == "Sign Up":
        if (user in login_dict):
            return redirect(url_for('error'))
        login_dict[user] = password
        session['user'] = user
        session['pass'] = password
        return render_template('home.html')
    if request.form['in'] == "Log In":
        if not (user in login_dict):
            return redirect(url_for('error'))
        if password == login_dict[user]:
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
