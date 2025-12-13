#!python3

import os
os.system("cls")

class EmptyClass :
            pass
        
print("Displaying the structure of the class...", end="\n")
print(EmptyClass.__dict__, end="\n")

"""
Output:
======
Displaying the structure of the class...
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'EmptyClass' objects>, '__weakref__': <attribute '__weakref__' of 'EmptyClass' objects>, '__doc__': None}
"""