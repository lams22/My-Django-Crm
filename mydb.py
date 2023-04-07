import mysql.connector

dataBase = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      passwd = 'lamarmelville',
	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE lamarm")

print("All Done!")
