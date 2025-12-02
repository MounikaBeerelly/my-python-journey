#!python3

import os
os.system("cls")

from functools import partial

def formatMessage(inGreeting, inPersonName, inPunctuation) :
    return f"{inGreeting}, {inPersonName}{inPunctuation}"

greetingValue = input("\nPlease give the greeting Phrase: ")
greetingFormat01 = partial(formatMessage, greetingValue)
inPersonName = input("\nPlease give your name to be displayed: ")
greetingPunctuation = input("\nPlease give the punctuation character: ")
print(f"\nHey, {greetingFormat01(inPersonName, greetingPunctuation)}, Your registration is done successfully", end="\n")

greetingValue = input("\nPlease give the greeting Phrase: ")
greetingFormat02 = partial(formatMessage, greetingValue)
inPersonName = input("\nPlease give your name to be displayed: ")
greetingPunctuation = input("\nPlease give the punctuation character: ")
print(f"\nHey, {greetingFormat02(inPersonName, greetingPunctuation)}, Your registration is done successfully", end="\n")
    
"""
Output:
-------

Please give the greeting Phrase: Hello

Please give your name to be displayed: John

Please give the punctuation character: !

Hey, Hello, John!, Your registration is done successfully

Please give the greeting Phrase: Hai

Please give your name to be displayed: Joy

Please give the punctuation character: @

Hey, Hai, Joy@, Your registration is done successfully
"""