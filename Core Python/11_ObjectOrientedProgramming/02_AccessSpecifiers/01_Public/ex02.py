#!python3

import os
os.system("cls")

class Sample :
    """Class to illustrate the public member scope"""
    # Public data members will go here
    sampleValue = 10
    
sampleObject01 = Sample()
print("\nThe sample object 01 value is : ", sampleObject01.sampleValue, end="\n")
    
sampleObject02 = Sample()
print("\nThe sample object 02 value is : ", sampleObject02.sampleValue, end="\n")

sampleObject01.sampleValue = 20
print("\nThe sample object value from \"sampleObject01\" is : ", sampleObject01.sampleValue, end="\n")
print("\nThe sample object value from \"sampleObject02\" is : ", sampleObject02.sampleValue, end="\n")

"""
Output:
------
The sample object 01 value is :  10

The sample object 02 value is :  10

The sample object value from "sampleObject01" is :  20

The sample object value from "sampleObject02" is :  10s
"""