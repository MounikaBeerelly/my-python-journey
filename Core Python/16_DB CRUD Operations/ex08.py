import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

# myCursor.execute("CREATE TABLE myDept02(DeptID INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, DeptName VARCHAR(30), DeptLoc VARCHAR(30))")

myCursor.execute("DESCRIBE myDept02")

myDept02Describe = myCursor.fetchall()

for columns in myDept02Describe :
    print(columns)
    
"""
Output:
-------
('DeptID', 'int', 'NO', 'PRI', None, 'auto_increment')
('DeptName', 'varchar(30)', 'YES', '', None, '')
('DeptLoc', 'varchar(30)', 'YES', '', None, '')
"""