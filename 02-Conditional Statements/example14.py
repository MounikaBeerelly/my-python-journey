"""
Scenario:
---------
Write a program to simulate the calculator operations for basic business calculations, accepting the required operator and operands at the run time
"""

#!python3

import os
os.system("cls")

print("\nPlease select the required Operation...\n\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n",end="\n")
operatorChoice = input("Select the required operation (1,2,3,4):")

operand1 = int(input("\nPlease enter the first number:"))
operand2 = int(input("\nPlease enter the second number:"))

if(operatorChoice == '1'):
    print("\n",operand1,"+",operand2,"=",(operand1 + operand2),end="\n")
else:
    if(operatorChoice == '2'):
        print("\n",operand1,"-",operand2,"=",(operand1 - operand2),end="\n")
    else:
        if(operatorChoice == '3'):
            print("\n",operand1,"*",operand2,"=",(operand1 * operand2),end="\n")
        else:
            if(operatorChoice == '4'):
                print("\n",operand1,"/",operand2,"=",(operand1 / operand2),end="\n")
            else:
                print("\nSorry! your operator is invalid..",end="\n")    
    
    