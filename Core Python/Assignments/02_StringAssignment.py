"""
Ask the user how many daya until their birthday
and print an approx number of weeks until their birthday

week is = 7 days
decimal within the return is allowed..
"""

import os
os.system("cls")

days = int(input("How many days until your birthday? "))

weeks = days/7

print(f"Number of weeks until your birtday is : {round(weeks)}")


"""
Output:
=======
How many days until your birthday? 330
Number of weeks until your birtday is : 47
"""