#!python3

import os
os.system("cls")

myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData//WriteData/ex01.dat", mode = "w", encoding = "cp1252")

print("\nAccepting the data from the End user...", end="\n")

writeData = input("\nPlease enter any text, and press enter key when finished : ")

myFileHandle.write(writeData + "\n")

myFileHandle.close() 