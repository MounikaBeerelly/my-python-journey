#!python3

import os
os.system("cls")

employeeDictionary = {
        "firstName" : "John",
        "lastName" : "Roy",
        "age" : 32,
        "job" : "IT"
    }

print("\nPrinting the elements in the dictionary...", end="\n")
for dictionaryKey, dictionaryValue in employeeDictionary.items() :
    print("\nThe dictionary key is : ",dictionaryKey, " and corresponding value is : ", dictionaryValue, end="\n")
    
"""
Output:
=======
Printing the elements in the dictionary...

The dictionary key is :  firstName  and corresponding value is :  John

The dictionary key is :  lastName  and corresponding value is :  Roy

The dictionary key is :  age  and corresponding value is :  32

The dictionary key is :  job  and corresponding value is :  IT

"""