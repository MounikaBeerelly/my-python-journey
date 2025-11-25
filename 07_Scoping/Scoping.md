### What is Scoping in Python ?
1. Any Identifier declared in python application can only be accessed in the area to which it is defined, this concept is called as Scope.
2. Once the scope of the identifier is lost then that identifier is no more available in the operational memory of the application, hence it is lost from the applications memory.
3. Within the same scope two identifiers cannot have the same name.
4. In Python the scope of the identifier is managed by a concept of rule called as `LEGB` rule.
5. All the python identifiers resolve the names in operational process in run time by using the LEGB rule, where LEGB stands for
    - `L` : Local, Functional scope
    - `E` : Enclosing, Non-local scope
    - `G` : Global, Module scope
    - `B` : Built-in, Programming language level
6. When a Python program is in execution the order of search for finalizing the scope of the identifier is executed in the order of `local -> Enclosing -> Global -> Built-in`

#### Note:
1. All the operations that are as part of the functions definition are considered to be in local scope of the function.
2. Local scope is visible only when the function is called.