import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

selectStatement = "SELECT * FROM myDept02"

myCursor.execute(selectStatement)

fetchRecords = myCursor.fetchall()

for record in fetchRecords :
    print(record)

selectDeptName = "SELECT DeptName FROM myDept02"

myCursor.execute(selectDeptName)

fetchDeptNames = myCursor.fetchall()

for record in fetchDeptNames :
    print(record)
    
    
"""
Output:
-------
(3, 'ACCOUNTING', 'NEW YORK')
(4, 'RESEARCH', 'CHICAGO')
(5, 'SALES', 'BOSTON')
(6, 'OPERATIONS', 'DALLAS')
(7, 'RESEARCH', 'CHICAGO')
(8, 'SALES', 'BOSTON')
(9, 'OPERATIONS', 'DALLAS')
('ACCOUNTING',)
('RESEARCH',)
('SALES',)
('OPERATIONS',)
('RESEARCH',)
('SALES',)
('OPERATIONS',)
"""