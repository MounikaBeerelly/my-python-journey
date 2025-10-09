"""
Scenario:
---------
Design a program that can calculate the "Dearness Allowance: DA" and "House Rent Allowance: HRA" for a specific employee. Given employee name and basic salary of the employee at run time as
SNo  Basic Salary Range      Dearness Allowance        House Rent Allowance
---  -------------------     ------------------        --------------------
1    within 1000 and 10000   0.8 of the basic salary   0.2 of the basic salary
2    within 10001 and 20000  0.9 of the basic salary   0.25 of the basic salary
3    within 20001 and 30000  0.95 of the basic salary  0.3 of the basic salary
4    within 30001 and 40000  1.25 of the basic salary  1.05 of the basic salary
5    within 40001 and 50000  1.35 of the basic salary  1.25 of the basic salary
6    within 50000 and above  1.45 of the basic salary  1.35 of the basic salary

Any salary below 1000, is not considerable for DA and HRA
- All the lower range are inclusive and higher range are exclusive
- finally calculate the employee individual
    1. Total DA allocated
    2. Total HRA allocated
    3. The total gross salary and take home salary
"""

#!python3

import os
os.system("cls")

basicSalary = grossSalary = dearnessAllowance = houseRentAllowance = 0.0

empName = input("\nPlease enter the employee name:")
basicSalary = float(input("\nPlease enter the employee basic salary:"))

if(basicSalary>=999):
    if(basicSalary>=1000 and basicSalary<=9999):
        dearnessAllowance = basicSalary * 0.8
        houseRentAllowance = basicSalary * 0.2
    else:
        if(basicSalary>=10000 and basicSalary<=19999):
            dearnessAllowance = basicSalary * 0.9
            houseRentAllowance = basicSalary * 0.25
        else:
            if(basicSalary>=20000 and basicSalary<=29999):
                dearnessAllowance = basicSalary * 0.95
                houseRentAllowance = basicSalary * 0.3
            else:
                if(basicSalary>=30000 and basicSalary<=39999):
                    dearnessAllowance = basicSalary * 1.25
                    houseRentAllowance = basicSalary * 1.05
                else:
                    if(basicSalary>=40000 and basicSalary<=49999):
                        dearnessAllowance = basicSalary * 1.35
                        houseRentAllowance = basicSalary * 1.25
                    else:
                        if basicSalary >= 50000:
                            dearnessAllowance = basicSalary * 1.45
                            houseRentAllowance = basicSalary * 1.35
                        else:
                            print("\nValue not supported in this version, try again with another value..",end="\n")
    print("\nThe actual basic salary of %s"%(empName),"is: %0.2f"%(basicSalary),end="\n")
    print("\nThe Calculated DA is: %0.2f"%(dearnessAllowance),end="\n")
    print("\nThe calculated HRA is: %0.2f"%(houseRentAllowance),end="\n")
    
    grossSalary = basicSalary + dearnessAllowance + houseRentAllowance
    
    print("\nThe calculated Gross Salary (take home) of %s"%(empName),"is %0.2f"%(grossSalary),end="\n")
else:
    print("\nHey!",empName,"Sorry, You are not  eligible for DA and HRA",end="\n")
    print("\nYour final take home salary is:",basicSalary,end="\n")
    