"""
Scenario 02
===========
Write a program that takes from the end user till the end user terminates by typing "quit"
"""
#!python3

import os
import time
os.system("cls")

while True:
    quitStatus = input("\nPlease type \"quit\" to exit the process:")
    if quitStatus.lower() == "quit":
        break
    print("\nThe message entered by you is:", quitStatus,end="\n")