### What are Python Lists :
1. Python `List` is a sequence datatype structure, with self-indexing feature, used to store `Multiple Continuous Elements` in a single variable.
2. List is a Built-in datatype in Python which is used to store collections of data.
    1. List Sequence type is Managed in python using `list type class`.
    2. List sequence type will have its own constructor by name `list()`.
3. List object instance is created in Python in two ways :
    1. Using the notation of square brackets `[]`
    2. Using the `list()` constructor of the "list" class.
4. Python list can accomodate Heterogeneous OR Homogeneous data by requirement, hence a list can contain a mixed collection of
    1. Integers
    2. Floats
    3. Strings
    4. Objects
    5. Nested List
    7. Any other sequence type
5. List objects are `Mutable` by nature, hence Python Lists can be altered even after their creation.

#### Example:
```
    stationaryItems = ["Pencil", "Eracers", "Pens", "Papers", "Exam Pads"]

    print("\nThe calss type is : ", type(stationaryItems))

    print("\nThe Stationary items are: ", stationaryItems, end="\n")
    
    print("\nFirst Stationary item is: ", stationaryItems[0], end="\n")
```

### What are the different types of copy methods by System Design :
1. As per the System Design standards, we have two types of copy methods
    1. **Shallow Copy** :
        - Shallow copy is a process where `A new object of collection directly references the properties and behaviors of the existing collection object`.
        - In Shallow copy one object changes another reference object also changes
    2. **Deep Copy** :
        - 
