import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

# Delete Record
deleteStatement = "DELETE FROM MyDept02 WHERE DeptID = 8"
myCursor.execute(deleteStatement)

# Update Record
updateStatement = "UPDATE myDept02 SET DeptName = 'TELECOM' WHERE DeptID = 7"
myCursor.execute(updateStatement)

db.commit()

# Show records
selectStatement = "SELECT * FROM myDept02"
myCursor.execute(selectStatement)
fetchRecords = myCursor.fetchall()
for record in fetchRecords :
    print(record)

    
"""
Output:
-------
(3, 'ACCOUNTING', 'NEW YORK')
(4, 'RESEARCH', 'CHICAGO')
(5, 'SALES', 'BOSTON')
(6, 'OPERATIONS', 'DALLAS')
(7, 'TELECOM', 'CHICAGO')
"""