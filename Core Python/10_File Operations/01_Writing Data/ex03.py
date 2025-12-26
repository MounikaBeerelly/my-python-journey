#!python3

import os
os.system("cls")

try :
    myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//WriteData/ex03.md", mode = "w", encoding = "cp1252")

    print("\nImplementing the File Write Operation", end="\n")
    print("\n------------oOo------------", end="\n")

    print("\nAccepting the data from the End user...", end="\n")

    loopState = True
    
    while loopState :
        writeData = input("\nPlease enter any text, and press enter key when finished : ")
        myFileHandle.write(writeData + "\n")
        continueState = input("\nDo you want to add another record (Y OR N) :")
        if continueState == 'N' or continueState == 'n' :
            print("\nYou requested for process Termination...Thank You", end="\n")
            loopState = False
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

Please enter any text, and press enter key when finished : This is Line Number - 01

Do you want to add another record (Y OR N) :y

Please enter any text, and press enter key when finished : This is Line Number - 02

Do you want to add another record (Y OR N) :Y

Please enter any text, and press enter key when finished : This is Line Number - 03

Do you want to add another record (Y OR N) :y

Please enter any text, and press enter key when finished : This is Line Number - 04

Do you want to add another record (Y OR N) :n

You requested for process Termination...Thank You

File handle is closed successfully...

"""