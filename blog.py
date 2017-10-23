from flask import Flask, render_template,  request, session, redirect, url_for
import os

myapp = Flask(__name__)

myapp.secret_key = os.urandom(32)


@myapp.route('/', methods = ['GET','POST'])
def root():
    return render_template('home.html')
if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
