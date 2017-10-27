import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


#f="../data/blog.db"
#db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops


#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def createTABLE(cursor):
	c=cursor
	command = "CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT);" 
	c.execute(command) 
	command = "CREATE TABLE IF NOT EXISTS postNum(name TEXT, postid INTEGER);" 
	c.execute(command) 
	command = "CREATE TABLE IF NOT EXISTS posts(postid INTEGER, post TEXT);" 
	c.execute(command) 



def insertintoTABLE(cursor,tablename, field1, field2):
	c=cursor 
	command = "INSERT INTO %s VALUES(%s, %s);"%(tablename, field1, field2) 
	c.execute(command)
    

#createTABLE()

#==========================================================
#db.commit() #save changes
#db.close()  #close database
