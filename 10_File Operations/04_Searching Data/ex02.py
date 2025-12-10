#!python3

import os
os.system("cls")

extractedFiles = os.listdir("C://Practice//my-python-journey//10_File Operations//")

print("\nDisplaying the Names of the files", end="\n")
print("\n---------------oOo---------------")

for fileIndex, extractedFileName in enumerate(extractedFiles, start = 1) :
    print("\n%d : %s"%(fileIndex, extractedFileName), end="\n")
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

"""