import os
os.system("cls")

myTemperatures = [25, 19, 34, 23, 15, 61, 27, 41, 36, 29, 52, 68] # Average temperatures recorded month wise in a year

print("\nExtracting the even number temperatures from the temperature list...", end="\n")

# Using Normal function
def isEven(temperature) :
    return temperature % 2 == 0

evenTemperatureList = []

for temperature in myTemperatures :
    if(isEven(temperature)) :
        evenTemperatureList.append(temperature)
print("\n-----Using Normal Function-----")
print("\nThe recorded temperatures that are even number in the year are: ", evenTemperatureList, end="\n")

# Using Lamda and Filter functions
evenTemperatures = list(filter(lambda evenTemperature : (evenTemperature % 2 == 0), myTemperatures))
print("\n-----Using Lambda, Filter Function-----")
print("\nThe recorded temperatures that are even number in the year are: ", evenTemperatures, end="\n")

"""
Output:
-------
Extracting the even number temperatures from the temperature list...

-----Using Normal Function-----

The recorded temperatures that are even number in the year are:  [34, 36, 52, 68]

-----Using Lambda, Filter Function-----

The recorded temperatures that are even number in the year are:  [34, 36, 52, 68]

"""