#!python3

import os
os.system("cls")

# without Decorators
def addValue(param01, param02) :
    return param01 + param02

def subtractValue(param01, param02) :
    return param01 - param02

def functionCallLog(inFunctionName, param01, param02) :
    print(f"\nNow calling the function {inFunctionName.__name__} with arguments {param01}, {param02}", end="\n")
    return inFunctionName(param01, param02)

if __name__ == "__main__" :
    print("\n------- Without Decorators ---------------", end="\n")
    print("\nPlease chose the operation.. \n1.Addition\n2.Subtraction")
    inChoice = int(input("\nPlease enter your choice :"))
    
    value01 = int(input("\nPlease enter the first value : "))
    value02 = int(input("\nPlease enter the second value : "))

    if inChoice == 1 :
        print(f"\nThe final result is : {functionCallLog(addValue, value01, value02)}", end="\n")
    elif inChoice == 2 :
        print(f"\nThe final result is : {functionCallLog(subtractValue, value01, value02)}", end="\n")
    else :
        print("In-valid choice..", end="\n")
        
# with Decorators
def functionCallLog(inFunctionName) :
    def wrapperFunction(param01, param02) :
        print(f"\nNow calling the function {inFunctionName.__name__} with arguments {param01}, {param02}", end="\n")
        return inFunctionName(param01, param02)
    return wrapperFunction

@functionCallLog
def addValue(param01, param02) :
    return param01 + param02

@functionCallLog
def subtractValue(param01, param02) :
    return param01 - param02

if __name__ == "__main__" :
    print("\n------- Without Decorators ---------------", end="\n")
    print("\nPlease chose the operation.. \n1.Addition\n2.Subtraction")
    inChoice = int(input("\nPlease enter your choice :"))
    
    value01 = int(input("\nPlease enter the first value : "))
    value02 = int(input("\nPlease enter the second value : "))

    if inChoice == 1 :
        print(f"\nThe final result is : {addValue(value01, value02)}", end="\n")
    elif inChoice == 2 :
        print(f"\nThe final result is : {subtractValue(value01, value02)}", end="\n")
    else :
        print("In-valid choice..", end="\n")
  
"""
Output:
-------

------- Without Decorators ---------------

Please chose the operation..
1.Addition
2.Subtraction

Please enter your choice :1

Please enter the first value : 34

Please enter the second value : 12

Now calling the function addValue with arguments 34, 12

The final result is : 46

------- Without Decorators ---------------

Please chose the operation..
1.Addition
2.Subtraction

Please enter your choice :2

Please enter the first value : 54

Please enter the second value : 6

Now calling the function subtractValue with arguments 54, 6

The final result is : 48
"""