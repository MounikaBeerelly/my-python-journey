#!python3

import os
os.system("cls")

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nThe given list of elements are: ", list(numberList), end="\n")

print("\nFiltering the even number elements from the given list using \"Lambda function\" Technique..", end="\n")

outEvenNumbers = list(filter(lambda outEven : outEven % 2 == 0, numberList)) 
print("\nThe identified even numbers are : ", list(outEvenNumbers), end="\n")

"""
Output:
-------
The given list of elements are:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

Filtering the even number elements from the given list using "Lambda function" Technique..

The identified even numbers are :  [2, 4, 6, 8]
"""