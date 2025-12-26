#!python3

import os
os.system("cls")

with open("C://Practice//my-python-journey//10_File Operations//06_Random Files//DataSets/001_DataSet.dat", mode = "r", encoding = "cp1252") as myData :
    filePosition = myData.tell()
    print("\nJust now opened the file at position : ", filePosition, " Bytes", end="\n")
    
    outData = myData.read(6)
    
    print("\nthe first 6 Bytes read are : ", outData, end="\n")
    
    filePosition = myData.tell()
    print("\nThe File position after reading the data : ", filePosition, " Bytes", end="\n")
    
    
"""
Output:
------

Just now opened the file at position :  0  Bytes

the first 6 Bytes read are :  Hai! W

The File position after reading the data :  6  Bytes

"""