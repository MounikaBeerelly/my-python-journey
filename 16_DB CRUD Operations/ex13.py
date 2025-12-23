import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

selectStatement = "SELECT * FROM myDept02 WHERE DeptID = 6"
myCursor.execute(selectStatement)
fetchRecords = myCursor.fetchall()
print("\n", fetchRecords)

# Filtering data
selectDeptName = "SELECT * FROM myDept02 WHERE DeptName = %s"
deptNameFilter = ("SALES",)
myCursor.execute(selectDeptName, deptNameFilter)

fetchDeptNames = myCursor.fetchall()

for record in fetchDeptNames :
    print("Department Name \"SALES\" data", record)
    
    
"""
Output:
-------

 [(6, 'OPERATIONS', 'DALLAS')]
Department Name "SALES" data (5, 'SALES', 'BOSTON')
Department Name "SALES" data (8, 'SALES', 'BOSTON')
"""