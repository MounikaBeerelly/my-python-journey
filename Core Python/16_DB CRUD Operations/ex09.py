import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

# Drop table 
myCursor.execute("DROP TABLE myDept")

myCursor.execute("SHOW TABLES")

myTables = myCursor.fetchall()

print("\n", myTables)

"""
Output:
-------
[('mydept02',)]
"""