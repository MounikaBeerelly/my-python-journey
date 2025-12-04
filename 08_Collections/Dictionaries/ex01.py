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
print("\nThe type class identified is: ", type(employeeDictionary), end="\n")
print("\nThe allocated ID is: ", id(employeeDictionary), end="\n")

"""
Output:
=======
The elements in the dictionary :  {'firstName': 'John', 'lastName': 'Roy', 'age': 32, 'job': 'IT'}

The type class identified is:  <class 'dict'>

The allocated ID is:  2257260731776
"""