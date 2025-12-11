
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

### Example for Writing Data :
   ```
   myFileHandle = open("C://Practice//my-python-journey//10_File Operations//OutData/ex01.dat", mode = "w", encoding = "cp1252")
   ```
   - `open` - Function to open the required file
   - `path` 
        - The total file name should be provided with full path
        - The path seperator should be "Two forward slashes"
        - File name can be with any extension
        - The file name including path should be in double/single quotes
   - `mode` - The mode in which the file will be operated, and throughout the program the file will be operate only in the specified mode. So this mmode we have permissions in the Operating system
   - `encoding` - This defines the code page in which the data willbe written OR read
   - `myFileHandle` - This variable is called as "File Pointer OR Reference to a file", where the file reference is retirned by the ope() function
   - `mode = 'w'` 
      - Creates a new file with given name, if the file is not existing. 
      - If the file is existing then opens the file and keeping the file pointer at the beginning of the file.
      - Existing data will be override

### Understanding `with open()~ function in Python :
1. `with open()` function is used as an alternate for opening the files in Python.
2. `with open()` is built-in functionality, with several advantages specially in terms of Readability, and ensures that the resources are properly managed.
3. `with open()` simplifies the "File handling" mechanism by "Managing the opening and closing of the files automatically".

### Working with Random files concept in Python :
1. Random files will allow reading and writing of the data at Random locations "Allowing the end user to access different parts of the file without reading it sequentially".
2. tell() function OR Method
    1. The `tell()` function returns the "Current position of the file pointer", that is fixed by the "seek()" function.
    2. The `tell()` function returns the value of the file pointer in Bytes "from the beginning of the file".
3. seek() Method OR Function
    1. To move the file pointer to the desired location, we use `seek()` function.
    2. The seek() function will take
        1. The required offset as one of the parameter to move the file pointer by number of bytes.
        2. The position from where the file pointer should be moved.
    - **Basic Syntax :** 

        ```
            seek(offsetInBytes, whence = 0)

            => whence = 0 : 
                - Which is default, and is beginning of the file
            => whence = 1 : 
                - It represents the "current position"
                - In this case, the file pointer can move in both forward direction as well as backward direction.
            => whence = 2 : 
                - It rrepresents the end of the file
                - In this case, the file pointer can move only in backward direction
        ```

### Handling PDF files using Python :
1. Python provides various different libraries for handling PDF files.
2. All PDF libraries will allow the Python programmer to progrmmatically
    1. Read the PDF files
    2. Manipulate the PDF files
    3. Create the PDF files
3. Python is supported with different libraries for handling PDF files
    1. PyPDF2
    2. ReportLab
    3. PDFMiner.six
    4. PikePDF