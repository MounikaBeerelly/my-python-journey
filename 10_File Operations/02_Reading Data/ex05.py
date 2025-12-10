#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//ReadData/ex03.md", mode = "r", encoding = "cp1252")

    print("\nImplementing the File Read Operation", end="\n")
    print("\n------------oOo------------", end="\n")

    readData = myFileHandle.readlines()
    print("\nReading the data from the file is done successfully.. Closing the file handle..", end="\n")
except Exception as exceptionObject :
    print("Hey, encountered an Exception : %s"%(exceptionObject), end="\n")
finally :
    myFileHandle.close()
    print("\nFile handle is closed successfully...", end="\n")
    print("\nThe data read from the file is : ", end="\n")
    recordCount = 0
    for lineIndex in readData :
        recordCount += 1
        print("Record number {} is : {}".format(recordCount, lineIndex))

"""
Output:
-------

Implementing the File Read Operation

------------oOo------------

Reading the data from the file is done successfully.. Closing the file handle..

File handle is closed successfully...

The data read from the file is :
Record number 1 is : This is Line Number - 01

Record number 2 is : This is Line Number - 02

Record number 3 is : This is Line Number - 03

Record number 4 is : This is Line Number - 04

"""