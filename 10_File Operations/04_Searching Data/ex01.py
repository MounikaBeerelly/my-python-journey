#!python3

import os
os.system("cls")

try : 
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//AppendData/purchItems.dat", mode = "r", encoding = "cp1252")
    print("\nPrinting the items purchased", end="\n")
    print("\n------------oOo--------------")
    
    fileReadData = myFileHandle.readlines()
finally :
    myFileHandle.close()
    print("\nFile handle is closed successfully......", end="\n")
    
for itemIndex, purchaseItemName in enumerate(fileReadData, start = 1) :
    print("%d : %s" %(itemIndex, purchaseItemName), end="\n")

print("\nImplementing Data search operations...", end="\n")

searchItem = int(input("\nPlease enter the item ID to display.."))

currentItemNumber = 1
for itemIndex, purchaseItemName in enumerate(fileReadData, start = 1) :
    if(currentItemNumber == searchItem) :
        print("\n%d : %s"%(itemIndex, purchaseItemName), end= "\n")
        break
    currentItemNumber = currentItemNumber + 1
"""
Output:
------
Printing the items purchased

------------oOo--------------

File handle is closed successfully......
1 : Chocolates

2 : Buscuits

3 : Fruits

4 : Vegetables

5 : Groceries

6 : Electronics

7 : Diary Products.


Implementing Data search operations...

Please enter the item ID to display..3

3 : Fruits

"""