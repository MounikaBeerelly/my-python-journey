- `__name__` - 
   - `__name__` is a special built-in variable in Python that tells you how a Python file is being used.
   - Every Python module has a variable called `__name__`
   - Its value depends on how the module is executed.
   - Run this code only if this file is the starting point of the program.
- `f` - String Interpolation
- `r` - 
- `%s` -
- `%d` - 
- `.T` -
- `strip()` - Removes additional trailing spaces on right side

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
