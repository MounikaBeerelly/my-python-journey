#!python3

"""
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59

Example:
if grade = 87 then print('B')
"""
import os
os.system("cls")

grade = int(input("\nEnter your grade : "))

if grade >= 90 and grade <= 100 :
    print("Your grade is : A")
elif grade >= 80 and grade <= 89 :
    print("Your grade is : B")
elif grade >= 70 and grade <= 79 :
    print("Your grade is : C")
elif grade >= 60 and grade <= 69 :
    print("Your grade is : D")
elif grade >= 0 and grade <= 59 :
    print("Your grade is : E")
else :
    print("Invalid grade.. Please enter valid one!")
    
"""
Output:
-------
Enter your grade : 87
Your grade is : B
"""