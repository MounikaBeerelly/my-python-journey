#!python3

import os
os.system("cls")

listSports01 = ["Cricket", "Football", "Chess", "Shuttle"]

print("\nThe elements in the first list: ", list(listSports01), " and the allocated ID is : ", id(listSports01), end="\n")

listSports02 = listSports01

print("\nThe elements in the second list: ", list(listSports02), " and the allocated ID is : ", id(listSports02), end="\n")
