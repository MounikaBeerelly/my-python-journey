import mysql.connector as mysql
import os

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost"
)

print(db)


"""
Output:
-------
<mysql.connector.connection.MySQLConnection object at 0x00000116CC554F10>
"""