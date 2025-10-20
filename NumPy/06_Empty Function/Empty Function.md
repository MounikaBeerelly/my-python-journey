## Empty function:

### `np.empty()` function:

1. The function `np.empty()` is a part of the NumPy library  in python, and it is used to create an uninitialized array.
2. Uninitialized array means that the contents of the array are not set to any specific value by the developer
3. Uninitiallized array contain random or garbage values from memory

### Basic Syntax:
    `numpy.empty(shape, dtype=float, order='C)`

**Parameters**:

1. **Shape**: A tuple the specifies the dimensions of the array. 
    - For example: (2,3) would create a 2*3 array
2. **dtype (optional):** The desired data type for the array. 
    - By default, it is float
    - You can specify other types like int,bool etc
3. **order (optional):** It specifies the memory layout order. 
    - 'C' is for row-major (C-style) order, 
    - 'F' is for column-major (Fortan style) order. 
    - By default is 'C'
