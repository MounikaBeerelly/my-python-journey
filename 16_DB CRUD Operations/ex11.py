import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "SkyEssDB01"
    )

myCursor = db.cursor()

insertStatement = "INSERT INTO myDept02(DeptName, DeptLoc) VALUES(%s, %s)"

valuesToInsert = [("RESEARCH", "CHICAGO"), ("SALES", "BOSTON"), ("OPERATIONS", "DALLAS")]

# myCursor.executemany(insertStatement, valuesToInsert)

#db.commit()

#print(myCursor.rowcount, "Record Inserted Successfully..")

myCursor.execute("SELECT * FROM myDept02")

myDept02Data = myCursor.fetchall()

for columns in myDept02Data :
    print(columns)
    
"""
Output:
-------
1 Record Inserted Successfully..
"""