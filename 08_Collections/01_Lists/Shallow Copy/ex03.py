#!python3

import os
os.system("cls")

listSports01 = ["Cricket", "Football", "Chess", "Shuttle"]

print("\nThe elements in the first list: ", list(listSports01), " and the allocated ID is : ", id(listSports01), end="\n")

listSports02 = listSports01

print("\nThe elements in the second list: ", list(listSports02), " and the allocated ID is : ", id(listSports02), end="\n")

listSports01[2] = "Hockey"

print("\nThe elements in the first list after updation : ", list(listSports01), " and the allocated ID is : ", id(listSports01), end="\n")
print("\nThe elements in the second list after updation : ", list(listSports02), " and the allocated ID is : ", id(listSports02), end="\n")

listSports02[3] = "Swimming"

print("\nThe elements in the second list after updation : ", list(listSports02), " and the allocated ID is : ", id(listSports02), end="\n")
print("\nThe elements in the first list after updation : ", list(listSports01), " and the allocated ID is : ", id(listSports01), end="\n")

"""
Output:
-------
The elements in the first list:  ['Cricket', 'Football', 'Chess', 'Shuttle']  and the allocated ID is :  2658465711296

The elements in the second list:  ['Cricket', 'Football', 'Chess', 'Shuttle']  and the allocated ID is :  2658465711296

The elements in the first list after updation :  ['Cricket', 'Football', 'Hockey', 'Shuttle']  and the allocated ID is :  2658465711296

The elements in the second list after updation :  ['Cricket', 'Football', 'Hockey', 'Shuttle']  and the allocated ID is :  2658465711296

The elements in the second list after updation :  ['Cricket', 'Football', 'Hockey', 'Swimming']  and the allocated ID is :  2658465711296

The elements in the first list after updation :  ['Cricket', 'Football', 'Hockey', 'Swimming']  and the allocated ID is :  2658465711296
"""