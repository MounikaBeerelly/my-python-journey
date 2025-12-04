#!python3
 
import os
os.system("cls")

inValue = int(input("\nPlease give any integer value : "))

assert inValue > 0, "Given value is Negative, cannot continue operations"

print("\nHey! found a positive number", end="\n")

"""
Output:
------
--------Output 01 -------------
Please give any integer value : 2

Hey! found a positive number

------------Output 02 ------------
Please give any integer value : -3
Traceback (most recent call last):
  File "C:\Practice\my-python-journey\09_Exceptions\ex12.py", line 8, in <module>
    assert inValue > 0, "Given value is Negative, cannot continue operations"
AssertionError: Given value is Negative, cannot continue operations
"""