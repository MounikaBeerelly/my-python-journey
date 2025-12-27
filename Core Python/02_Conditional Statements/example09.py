"""
Scenario:
--------
1. Finalize the grade of the student by the input marks achieved in the exam.
2. The grade table is
    a. Marks greater than OR equal to 90 "A"
    b. Marks greater than Or equal to 80 "B"
    c. Marks greater than or equal to 70 "C"
    d. Marks greater than OR equal to 60 "D"
    e. Marks less than 60 is "E"
    
Design the logic as a single liner control structure.
"""

#!python3

import os
os.system("cls")

inMarks = int(input("\nPlease enter the marks scored in the exam: "))
print("\nThe given marks for the grade test is: ", inMarks, end="\n")

gradeTest = "A" if inMarks >= 90 else "B" if inMarks >= 80 else "C" if inMarks >= 70 else "D" if inMarks >= 60 else "E"
print("\nThe grade allocated for the student is: ",gradeTest, "for marks", inMarks, end="\n")