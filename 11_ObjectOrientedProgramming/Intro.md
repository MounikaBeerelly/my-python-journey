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
    - Public members of a class can be directly called upon the object of the class using `.` operator.
2. private 
    - Private members of a class can be used only within the class, hence cannot be  directly called on the object of the class.
    - To access the private members of the class we definitely need public method in the class.
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

### Destructor in Python :
- Called when the reference to the object is about to close.
- `def __del__(self) :`

### Inheritance : 
- Passing another class as parameter to the class
1. Single Inheritance :
    - `Message Passing` : To access the private members of the Base Class from the Derived class, we have to pass the message to the Base Class public methods, from the Derived Class public methods definition.
    - All the public members of the Base Class will become publicmembers of the Derived Class.
2. Multi-level Inheritance
3. Hierarchical Inheritance : One parent - two childs
4. Multiple Inheritance : two parents - one child