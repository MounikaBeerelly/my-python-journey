import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost"
)

myCursor = db.cursor()

# Create database
myCursor.execute("CREATE DATABASE SkyEssDB01")

myCursor.execute("SHOW DATABASES")

myDataBases = myCursor.fetchall()

for outDBName in myDataBases :
    print(outDBName)


"""
Output:
-------
('information_schema',)
('mysql',)
('performance_schema',)
('sakila',)
('skyessdb01',)
('sys',)
('world',)
"""