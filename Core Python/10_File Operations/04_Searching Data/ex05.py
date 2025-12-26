#!python3

import os
os.system("cls")

try : 
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//AppendData/purchItems.dat", mode = "r", encoding = "cp1252")

    print("\nPrinting the items purchased", end="\n")
    print("\n------------oOo--------------")
    
    fileReadData = myFileHandle.readlines()

    for itemIndex, purchaseItemName in enumerate(fileReadData, start = 1) :
        print("%d : %s" %(itemIndex, purchaseItemName), end="\n")

    print("\nPrinting the file status information", end="\n")
    print("\nThe File name is : ", myFileHandle.name, end = "\n")
    print("\nThe File clsoed state is : ", myFileHandle.closed, end = "\n")
    print("\nThe file opening mode is: ", myFileHandle.mode, end="\n")
finally :
    myFileHandle.close()
    if (myFileHandle.closed) :
        print("\nFile handle is closed successfully......", end="\n")
        print("\nAll the resources are released..", end="\n")
    else :
        print("\nFatal Error! Encountered problem in closing the file", end="\n")
        print("\nResources De-allocation is failed.. Try once again", end="\n")

"""
Output:
------

Printing the items purchased

------------oOo--------------
1 : Chocolates

2 : Buscuits

3 : Fruits

4 : Vegetables

5 : Groceries

6 : Electronics

7 : Diary Products.


Printing the file status information

The File name is :  C://Practice//my-python-journey//10_File Operations//OutData//AppendData/purchItems.dat

The File clsoed state is :  False

The file opening mode is:  r

File handle is closed successfully......

All the resources are released..
"""