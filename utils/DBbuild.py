import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


def createTABLE():
    f="data/blog.db"            
    db=sqlite3.connect(f)              #connects to Datebase to allow editing
    c=db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT);"   #creates users table if it doesnt exist
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS posts(name TEXT, post TEXT, postNum TEXT);"  #creates posts table if it doesnt exist
    c.execute(command)
    db.commit()
    db.close()       #closes and commits changes



def insertIntoUserTABLE(tablename, field1, field2):
    f="data/blog.db"
    db=sqlite3.connect(f)         #connects to Datebase to allow editing
    c=db.cursor()
    command = "INSERT INTO %s VALUES('%s', '%s');"%(tablename, field1, field2)       #adds uder to User Table
    c.execute(command)
    db.commit()
    db.close()       #closes and commits changes

def insertIntoPostsTABLE(username, postText):        #places
	f="data/blog.db"
	db=sqlite3.connect(f)         #connects to Datebase to allow editing
	c=db.cursor()
	command = "SELECT postNum FROM posts WHERE name='" + username + "';"
	try:
		entryList = c.execute(command)           
		newMaxID = 1       #sets beginning ID
		for entry in entryList:
			newMaxID +=1     #adds 1 to every existing entry
	except:
		newMaxID = 1    #first post gets value of 1 
	command = "INSERT INTO posts VALUES('" + username + "','" + postText + "',"+ str(newMaxID) + ");"  #inserts new Post into table
	c.execute(command)
	db.commit()
	db.close()        #closes and commits changes
def replaceValueInPosts(username,postText, postID):
	f="data/blog.db"
	db=sqlite3.connect(f)        #connects to Datebase to allow editing
	c=db.cursor()
        command = "UPDATE posts SET post = '%s' WHERE postNum = "%(postText) + postID + ';' #Replaces the old post with the new post
        c.execute(command)
        db.commit()
	db.close()      #closes and commits changes

def getPostsAndIDPairs(username):
	f="data/blog.db"
	db=sqlite3.connect(f)         #connects to Datebase to allow editing
	c=db.cursor()
	command = "SELECT post, postNum FROM posts WHERE name='" + username + "';"        #selects post and its ID pair
	try:
		pairs=[]
		for entries in c.execute(command):    
			pairs.append(entries)      #pairs entries with their ids
	except:
		pairs=([],[])
	return pairs[::-1]       #reverses result for chronological order
	db.commit()
	db.close()       #closes and commits changes
	
def getPostsFromIDandUser(id,username):
	f="data/blog.db"
	db=sqlite3.connect(f)         #connects to Datebase to allow editing
	c=db.cursor()
	command = "SELECT post FROM posts WHERE name='" + username  + "' AND postNum='" + id + "';"     #gets post associated with user and ID
	for entry in c.execute(command):
		return entry
        db.commit()
        db.close()    #closes and commits changes

def listUsers(tablename, withPassword, user):
    f="data/blog.db"
    db=sqlite3.connect(f)           #connects to Datebase to allow editing
    c=db.cursor()
    if (withPassword):
        command = "SELECT pass FROM %s WHERE name = '%s';"%(tablename, user)    #used for password checking
    else:
        command = "SELECT name FROM %s;"%(tablename)       #returns all users from the table
    c.execute(command)
    listNames = c.fetchall()    #gets all data extracted and puts it in a list
    db.commit()
    db.close()        #closes and commits changes
    return listNames

def listUserEntries(username):
	f="data/blog.db"
	db=sqlite3.connect(f)     #connects to Datebase to allow editing
	c=db.cursor()
	postIdList=[]
	listEntries=[]
	command = "SELECT postid FROM postNUM WHERE name=" + username + ";"
	cList = c.excute(command)
	for entry in cList:
		postIdList.append(entry)
	for entry in postIDList:
		command = "SELECT post FROM posts WHERE postid=" + entry + ";"
		cList = c.execute(command)
		listEntries.append(cList[0][0]) #we know cList here only has one entry and we want remove that u'   '
	db.commit()
	db.close()        #closes and commits changes
	return listEntries

def listAllUsers():
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	userList=[]
	for row in c.execute('SELECT name from users'):
		userList.append(row[0])
        db.commit()
        db.close()          #closes and commits changes
	return userList

def listPosts(username):
	f="data/blog.db"
	db=sqlite3.connect(f)       #connects to Datebase to allow editing
	c=db.cursor()
	postList=[]
	for row in c.execute('SELECT post from posts WHERE name=\'' + username + "\'"):   #extracts data from table
		postList.append(row[0])
        db.commit() 
        db.close()           #closes and commits changes
	return postList[::-1]       #reverses list so it appears in chronological order
	 
