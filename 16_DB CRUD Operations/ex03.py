import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost"
)

# Show all the available databases
myCursor = db.cursor()

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
('sys',)
('world',)
"""