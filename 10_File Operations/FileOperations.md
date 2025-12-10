
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

