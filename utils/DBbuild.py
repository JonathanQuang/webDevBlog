import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


#f="../data/blog.db"
#db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops


#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def createTABLE():
    f="data/blog.db"
    db=sqlite3.connect(f)
    c=db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT);"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS posts(name TEXT, post TEXT, postNum TEXT);"
    c.execute(command)
    db.commit()
    db.close()



def insertIntoUserTABLE(tablename, field1, field2):
    f="data/blog.db"
    db=sqlite3.connect(f)
    c=db.cursor()
    command = "INSERT INTO %s VALUES('%s', '%s');"%(tablename, field1, field2)
    c.execute(command)
    db.commit()
    db.close()

def insertIntoPostsTABLE(username, postText):
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	command = "SELECT postNum FROM posts WHERE name='" + username + "';"
	try:
		entryList = c.execute(command)
		newMaxID = 1
		for entry in entryList:
			newMaxID +=1
	except:
		newMaxID = 1
	command = "INSERT INTO posts VALUES('" + username + "','" + postText + "',"+ str(newMaxID) + ");"
	c.execute(command)
	db.commit()
	db.close()
	
def getPostsAndIDPairs(username):
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	command = "SELECT post, postNum FROM posts WHERE name='" + username + "';"
	try:
		pairs=[]
		for entries in c.execute(command):
			pairs.append(entries)
	except:
		pairs=([],[])
	return pairs[::-1]
	db.commit()
	db.close()
	
def getPostsFromIDandUser(id,username):
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	command = "SELECT post FROM posts WHERE name='" + username  + "' AND postNum='" + id + "';"
	return c.execute(command)[0]

def listUsers(tablename, withPassword, user):
    f="data/blog.db"
    db=sqlite3.connect(f)
    c=db.cursor()
    if (withPassword):
        command = "SELECT pass FROM %s WHERE name = '%s';"%(tablename, user)
    else:
        command = "SELECT name FROM %s;"%(tablename)
    c.execute(command)
    listNames = c.fetchall()
    db.commit()
    db.close()
    return listNames
#createTABLE()

def listUserEntries(username):
	f="data/blog.db"
	db=sqlite3.connect(f)
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
	db.close()
	return listEntries

def listAllUsers():
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	userList=[]
	for row in c.execute('SELECT name from users'):
		userList.append(row[0])
	return userList

def listPosts(username):
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	postList=[]
	for row in c.execute('SELECT post from posts WHERE name=\'' + username + "\'"): 
		postList.append(row[0]) 
	return postList[::-1]
	
def editPosts(username,oldEntry,newEntry):
	f="data/blog.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	command = "UPDATE posts SET post=" + newEntry + "WHERE name = " + newEntry + "AND post=" + oldEntry + ";"
	c.execute(command)
	db.commit
	db.close
#==========================================================
#db.commit() #save changes
#db.close()  #close database
