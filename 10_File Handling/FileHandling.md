
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