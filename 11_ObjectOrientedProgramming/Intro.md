### What is an Empty class in Python ?
- Empty classes are extendable
- **Basic Syntax :**
    ```
        class EmptyClass :
            pass
        
        emptyClassObject = EmptyClass() # Creating Instance of the class : object
    ```
- Print the structure of the class : `emptyClass.__dict__`
- Method always works for object of its class.
### Access Specifiers :
1. pubic
2. private 
    - Accessing pubilc attributes directly on the name of the object which is outside the class.
    - Private members of a class cannot call directly on the object of a class.
    - Without the methods, we can't call the private members
3. protected
    
### Constructor in Object Oriented Applications :
- A constructor is a special method, which is basically used to 
    1. Create an instance of the class (object)
    2. Initialize the objects of the class

- **Basic Syntax :**
    ```
    class className:
        def __init__(self) :
            constructor Body
    ```
    ```
    class className:
        def __init__(self, param01, param02, ...) :
            constructor Body
    ```

- Any variable declared at class level,  behaves as static varible