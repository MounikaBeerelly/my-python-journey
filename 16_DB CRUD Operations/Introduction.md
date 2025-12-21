### What is the Pre-Requisite to connect Python with a Database ?
1. Python as a languauge, should provide a database connectivity API, OR the database vendor should provide the API.
2. Python provides standard database connectivity interface called as `DB-API of Python`.
3. The `Python DB-API` can be connected to any database that adjers to the stsndard that is expected by Python.
4. To connect with `Python DB-API` we need the support of `ODBC (Operating DataBase Connecctivity)` from the Operating system.

### What we need if we want to connect to Databases using Python?
1. Download the `DB-API module` for each database that we need to connect, cross checking the proper version of the Python that is supported.
    - `https://wiki.python.org/moin/MySQL`
2. The DB-API will provide minimal standards for working with databases, by using Python structures.

### What steps we need to operate with DB-API ?
1. Import the API module
2. Setup OR aquire the Database connection
3. Issue OR execute the SQL statements and stored procedures if available
4. Close the connection once all the required operations on the database are done


### Setup Database using Python
1. Installing the required database in the machine.
2. Installing OR Configuring the database connector for Python

#### Installing MySQL 5.7.28 on the local machine :
1. https://downloads.mysql.com/archives/get/p/25/file/mysql-installer-community-5.7.28.0.msi
2. Double click the installer to begin the installation.