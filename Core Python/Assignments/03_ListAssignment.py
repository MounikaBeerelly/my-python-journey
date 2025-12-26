#!python3

"""
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
"""

import os
os.system("cls")

zoo = ["Monkey", "Lion", "Tiger", "Giraffee", "Zebra"]

print(f"\nAnimals in the zoo are : {zoo}")

zoo.pop(3) # delete 3rd element

print(f"\nAnimals in the zoo after deleting 3rd index animal are : {zoo}")

zoo.append("Gorilla")

print(f"\nAnimals in the zoo after appending new animal are : {zoo}")

zoo.pop(0)

print(f"\nAnimals in the after deleting the first index animal are : {zoo}")

for index, animal in enumerate(zoo ,1) :
    print(f"\n{index} - {animal}")
    
print(f"\nFirst three animals are: {zoo[0:3]}")

"""
Output:
-------

Animals in the zoo are : ['Monkey', 'Lion', 'Tiger', 'Giraffee', 'Zebra']

Animals in the zoo after deleting 3rd index animal are : ['Monkey', 'Lion', 'Tiger', 'Zebra']

Animals in the zoo after appending new animal are : ['Monkey', 'Lion', 'Tiger', 'Zebra', 'Gorilla']

Animals in the after deleting the first index animal are : ['Lion', 'Tiger', 'Zebra', 'Gorilla']

1 - Lion

2 - Tiger

3 - Zebra

4 - Gorilla

First three animals are: ['Lion', 'Tiger', 'Zebra']

"""