from flask import Flask, render_template,  request, session, redirect, url_for
from utils import DBbuild
import os, sqlite3, csv, hashlib

myapp = Flask(__name__)
myapp.secret_key="SuperSecretKeyThatIsTooLongToJustRandomlyHackInto"
DBbuild.createTABLE() #creates initial tables if they dont exist already


@myapp.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:     #logs user back in if their session is valid
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title = "Login") # directs to login page

@myapp.route('/home/', methods = ['GET','POST'])
def home():
    if bool(session) != False:       #logs user back in if their session is valid
        return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
    user = request.form['username']
    password = hashlib.md5(request.form['inputPassword3'].encode()).hexdigest() #hashes password with MD5 encryption
    if request.form['submit'] == "Sign up":              #checks if sign up button was pressed
        for entry in DBbuild.listUsers("users", False, ""):
            if (user == entry[0]):           #checks if username isn't already taken, if it is then redirects to error page
                return redirect(url_for('error'))
        DBbuild.insertIntoUserTABLE('users', user, password)        # adds new user to the table of Users
        session['user'] = user    #creates session for the user
        return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
    if request.form['submit'] == "Sign in":          #checks if sign in button was pressed
        for entry in DBbuild.listUsers("users", False, ""):
            if user == entry[0]:     #checks if the user is in the table of Users
                print DBbuild.listUsers("users", True, user)[0][0]
                if password == DBbuild.listUsers("users", True, user)[0][0]:      #checks for password match with attempted user login
                    session['user'] = user #starts session
                    return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
        return redirect(url_for('error'))

@myapp.route('/profile/', methods=['GET', 'POST'])
def profile():
	try:
		post = request.form['postText'] #pulls data from textbox from the CreatePost page if it exists
		DBbuild.insertIntoPostsTABLE(session['user'], post)   # adds a post
	except:
		print "postText error"
	try:
		ePost = request.form['editText'] #pulls data from textbox from the EditPost page if it exists
                numPost = request.form['submit']  #sets the number of the post
		DBbuild.replaceValueInPosts(session['user'], ePost,numPost ) #updates table with new post
	except:
		print "editText error"
	pairedList= DBbuild.getPostsAndIDPairs(session['user'])    #list of users that gets displayed on main page
	return render_template('profile.html', USER=session['user'], entryList=pairedList)  

@myapp.route('/otherBlog/', methods=['GET', 'POST'])
def otherBlog():
    return render_template('listUserEntries.html', USER=session['user'], otherUSER=request.form['uname'],entryList=DBbuild.listPosts(request.form['uname']))  #displays another user's blog pages

@myapp.route('/newpost/', methods = ['GET', 'POST'])
def newpost():
	return render_template('makePost.html', USER=session['user'])      #renders the page that allows you to create a post

@myapp.route('/editPost/',methods = ['GET', 'POST'])
def editpost():
	post = request.form['edit']                                       #returns postID of the post that will be edited
	text = DBbuild.getPostsFromIDandUser(post,session['user'])[0]          #returns post text from posts table matching the post id
	return render_template('editPost.html', ENTRY=text, POSTNUM = post)         #renders page that allows user to edit their post

@myapp.route('/error/', methods = ['GET', 'POST'])
def error():
    return render_template ('error.html')            #basic error page that leads back to home/login page

@myapp.route('/logout/', methods= ['GET', 'POST'])
def logout():
    session.pop('user')            #ends the session for the user
    return redirect(url_for('root'))      #redirects back to the login page

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()        #runs the app
