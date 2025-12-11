#!python3

import os
os.system("cls")

with open("C://Practice//my-python-journey//10_File Operations//06_Random Files//DataSets/001_DataSet.dat", mode = "r", encoding = "cp1252") as myData :
    filePosition = myData.tell()
    print("\nJust now opened the file at position : ", filePosition, " Bytes", end="\n")
    
    outData = myData.read(5)
    print("\nThe first 5 Bytes read are : ", outData, end="\n")
    
    filePosition = myData.tell()
    print("\nThe File position after reading the data : ", filePosition, " Bytes", end="\n")
    
    myData.seek(6)
    
    outData = myData.read(5)
    print("\nThe first 5 Bytes read are : ", outData, end="\n")

    filePosition = myData.tell()
    print("\nThe File position after reading the data : ", filePosition, " Bytes", end="\n")
    
    
"""
Output:
------
Just now opened the file at position :  0  Bytes

The first 5 Bytes read are :  Hai!

The File position after reading the data :  5  Bytes

The first 5 Bytes read are :  ood M

The File position after reading the data :  11  Bytes

"""