import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

myCursor.execute("CREATE TABLE myDept02(DeptID INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, DeptName VARCHAR(30), DeptLoc VARCHAR(30))")

myCursor.execute("SHOW TABLES")

myTables = myCursor.fetchall()

for outTable in myTables :
    print(outTable)
    
"""
Output:
-------
('mydept',)
('mydept02',)
"""