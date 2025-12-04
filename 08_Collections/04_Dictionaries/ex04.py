#!python3

import os
os.system("cls")

employeeDictionary = {
        "firstName" : "John",
        "lastName" : "Roy",
        "age" : 32,
        "job" : "IT"
    }

loopState = True

while loopState :
    os.system("cls")
    print("\nThe original elements in the dictionary...", end="\n")
    searchKey = input("\nEnter the key to Search : ")
    if searchKey in employeeDictionary :
        print("\nThe value found is: ", employeeDictionary[searchKey], end="\n")
    else:
        print("Sorry!, The given key is not found...", end="\n")
        
    constinueState = input("\nDo you want to continue (Y OR N) :")
    if constinueState == 'N' or constinueState == 'n' :
        print("\nYou are requested for process termination..")
        loopState = False
"""
Output:
=======
The original elements in the dictionary...

Enter the key to Search : job

The value found is:  IT

Do you want to continue (Y OR N) :n

You are requested for process termination..
"""