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
    command = "CREATE TABLE IF NOT EXISTS postNum(name TEXT, postid INTEGER);" 
    c.execute(command) 
    command = "CREATE TABLE IF NOT EXISTS posts(postid INTEGER, post TEXT);" 
    c.execute(command)
    db.commit()
    db.close()



def insertintoTABLE(tablename, field1, field2):
    f="data/blog.db"
    db=sqlite3.connect(f)
    c=db.cursor()
    command = "INSERT INTO %s VALUES('%s', '%s');"%(tablename, field1, field2)
    c.execute(command)
    db.commit()
    db.close()  

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

#==========================================================
#db.commit() #save changes
#db.close()  #close database
