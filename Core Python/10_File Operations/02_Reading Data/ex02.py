#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//ReadData/ex02.txt", mode = "r", encoding = "cp1252")

    print("\nImplementing the File Read Operation", end="\n")
    print("\n------------oOo------------", end="\n")

    readData = myFileHandle.read()
    print("\nReading the data from the file is done successfully.. Closing the file handle..", end="\n")
except Exception as exceptionObject :
    print("Hey, encountered an Exception : %s"%(exceptionObject), end="\n")
finally :
    myFileHandle.close()
    print("\nFile handle is closed successfully...", end="\n")
    print("\nRe-directing the data to the end user interface, Please wait..", end="\n")
    print("\nThe data read from the file is : ", readData, end="\n")


"""
Output:
-------
Implementing the File Read Operation

------------oOo------------

Reading the data from the file is done successfully.. Closing the file handle..

File handle is closed successfully...

Re-directing the data to the end user interface, Please wait..

The data read from the file is :  Hello Python Learners ....
"""