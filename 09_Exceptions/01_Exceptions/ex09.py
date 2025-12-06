import os
os.system("cls")


try :
    finalSum = "Welcome " + 5
    print("\nThe final result is : ", finalSum, end="\n")
except TypeError as typeErrObj :
    print("\nHey! Type error is identified, some where incompatible types are forced, please check...", end="\n")
    print("\nThe Error state identified by the application is : ", typeErrObj, end="\n")
except BaseException as baseExcepObj :
    print("\nHey! Un known abnormality is identified, the final exception message is...", end="\n")
else :
    print("\nGiven operation is successfully executed", end="\n")
finally :
    print("\nResources De-Allocation section operating always finally when leaving the exception section", end="\n")
    
"""
Output:
-------
Hey! Type error is identified, some where incompatible types are forced, please check...

The Error state identified by the application is :  can only concatenate str (not "int") to str

Resources De-Allocation section operating always finally when leaving the exception section

"""