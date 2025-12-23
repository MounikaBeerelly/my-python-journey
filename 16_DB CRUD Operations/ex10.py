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

valuesToInsert = ("ACCOUNTING", "NEW YORK")

myCursor.execute(insertStatement, valuesToInsert)

db.commit()

print(myCursor.rowcount, "Record Inserted Successfully..")

"""
Output:
-------
1 Record Inserted Successfully..
"""