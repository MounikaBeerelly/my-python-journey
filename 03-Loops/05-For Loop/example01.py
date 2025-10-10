#!python3

import os
import time
os.system("cls")

print("\nIllustration of \"FOR\" loop in python")
print("--------------------OoO-------------------")

for loopIndex in range(5):
    print("\nThis is the interation number: %d"%(loopIndex),end="\n")
    time.sleep(3)
    
#Out of the looping process working in the main program
print("\n\nout of the Iterative process working in the main application scope",end="\n")