import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

selectStatement = "SELECT * FROM myDept02 ORDER BY DeptID DESC"
myCursor.execute(selectStatement)
fetchRecords = myCursor.fetchall()
for record in fetchRecords :
    print(record)

    
"""
Output:
-------
(9, 'OPERATIONS', 'DALLAS')
(8, 'SALES', 'BOSTON')
(7, 'RESEARCH', 'CHICAGO')
(6, 'OPERATIONS', 'DALLAS')
(5, 'SALES', 'BOSTON')
(4, 'RESEARCH', 'CHICAGO')
(3, 'ACCOUNTING', 'NEW YORK')
"""