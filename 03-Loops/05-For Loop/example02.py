#!python3

import os
import time
os.system("cls")

print("\nIllustration of \"FOR\" loop in python")
print("--------------------OoO-------------------")

time.sleep(3)

loopcontrol = 1

loopTerminator = int(input("\nPlease enter the number of times to iterate:"))

print("\nInitializing the loop for execution..please wait..",end="\n")
time.sleep(3)

for loopIndex in range(loopcontrol,loopTerminator):
    print("\nThis is the interation number: %d"%(loopIndex),end="\n")
    time.sleep(3)
    
#Out of the looping process working in the main program
print("\n\nout of the Iterative process working in the main application scope",end="\n")