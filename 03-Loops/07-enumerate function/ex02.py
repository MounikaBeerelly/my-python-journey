#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"enumerate\" function in python")
print("--------------------OoO-------------------")

stepsToWithdrawFromATM = ["Insert the ATM card", "Enter the Pin number", "Select the transaction type", "Enter the amount", "Enter the OTP sent", "Wait for the cash collection message", "Collect the cash", "Collect your ATM card", "Take the receipt"]

enumeratingObject = enumerate(stepsToWithdrawFromATM, 1)

for extractedsteps in enumeratingObject:
    print(extractedsteps, end="\n")