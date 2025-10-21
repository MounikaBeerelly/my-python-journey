## Understanding the concept of Indexing and Slicing in NumPy Arrays

1. **Indexing** -
    - Indexing refers to accessing specific elements within the NumPy array
    - Indexing allows retrieving OR modifying the individual elements OR group of elements in an array
    - Indexing starts from 0, and Thereby increments by 1
    - NumPy arrays will provide `Negative Indexing` to access the elements from the end of the array
    - Basic syntax of indexing
        - `NumPyArray[indexNumber]`
2. **Slicing** -
    - Slicing allows accessing a range of elements (Also called as Sub-Array) from a NumPy array
    - Slicing is done using a colon (:) notation
    - Basic syntax of slicing
        - `NumPyArray(start:stop:step)`
            - Start: The starting index (Inclusive)
            - Stop: The ending index (Exclusive)
            - Step: The increment between indices (default is 1)