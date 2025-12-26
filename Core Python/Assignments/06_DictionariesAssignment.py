#!python3

"""
Based on the dictionary:
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
"""
import os
os.system("cls")

myVehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x, y in myVehicle.items() :
    print(f"Keys and Values in the \"myVehicle\" are - {x}, {y} ")
    
vehicle2 = myVehicle.copy()

vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")

for i in vehicle2:
    print(f"Keys in the \"vehicle2\" are : {i}")

"""
Output:
-------
Keys and Values in the "myVehicle" are - model, Ford 
Keys and Values in the "myVehicle" are - make, Explorer 
Keys and Values in the "myVehicle" are - year, 2018 
Keys and Values in the "myVehicle" are - mileage, 40000 
Keys in the "vehicle2" are : model
Keys in the "vehicle2" are : make
Keys in the "vehicle2" are : year
Keys in the "vehicle2" are : number_of_tires
"""