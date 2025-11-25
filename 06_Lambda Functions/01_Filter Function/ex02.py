import os
os.system("cls")

myTemperatures = [25, 19, 34, 23, 15, 61, 27, 41, 36, 29, 52, 68] # Average temperatures recorded month wise in a year

print("\nExtracting the even number temperatures from the temperature list...", end="\n")

oddTemperatures = list(filter(lambda oddTemperature : (oddTemperature % 2 != 0), myTemperatures))
print("\nThe recorded temperatures that are odd number in the year are: ", oddTemperatures, end="\n")

temperaturesGT25 = list(filter(lambda temperature : (temperature > 25), myTemperatures))
print("\nThe recorded temperatures that are greater than 25 degrees farenheit are: ", temperaturesGT25, end="\n")

tempLevel = int(input("\nPlease give the threshold value of the temperature to filter: "))
filterTemperature = list(filter(lambda temperature : (temperature < tempLevel), myTemperatures))
print(f"\nThe recorded temperatures that are less than {tempLevel} degrees farenheit are: ", filterTemperature, end="\n")

temperatureBT20and35 = list(filter(lambda temperature : ((temperature > 20) and (temperature < 35)), myTemperatures))
print(f"\nThe recorded temperatures that are between 20 and 35 degrees farenheit are: ", temperatureBT20and35, end="\n")

"""
Output:
-------
Extracting the even number temperatures from the temperature list...

The recorded temperatures that are odd number in the year are:  [25, 19, 23, 15, 61, 27, 41, 29]

The recorded temperatures that are greater than 25 degrees farenheit are:  [34, 61, 27, 41, 36, 29, 52, 68]

Please give the threshold value of the temperature to filter: 20

The recorded temperatures that are less than 20 degrees farenheit are:  [19, 15]

The recorded temperatures that are between 20 and 35 degrees farenheit are:  [25, 34, 23, 27, 29]
"""