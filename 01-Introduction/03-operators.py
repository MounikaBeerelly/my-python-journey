#!python3

import os
os.system("cls")

print("\nApplying later type casting principle... ")

intValue01 = input("\nplease  enter the first number: ")

myintValue01 = int(intValue01)

intValue02 = input("\nplease  enter the second number: ")

myintValue02 = int(intValue02)

addition = myintValue01 + myintValue02
print("\nThe sum of", intValue01,"and", intValue02, "is: ", addition, end="\n")

sub = myintValue01 -  myintValue02
print("\nThe sub of", intValue01,"and", intValue02, "is: ", sub, end="\n")

mul = myintValue01 * myintValue02
print("\nThe mul of", intValue01,"and", intValue02, "is: ", mul, end="\n")

div = myintValue01 / myintValue02
print("\nThe div of", intValue01,"and", intValue02, "is: ", div, end="\n")

floorDiv = myintValue01 // myintValue02
print("\nThe floorDiv of", intValue01,"and", intValue02, "is: ", floorDiv, end="\n")

reminder = myintValue01 % myintValue02
print("\nThe reminder of", intValue01,"and", intValue02, "is: ", reminder, end="\n")

power = myintValue01 ** myintValue02
print("\nThe power of", intValue01,"and", intValue02, "is: ", power, end="\n")

#Compound Assignment Operator
addMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", addMyVal,end="\n")
addMyVal += 10
print("\nThe updated value is: ", addMyVal,end="\n")

subMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", subMyVal,end="\n")
subMyVal -= 10
print("\nThe updated value is: ", subMyVal,end="\n")

mulMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", mulMyVal,end="\n")
mulMyVal *= 10
print("\nThe updated value is: ", mulMyVal,end="\n")

divMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", divMyVal,end="\n")
divMyVal /= 10
print("\nThe updated value is: ", divMyVal,end="\n")

reminderMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", reminderMyVal,end="\n")
reminderMyVal %= 10
print("\nThe updated value is: ", reminderMyVal,end="\n")

exponentMyVal = int(input("\nplease enter the value here: "))
print("\nThe original value is:", exponentMyVal,end="\n")
exponentMyVal **= 10
print("\nThe updated value is: ", exponentMyVal,end="\n")

#Bitwise operators
binVal = 0
binVal = int(input("\nPlease enter any integer values: "))
print("\nThe given decimal value is:",binVal,"and the converted binary value is:", bin(binVal), end="\n")

print("\nThe converted binary value is: ",bin(binVal).replace("0b",""),end="\n")

print("\nThe converted binary value for 8 Bit architecture is: ",bin(binVal).replace("0b","").zfill(8),end="\n")
print("\nThe converted binaryvalue for 16 Bit architecture is: ",bin(binVal).replace("0b","").zfill(16),end="\n")
print("\nThe converted binary value for 32 Bit architecture is: ",bin(binVal).replace("0b","").zfill(32),end="\n")

#AND Operator
val1 = int(input("\nPlease enter the first decimal value: "))
val2 = int(input("\nPlease enter the second decimal value: "))
resultAND = val1 & val2
print("\nThe AND result of ",val1,"and",val2,"is: ",resultAND,end="\n")

resultOR = val1 | val2
print("\nThe OR result of ",val1,"and",val2,"is: ",resultOR,end="\n")

resultXOR = val1 ^ val2
print("\nThe XOR result of ",val1,"and",val2,"is: ",resultXOR,end="\n")