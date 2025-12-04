"""
Scenario:
---------
Write a program to generate the following output: My name is: John Roy
"""

import os
os.system("cls")

try :
    print("\nMy name is: John Roy", end="\n")
except BaseException as baseExpObj:
    print("\nOh! Some abnormality is identified in printing your name...", end="\n")
    print("\nThe information revealed by the current Exception is...",baseExpObj, end="\n")
    
    
"""
Output:
-------
My name is: John Roy
"""