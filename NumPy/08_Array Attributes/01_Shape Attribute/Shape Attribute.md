## Understanding `ndarray.shape` attribute:

- The shape attribute of a NumPy array returns the dimensions of the array as a tuple.
- Each elemnt in the tuple represents the size of the array along that dimension
- `ndarray.shape` is used to 
    - get or modify the dimensiona of the array
    - understand the layout and size of the array (e.g.,  rows, columns, etc.)
- `ndarray.shape` is crucial for reshaping arrays or performing operations that depend on array dimensions
- Shape is a tuple of integers, where the length of the tuple is the number of dimensions (ndi) of the array.
- The shape can be modified directly to reshape the array (if the total number of elements remains the same)
- Changing the shape directly will not create a new array but will modify the existing one