#!python3

import os
os.system("cls")

print("\nIllustration of the Bitwise \"Left shift: <<\" operator in Python", end="\n")
print("---------------------------------OoO-----------------------------",end="\n")

inValue = 0
displacementValue = 0
finalValue = 0

#Left shift operator
inValue = int(input("\nPlease enter the required decimal value: "))

displacementValue = int(input("\nPlease enter the required displacement value: "))

finalValue = inValue << displacementValue
print("\nThe value", inValue,"then shifted by a displacement of",displacementValue,"Bit(s) is equal to:",finalValue, end="\n")

#Right shift operator
inValue02 = int(input("\nPlease enter the required decimal value: "))

displacementValue02 = int(input("\nPlease enter the required displacement value: "))

finalValue02 = inValue02 >> displacementValue02
print("\nThe value", inValue02,"then shifted by a displacement of",displacementValue02,"Bit(s) is equal to:",finalValue02, end="\n")
