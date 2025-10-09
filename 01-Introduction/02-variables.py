#!python3

import os
os.system("cls")

import sys

"""
int empName

Raises an error
---------------
File "C:\Python\variables.py", line 6
    int empName
        ^
SyntaxError: invalid syntax

Note: Don't declare the data type in python3

empAge

Raises an error
---------------
 File "C:\Python\variables.py", line 6, in <module>
    empName
NameError: name 'empAge' is not defined

empNo = None

Note:
-----
1. "None" is a built-in constant in python.
2. None is used to signify that a 
    - variable or expression has no value
    - It can also be used with function to represent that the "functions call does not returns any value"
 3. By common sence it is similar to NULL in other programming languages.
 """
 
empNo = 1234 #Here the variable is allocated a memory space with the initial value, having tits own "ID" and "memory address"

print("\nThe given employee number is :", empNo, end="\n")

"""
Notes:
------
- Every variable having 
    - A "variable name" given by the programmer
    - An ID allocated by the system
    - An address of storage allocated by the system
    - An initial value is assigned by the programmer
    - A "data type" allocated and associated by the interpreter, according to the value type assigned
    - an identified scope upon the usage of the variable.
- The programmer will references the "Name of the variable" throughout the program, and the interpreter references the "physical memmory address" for accessing the variable.
"""

empNo = 1234.56

print("\nThe given employee number is :", empNo, end="\n")

empNum = empSal = empDept = 0 #cascading declaration and initialization style

print("\nThe given Employee Number is :", empNum, end="\n")
print("\nThe given Employee Salary is :", empSal, end="\n")
print("\nThe given Employee Department is :", empDept, end="\n")

empDept = 10

print("\nThe given Employee Number is :", empNum, end="\n")
print("\nThe given Employee Salary is :", empSal, end="\n")
print("\nThe given Employee Department is :", empDept, end="\n")

charValue = 'M'
print("\nThe given string is: ",charValue,"\nThe Datatype identified is: ",type(charValue),"\nThe allocated Object ID is: ",id(charValue), end="\n")

charVal = 'Mounika'
print("\nThe given string is: ",charVal,"\nThe Datatype identified is: ",type(charVal),"\nThe allocated Object ID is: ",id(charVal), end="\n")

myVal = 29
print("\nThe given string is: ",myVal,"\nThe Datatype identified is: ",type(myVal),"\nThe allocated Object ID is: ",id(myVal), end="\n")

myVal = 29.18
print("\nThe given string is: ",myVal,"\nThe Datatype identified is: ",type(myVal),"\nThe allocated Object ID is: ",id(myVal), end="\n")

myVal = 29
print("\nThe given string is: ",myVal,"\nThe Datatype identified is: ",type(myVal),"\nThe allocated Object ID is: ",id(myVal), end="\n")

# different types

myName = 'A'
print("\nThe given string is: ",myName,"\nThe Datatype identified is: ",type(myName),"\nThe allocated Object ID is: ",id(myName), end="\n")

myName = 29
print("\nThe given string is: ",myName,"\nThe Datatype identified is: ",type(myName),"\nThe allocated Object ID is: ",id(myName), end="\n")

myName = 29.21
print("\nThe given string is: ",myName,"\nThe Datatype identified is: ",type(myName),"\nThe allocated Object ID is: ",id(myName), end="\n")

myName = 9.32j
print("\nThe given string is: ",myName,"\nThe Datatype identified is: ",type(myName),"\nThe allocated Object ID is: ",id(myName), end="\n")

myName = 'Avyay'
print("\nThe given string is: ",myName,"\nThe Datatype identified is: ",type(myName),"\nThe allocated Object ID is: ",id(myName), end="\n")

maximumInteger = sys.maxSize
minimumNumber = sys.maxSize - 1

print("\nThe minimum value of the integer managed on this system is: ", minimumNumber, end="\n")
print("\nThe maximum value of the integer managed on this system is: ", maximumNumber, end="\n")

integerInfo = sys.int_info

print("\nPrinting the information managed by integer type in Python...", end="\n\n")
print(integerInfo, end="\n")

maximumfloat = sys.float_info.max
minimumFloat = sys.float_info.min

print("\nMinimum float number in python", minimumFloat, end="\n")
print("\nMaximum float number in python", maximumfloat, end="\n")

# find size of the variable occupied in the memory -- sys.getsizeof(var)

myValue = 37

print("\nThe given integer is:", myValue, "\nThe size occupied in the memory is: ", sys.getsizeof(myValue), "Bytes.", end="\n")

# different types of values
charValue = 'A'
stringValue = 'Apple'
intValue = 30
longIntValue = 345678904567895678765
#longValue = 7649375L
floatValue = 35.45
bigFloatValue = 2345678976543234567.3456789765432
complexValue = 6.35j
print("\nthe given character id: ", charValue,"the datatype identified is:",type(charValue), end="\n")