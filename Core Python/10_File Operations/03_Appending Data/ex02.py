#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//AppendData/purchItems.dat", mode = "a", encoding = "cp1252")

    print("\nAccepting the data from the End user...", end="\n")

    listItems = [];
    
    loopState = True
    
    print("\nPlease enter the items you want to purchase..", end="\n\n")
    
    while loopState :
        purchaseItems = input()
        listItems.append(purchaseItems + "\n")
        terminatorChar = purchaseItems[-1 :]
        if terminatorChar != "." :
            continue
        else :
            loopState = False
            
    myFileHandle.writelines(listItems)
    print("\nSaved the items purchased in this sales order.. Closing the file handle...", end="\n")
except Exception as excepttionObject :
    print("Hey encountered Exception : %s"%(excepttionObject), end="\n")
finally :
    myFileHandle.close() 
    print("\nFile handle is closed successfully...", end="\n")

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
 

"""
Output:
------

Accepting the data from the End user...

Please enter the items you want to purchase..

Chocolates
Buscuits
Fruits
Vegetables
Groceries
Electronics
Diary Products.

Saved the items purchased in this sales order.. Closing the file handle...

File handle is closed successfully...

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
"""