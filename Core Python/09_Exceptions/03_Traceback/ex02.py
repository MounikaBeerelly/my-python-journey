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
    assert greetingMessage == 'Welcome to the World of Python'
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
File "C:\Practice\my-python-journey\09_Exceptions\Traceback\ex02.py", line 17, in <module>
    assert 40 == 20
Encountered some error in the line number 17 in the statement: assert 40 == 20
"""