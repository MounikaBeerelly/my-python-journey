#!python3

import os
os.system("cls")

employeeDictionary = {
        "firstName" : "John",
        "lastName" : "Roy",
        "age" : 32,
        "job" : "IT"
    }

print("\nThe elements in the dictionary : ", employeeDictionary, end="\n")
print("T\nThe firstName of the Employee : ", employeeDictionary["firstName"], end="\n")
print("T\nThe lastName of the Employee : ", employeeDictionary["lastName"], end="\n")
print("T\nThe age of the Employee : ", employeeDictionary["age"], end="\n")
print("T\nThe job of the Employee : ", employeeDictionary["job"], end="\n")

print("\nPrinting the elements in the dictionary...", end="\n")
for dictionaryValue in employeeDictionary.values() :
    print("\nThe extracted values are: ", dictionaryValue, end="\n")
    
"""
Output:
=======
The elements in the dictionary :  {'firstName': 'John', 'lastName': 'Roy', 'age': 32, 'job': 'IT'}
T
The firstName of the Employee :  John
T
The lastName of the Employee :  Roy
T
The age of the Employee :  32
T
The job of the Employee :  IT

Printing the elements in the dictionary...

The extracted values are:  John

The extracted values are:  Roy

The extracted values are:  32

The extracted values are:  IT
"""