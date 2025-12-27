"""
Scenario:
---------
1. Design the operational logic for a banking transaction, associated with
    a. Cash deposit
    b. Cash withdraw
2. Design the logic with all the "common sence oriented business logical locations" as per the domain of banking.
3. Finally present the final balance and the messages that are essential ina  system of banking process.
"""

#!python3

import os
os.system("cls")

currentBalance = 25000.25
minBalance = 5000
print("\nPlease choose the transaction type to execute:")
print("\n------------OoO-------------")
print("\n1.Cash Deposit",end="\n")
print("\n2.Cash withdraw",end="\n")

transactionChoice = int(input("\nPlease enter your choice of the transaction type:"))

if(transactionChoice == 1):
    amountDeposit = float(input("\nPlease enter the amount for deposit: "))
    currentBalance += amountDeposit
    print("\n\nYour previous balance is %0.2f:"%(currentBalance-amountDeposit),"And the current balance is:%0.2f"%(currentBalance),end="\n")
else:
    amountWithdraw = float(input("\nPlease enter the amount for withdrawl:"))
    currentBalance -= amountWithdraw 
    if(currentBalance<minBalance):
        print("\nAlert! balance in the amount is below the minimum balance limit",end="\n")
    else:
        print("\n\nYour previous balance is %0.2f:"%(currentBalance+amountWithdraw),"And the current balance is:%0.2f"%(currentBalance),end="\n")