import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

## myCursor.execute("CREATE TABLE myDept(DeptID integer, DeptName VARCHAR(30), DeptLoc VARCHAR(30))")

myCursor.execute("SHOW TABLES")

myTables = myCursor.fetchall()

for outTable in myTables :
    print(outTable)
    
"""
Output:
-------
('mydept',)
"""