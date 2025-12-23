`__name__` - 
`f ` - String Interpolation
`%s` -
`%d` - 
`.T` -
`strip()` - Removes additional trailing spaces on right side

### DataBase Queries :
1. Import package - `import mysql.connector as mysql`
2. Connect database - `mysql.connect(host = "localhost", user = "root", passwd = "localhost", database = "db-name")`
3. Create database - `myCursor.execute("CREATE DATABASE myDB")`
4. Show databases - `myCursor.execute("SHOW DATABASES")`
5. Create Table - `myCursor.execute("CREATE TABLE myDept(DeptID integer, DeptName VARCHAR(30), DeptLoc VARCHAR(30))")`
6. Show tables - `myCursor.execute("SHOW TABLES")`
7. Fetch all the data - `myCursor.fetchall()`
8. Insert single record -
9. Insert multiple records -
