#!python3

"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""
import os
os.system("cls")

def userdictionary(firstName, lastName, age) :
    created_user_dictionary = {
        "firstName" : firstName,
        "lastName" : lastName,
        "age" : age
    }
    return created_user_dictionary

solution_dictionary = userdictionary(firstName = "Smith", lastName = "Roi", age = 32)
print(solution_dictionary)

"""
Output:
-------
{'firstName': 'Smith', 'lastName': 'Roi', 'age': 32}
"""