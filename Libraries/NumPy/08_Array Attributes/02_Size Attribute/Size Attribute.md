## Understanding `ndarray.size` attribute:

- The size attribute of a NumPy array provides the total number of elements in the array.
- The size attribute is particularly useful when you need to know how many elements are stored in the array, regardless of its shape or dimensionality.
- The size attribute returns the product of the dimensions of the array, which is equivalent to the total count of all elements in the array.
- The size attribute is a read-only attribute, and works on arrays of any dimensionality, an empty array returns the size as 0.
- When we want to calculate the total memory usage of an array, then combine size with itemsize.
    - `total Memory (Bytes) = size * itemsize`
    