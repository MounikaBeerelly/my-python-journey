### Pre-requisites for creating Packages :

- `STEP 01 : Creating the directory structure`
1. Create the below directory structure in the operating system
        - C:\Practice\my-python-journey\13_Packages\Packages001\Greetings
- `STEP 02 : Create an Empty __init__.py file`
1. Open any text editor and save the EmptyFile, with a name **__init__.py** in the "C:\Practice\my-python-journey\13_Packages\Packages001\Greetings" path.
- `STEP 03 : Create the required package file`
1. Open any text editor and creates a file with the name : **Greetings.py**, in "C:\Practice\my-python-journey\13_Packages\Packages001\Greetings" path.
2. Type the following code
    ```
        def greetingsFunc() :
            #This function just greets end user
            print("\nHai! Welcome to the world of Python packages", end="\n)
            print("\nPAckages are modules that can be shared among different Python applications", end="\n)
            print("\nPackages are external Python files containing Re-usable applications code", end="\n)
            return
    ```
3. Save and close the file
- `STEP 04 : Creating the Operational module`
1. Open any text editor and create a file with name : **Scripts.py** in "C:\Practice\my-python-journey\13_Packages\Packages001" path.
2. Type the following code
    ```
        import os
        os.system("cls")

        from Greetings import Greetings

        print("\nIllustration of the Packages", end="\n")
        print("---------------oOo-------------", end="\n")

        Greetings.greetingsFunc()
        print("\nReturned from the PAckage, After completing the function..", end="\n")

    ```
- `STEP 05 : Execute the program`
1. Once the execution is completed a `__pycache__` directory is automatically created
2. `__pycache__` directory contains the **cpython files**.