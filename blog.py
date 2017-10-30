from flask import Flask, render_template,  request, session, redirect, url_for
import os, sqlite3, csv, hashlib
from utils import DBbuild
myapp = Flask(__name__)

#myapp.secret_key = os.urandom(32)
myapp.secret_key="testing123"
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
        return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
    user = request.form['username']
    print user
    password = hashlib.md5(request.form['inputPassword3'].encode()).hexdigest()
    print password
    if request.form['submit'] == "Sign up":
        for entry in DBbuild.listUsers("users", False, ""):
            if (user == entry[0]):
                return redirect(url_for('error'))
        DBbuild.insertIntoUserTABLE('users', user, password)
        session['user'] = user
        return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
    if request.form['submit'] == "Sign in":
        for entry in DBbuild.listUsers("users", False, ""):
            if user == entry[0]:
                print DBbuild.listUsers("users", True, user)[0][0]
                if password == DBbuild.listUsers("users", True, user)[0][0]:
                    session['user'] = user
                    print DBbuild.listAllUsers()
                    return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
        return redirect(url_for('error'))

@myapp.route('/profile/', methods=['GET', 'POST'])
def profile():
	try:
		print 1
		post = request.form['postText']
		print 2
		DBbuild.insertIntoPostsTABLE(session['user'], post)
		print 3
	except:
		print "postText error"
	try:
		print 4
		ePost = request.form['editText']
		print 5
		#DBbuild.insertintoTABLE('posts', session['user'], ePost)
		print 6
	except:
		print "editText error"
	pairedList=DBbuild.getPostsAndIDPairs(session['user'])
	return render_template('profile.html', USER=session['user'], entryList=pairedList)

@myapp.route('/otherBlog/', methods=['GET', 'POST'])
def otherBlog():
    return render_template('listUserEntries.html', USER=session['user'], otherUSER=request.form['uname'],entryList=DBbuild.listPosts(request.form['uname']))

@myapp.route('/newpost/', methods = ['GET', 'POST'])
def newpost():
	return render_template('makePost.html', USER=session['user'])

@myapp.route('/editPost/',methods = ['GET', 'POST'])
def editpost():
	post = request.form['edit']
	text = DBbuild.getPostsFromIDandUser(post,session['user'])[0]
	return render_template('editPost.html', ENTRY=text)

@myapp.route('/error/', methods = ['GET', 'POST'])
def error():
 #   if bool(list) == False:
    return render_template ('error.html')

@myapp.route('/logout/', methods= ['GET', 'POST'])
def logout():
    session.pop('user')
    return redirect(url_for('root'))

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
