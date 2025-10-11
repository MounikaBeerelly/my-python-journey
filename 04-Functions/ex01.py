#!python3 
import os
os.system("cls")
    
import time

def executeTask():    
    print("\nWe are in the \"executeTask()\" module of the Python program")
    print("---------------------------------------------------------------",end="\n")
    time.sleep(2)
    
    print("\nHai! You are seeing this message as a sequential execution in the natural execution order of the program", end="\n")
    time.sleep(2)
    print("\nThis is another mesage in the natural execution order of the program",end="\n")
    time.sleep(2)

    print("\nNow leaving the \"executeTask()\" module of the Python program",end="\n")
    time.sleep(2)
    return

print("\nWe are in the Main block of the Python program")
time.sleep(2)
print("\nMain block instruction 01",end="\n")
time.sleep(2)
print("\nMain block instruction 02",end="\n")
time.sleep(2)
print("\nMain block instruction 03",end="\n")
time.sleep(2)
print("\nMain block instruction 04, Now ready to call \"executeTask()\" module of the python program",end="\n")
time.sleep(2)
executeTask() # calling a function 
# when a function is called, it immediately jumps to teh location of its definition (run-time memory)
print("\nWe are in the Main block of the Python program")
time.sleep(2)
print("\nMain block instruction 05",end="\n")
time.sleep(2)
print("\nMain block instruction 06",end="\n")
time.sleep(2)
print("\nMain block instruction 07",end="\n")
time.sleep(2)
print("\nMain block instruction 08, Now ready to terminate main block of operations",end="\n")
time.sleep(2)
"""
1. The above case we have defined a function by name "executeTask()"
2. All the operational instructions are encapsulated into the body  of the function (definition of the function)
3. Once the operational statements are "Encapsulated" this function is not abstracted for usage. Hence when the program is executed.

Note:
-----
1. Functions in design can exhibit their ability of operations only when they are called by the end user modules.
"""