#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"enumerate\" function in python")
print("--------------------OoO-------------------")

stepsToWithdrawFromATM = ["Insert the ATM card", "Enter the Pin number", "Select the transaction type", "Enter the amount", "Enter the OTP sent", "Wait for the cash collection message", "Collect the cash", "Collect your ATM card", "Take the receipt"]

enumeratingObject = enumerate(stepsToWithdrawFromATM, 1)

print("\nYor ATM card is available in the envelop...", end="\n")
print("Congratulations for being the banking family..", end="\n")
print("Please follow the below steps to withdraw cash from the ATM nearest to you", end="\n")
print()

for stepIndex,stepDescription in enumeratingObject:
    print("%d. %s"%(stepIndex,stepDescription), end="\n")

print("\n Happy and safe banking to you and your family..", end="\n")