#!python3

import os
os.system("cls")

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nThe given list of elements are: ", list(numberList), end="\n")

print("\nFiltering the even number elements from the given list using \"List Comprehension\" Technique..", end="\n")

outEvenNumbers = [outValue for outValue in numberList if outValue % 2 == 0 and outValue > 5]
print("\nThe identified even numbers greater than 5 are : ", list(outEvenNumbers), end="\n")

"""
Output:
-------
The given list of elements are:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

Filtering the even number elements from the given list using "List Comprehension" Technique..

The identified even numbers greater than 5 are :  [6, 8]

"""