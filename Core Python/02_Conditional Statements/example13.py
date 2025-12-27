"""
Scenario:
---------
1. Design a grading system for a examination assessment process considering the system to accept
    a. name of the student
    b. The total marks scored in the examination
      Sno   Begin Range  End Range   Grade Allocated
      ---   -----------  ---------   ---------------
      1        30         40            C
      2        40         60            B
      3        60         85            B+
      4        85        100            A
- All the begin ranges are exclusive and end ranges are inclusive
- Any given marks are not fitting in the range and below 30 marks are considered as "Failed class"
- The application should operate only when the given marks are within the range of 0 to 100.
"""

#!python3

import os
os.system("cls")

studentName = input("\nPlease enter your name:")
studentMarks = int(input("\nPlease enter the marks you scored:"))

"""
if(studentMarks>=0 and studentMarks<=100):
    if(studentMarks>85 and studentMarks<=100):
        print("\nCongratulations! %s"%(studentName),"You are awarded with grade \"A\"",end="\n")
    else:
        if(studentMarks>60 and studentMarks<=85):
            print("\n%s"%(studentName),"You are awarded with grade \"B+\"",end="\n")
        else:
            if(studentMarks>40 and studentMarks<=60):
                print("\n%s"%(studentName),"You are awarded with grade \"B\"",end="\n")
            else:
                if(studentMarks>30 and studentMarks<=40):
                    print("\n%s"%(studentName),"You are awarded with grade \"C\"",end="\n")
                else:
                    print("\nSorry! %s"%(studentName),"You have failed,need to attempt once again.",end="\n")
else:
    print("\nHey, improper input detected, Please try again once.",end="\n")
    """
if(studentMarks>=0 and studentMarks<=100):
    if(studentMarks>85 and studentMarks<=100):
        print("\nCongratulations! %s"%(studentName),"You are awarded with grade \"A\"",end="\n")
    elif(studentMarks>60 and studentMarks<=85):
        print("\n%s"%(studentName),"You are awarded with grade \"B+\"",end="\n")
    elif(studentMarks>40 and studentMarks<=60):
        print("\n%s"%(studentName),"You are awarded with grade \"B\"",end="\n")
    elif(studentMarks>30 and studentMarks<=40):
        print("\n%s"%(studentName),"You are awarded with grade \"C\"",end="\n")
    else:
        print("\nSorry! %s"%(studentName),"You have failed,need to attempt once again.",end="\n")
else:
    print("\nHey, improper input detected, Please try again once.",end="\n")