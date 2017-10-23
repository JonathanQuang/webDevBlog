from Flask import flask, render_template,  request, session, redirect, url_for
import os

myapp = Flask(__name__)

my_app.secret_key = os.urandom(32)


@my_app.route('/', methods = ['GET','POST'])
def root():
    return '<b>WORKING</b>'
