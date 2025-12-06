### Understanding NameError in Python :
1. NameError is raised when a local OR Global Name is not found in the "Execution Module"
2. The name can be any identifier in Pythons currently running application like
    1. Variable Name
    2. Function Name
    3. Modulr Name
    4. Package Name
3. We can even raise the NameError explicitly, when needed by using
    - **Syntax** :
        ```
        raise NameError("Required Message")
        ```
### Understanding the `traceback` module in Python :
1. The `Traceback` module in Python is a "Built-in" module.
2. The `traceback` module provides functions for handling "Stack Traces" of the Python programs for
    1. Extarcting
    2. Formatting
    3. Printing

### What is the order that has to be followed when operating with Files ?
1. Any file operation will be implemented with a standardized order followed as 
    1. File Opening
        1. This step will creates a file handle OR file pointer that points to the physical location of the file in the computer storage device
        2. This step actually confirms the mode in which the file will be operated
            - **File operational Modes**
                1. Read only mode : `r`
                2. Write only mode : `w`
                3. Append mode : `a`
                4. Exclusive creation mode : `x`
            - **File Type Modes**
                1. Text Mode : `t`
                2. Binary mode : `b`
            - **Basic Syntax to Open a file**
                ```
                fileHandle = open("SampleData.txt")
                fileHandle = open("C:\myData\SampleData.txt")
                fileHandle = open("C:\myData\SampleData.txt", 'w')
                fileHandle = open("C:\myData\SampleData.txt", 'r+b')
                fileHandle = open("C:\myData\SampleData.txt", mode = 'r', encoding = 'utf-8)
                ```
2. File Read and write operations
3. File Closing
    ```
    fileHandle.close()
    ```