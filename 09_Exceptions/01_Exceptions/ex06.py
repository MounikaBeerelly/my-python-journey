import os
os.system("cls")

try :
    print("\nMy name is: ", myName, end="\n")
except NameError as nameErrorObj :
    print("\nOh! Some abnormality is identified in printing your name...", end="\n")
    print("\nResponse from Python Interpretor is:", nameErrorObj, end="\n")
except BaseException as baseExcepObj :
    print("\nFatal! Un-Identified exception is encountered, hence handled at the baseException level", end="\n")
    print("\nResponse from Python Interpretor is:", baseExcepObj, end="\n")
else :
    print("\nHurray! No runtime exception was encountered in this test cycle", end="\n")
    print("\nChange the tet case and Re-try to find another situation for exception", end="\n")
finally :
    print("\nCleaning the allocated resources.. please wait...", end="\n")
    
"""
Output:
-------
Oh! Some abnormality is identified in printing your name...

Response from Python Interpretor is: name 'myName' is not defined

Cleaning the allocated resources.. please wait...
"""