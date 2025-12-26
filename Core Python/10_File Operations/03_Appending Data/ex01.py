#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//AppendData/ex01.txt", mode = "a", encoding = "cp1252")

    print("\nImplementing the File Write Operation", end="\n")
    print("\n------------oOo------------", end="\n")

    print("\nAccepting the data from the End user...", end="\n")

    listItems = []
    
    loopState = True
    
    print("\nPlease Write the Rhyme.. To stop please enter Full stop...", end="\n")
    
    while loopState :
        rhymeList = input()
        listItems.append(rhymeList + "\n")
        terminatorChar = rhymeList[-1 :]
        
        if terminatorChar != "." :
            continue
        else :
            loopState = False
            
    myFileHandle.writelines(listItems)
except Exception as excepttionObject :
    print("Hey encountered Exception : %s"%(excepttionObject), end="\n")
finally :
    myFileHandle.close() 
    print("\nFile handle is closed successfully...", end="\n")


"""
Output:
------
Implementing the File Write Operation

------------oOo------------

Accepting the data from the End user...

Please Write the Rhyme.. To stop please enter Full stop...
Twinkle Twinkle little star
How I wonder what you are
Up above the world so high
.

File handle is closed successfully...
"""