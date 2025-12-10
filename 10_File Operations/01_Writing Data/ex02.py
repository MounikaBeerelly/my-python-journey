#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//WriteData/ex02.txt", mode = "w", encoding = "cp1252")

    print("\nImplementing the File Write Operation", end="\n")
    print("\n------------oOo------------", end="\n")

    print("\nAccepting the data from the End user...", end="\n")

    writeData = input("\nPlease enter any text, and press enter key when finished : ")

    myFileHandle.write(writeData + "\n")
    print("\nWriting the data into the file is done successfully.. Closing the file handle..", end="\n")
except Exception as excepttionObject :
    print("Hey encountered Exception : %s"%(excepttionObject), end="\n")
finally :
    myFileHandle.close() 
    print("\nFile handle is closed successfully...", end="\n")


"""
Output:
------
Implementing the File Write Operation

------------oOo------------

Accepting the data from the End user...

Please enter any text, and press enter key when finished : Hello Python Learners ....

Writing the data into the file is done successfully.. Closing the file handle..

File handle is closed successfully...
"""