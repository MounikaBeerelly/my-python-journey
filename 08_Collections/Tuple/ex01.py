#!python3

import os
os.system("cls")

tupleSports = ("Cricket", "Shuttle", "FootBall")

print("\nDifferent sports registered in the tuple are: ", tupleSports, end="\n")
print("\nDifferent sports registered in the tuple are: ", tuple(tupleSports), end="\n")

#Indexing
print("\nIn Sports tuple Index 0 is: ", tupleSports[0], end="\n")
print("\nIn Sports tuple Index 1 is: ", tupleSports[1], end="\n")
print("\nIn Sports tuple Index 2 is: ", tupleSports[2], end="\n")

"""
Output:
-------
Different sports registered in the tuple are:  ('Cricket', 'Shuttle', 'FootBall')

Different sports registered in the tuple are:  ('Cricket', 'Shuttle', 'FootBall')

In Sports tuple Index 0 is:  Cricket

In Sports tuple Index 1 is:  Shuttle

In Sports tuple Index 2 is:  FootBall
"""
