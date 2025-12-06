"""
Can we handle the Assertion Errors in Python?
Answer: Yes, using the "Traceback" module
"""

import os
os.system("cls")

import sys
import traceback

greetingMessage = "Welcome to the World of Python"

try:
    assert greetingMessage == 'Welcome to World of Python'
    assert 25 == 25
    assert 40 == 20
    assert True
except AssertionError as assertErrorObj :
    assertVar = sys.exc_info()
    traceback.print_tb(assertVar[2])
    traceBackInfo = traceback.extract_tb(assertVar[2])
    fileName, lineNumber, functionName, errorText = traceBackInfo[-1]
    
    print("Encountered some error in the line number {} in the statement: {}".format(lineNumber, errorText))
    exit(1)


"""
Output:
-------
  File "C:\Practice\my-python-journey\09_Exceptions\Traceback\ex01.py", line 15, in <module>
    assert greetingMessage == 'Welcome to the of Python'
Encountered some error in the line number 15 in the statement: assert greetingMessage == 'Welcome to the of Python'
"""