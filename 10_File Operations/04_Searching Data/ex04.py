#!python3

import os, fnmatch
os.system("cls")

extractedFiles = os.listdir("C://Practice//my-python-journey//10_File Operations//")

print("\nDisplaying the Names of the files", end="\n")
print("\n---------------oOo---------------")

for fileIndex, extractedFileName in enumerate(extractedFiles, start = 1) :
    print("\n%d : %s"%(fileIndex, extractedFileName), end="\n")

searchChoice = input("\nDo you want to search any files (Yes : Y OR No: N) : ")

if(searchChoice == "Y" or searchChoice == "y") :
    searchPattern = input("\nPlease enter the search pattern including wild cards if any : ")
    print("\nThe given pattern for searching the files is : ", searchPattern, end="\n")
    
for extractedName in extractedFiles :
    if fnmatch.fnmatchcase(extractedName, searchPattern) :
        print("\nFile Name : %s" %(extractedName), end = "\n")

"""
Output:
------

Displaying the Names of the files

---------------oOo---------------

1 : 01_Writing Data

2 : 02_Reading Data

3 : 03_Appending Data

4 : 04_Searching Data

5 : FileOperations.md

6 : OutData

Do you want to search any files (Yes : Y OR No: N) :y

Please enter the search pattern including wild cards if any : *Data

The given pattern for searching the files is :  *Data

File Name : 01_Writing Data

File Name : 02_Reading Data

File Name : 03_Appending Data

File Name : 04_Searching Data

File Name : OutData

"""