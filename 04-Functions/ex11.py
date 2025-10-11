#!python3

"""
Scenario:
---------
Write a program to calculate the "Gross aggregate and percentage secured by the student for the given marks in
    1. Mathematics
    2. Science
    3. English
    4. Computers
The program should accept the "student name" and the corresponding marks at run-time from the end user.
"""

import os
os.system("cls")

def getStudentData():
    """Collecting the information for the students progress report card implementation"""
    studentName = input("\nEnter the name of the student:")
    marksinMaths = float(input("\nPlease enter the marks in Maths:"))
    marksinSceince = float(input("\nPlease enter the marks in Science:"))
    marksinEnglish = float(input("\nPlease enter the marks in English:"))
    marksinComputers = float(input("\nPlease enter the marks in computers:"))
    calculateGrossMarks(studentName,marksinMaths,marksinSceince,marksinEnglish,marksinComputers)
    return

def calculateGrossMarks(inStudentName,inMarksinMaths,inMarksinSceience,inMarksinEnglish,inMarksinComputers):
    """calculating the corresponding students gross marks that are acheived"""
    grossAggregate = inMarksinMaths + inMarksinSceience + inMarksinEnglish + inMarksinComputers
    calculatePercentage(inStudentName,grossAggregate)
    return

def calculatePercentage(inStudentName,grossAggregate):
    """Calculating the corresponding students percentage that are acheived"""
    percentageScored = (grossAggregate/400.00)*100
    print("\n",inStudentName,",Your total marks scored in the examination :",grossAggregate,end="\n")
    print("\nThe secured percentage is:", percentageScored,"%",end="\n")
    return

processExit = True

while processExit == True:
    """Module to simulate the students progress report card"""
    os.system("cls")
    
    getStudentData()
    
    inResponse = input("\nDo you want to enter the details of another student (Yes:Y, No:N):")
    if inResponse == 'N' or inResponse == 'n':
        processExit = False