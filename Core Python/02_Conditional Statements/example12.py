"""
Scenario:
---------
1. A sports complex admits children for cetain sports only by the fulfilled age, and provided by the date of birth certificate.
2. Currently there are vacancies for admission into "Swimming" and "Athletics"
3. To join in n either "Swimming OR Athletics OR both" The given child should be definitely more than 10 years of age
4. To join in swimming he should be more than 5 years of age, but not suitable for athletics
5. Any age below five years the child is not considered for outdoor games

Designt he logic considering the above facts to finalize the admission to the correct sport
"""

#!python3

import os
os.system("cls")

inAge = int(input("\nPlease enter your children age:"))

if (inAge>5):
    if (inAge>10):
        print("\nyour children is ready for training either Swimming OR Athletics OR both",end="\n")
    else:
        print("\nThe child is ready for training for Swimming but not suitable for Athletics",end="\n")
else:
    print("\nYour child is too young to be part of the outdoor games. Let him wait...",end="\n")