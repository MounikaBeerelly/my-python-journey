#!python3

import os
os.system("cls")

class Sample :
    """Class to illustrate the public member scope"""
    # Public data members will go here
    sampleValue = 10
    
sampleObject01 = Sample()
print("\nThe sample object value is : ", sampleObject01.sampleValue, end="\n")
    
sampleObject02 = Sample()
print("\nThe sample object value is : ", sampleObject02.sampleValue, end="\n")

"""
Output:
------
The sample object value is :  10

The sample object value is :  10
"""