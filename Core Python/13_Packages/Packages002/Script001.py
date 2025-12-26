import os
os.system("cls")

from Greetings import WelcomeMessages, SendOffMessages

print("\nIllustration of the Packages", end="\n")
print("---------------oOo-------------", end="\n")

WelcomeMessages.welcomeFunc()
print("\nReturned from the Package, After completing the Welcome function responsibilities..", end="\n")

SendOffMessages.sendOffFunc()
print("\nReturned from the Package, After completing the Sendoff function responsibilities..", end="\n")
print("\nLeaving the program finally..", end="\n")

"""
Output:
-------
Illustration of the Packages
---------------oOo-------------

Hai! Welcome to the world of Python packages

Packages are modules that can be shared among different Python applications

Packages are external Python files containing Re-usable applications code

Returned from the Package, After completing the Welcome function responsibilities..

Hai! Thank you for being part of the world of Python packages

Packages makes your applications highly Re-Usable

Packages save time, economy and maintenance

Returned from the Package, After completing the Sendoff function responsibilities..

Leaving the program finally..

"""