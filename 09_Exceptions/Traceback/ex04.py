import os
import traceback

os.system("cls")

def executeDivision(inNumerator, inDenominator):
    try:
        quotientValue = inNumerator / inDenominator
        return quotientValue
    except ZeroDivisionError:
        # Ensure the directory exists
        log_dir = "C:/Practice/my-python-journey/09_Exceptions/Traceback"
        os.makedirs(log_dir, exist_ok=True)

        # Log the traceback
        with open(os.path.join(log_dir, "TraceBackLog.txt"), "w") as f:
            traceback.print_exc(file=f)

        return None

inNumerator = int(input("\nPlease enter the Numerator value : "))
inDenominator = int(input("\nPlease enter the Denominator value : "))

outResult = executeDivision(inNumerator, inDenominator)

if outResult is None:
    print("\nFatal error! Division by zero occurred..")
else:
    print("\nThe calculated quotient is : ", outResult)
