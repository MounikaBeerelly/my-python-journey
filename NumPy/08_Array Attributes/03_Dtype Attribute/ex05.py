#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

myEmployee = np.array(
    [
        (1,"John",25.5), 
        (2, "Scott", 26.6), 
        (3, "Smith", 28.2)
    ], dtype = [
        ("EmpID", "int32"), 
        ("EmpName", "U10"), 
        ("EmpAge", "float32")
    ])

print(f"\nThe given Employee structure is..", end="\n")
print(myEmployee)

print(f"\nEmployee ID's : {myEmployee['EmpID']}", end="\n")
print(f"\nEmployee Names : {myEmployee['EmpName']}", end="\n")
print(f"\nEmployee Ages : {myEmployee['EmpAge']}", end="\n")
