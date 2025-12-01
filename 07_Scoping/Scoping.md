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

### Concepts to be remembered when operating with the `Enclosing Scope` :
1. `Enclosing Scope` arises only when we are having `Nested Functions`.
2. Inner function accessing the outer function scope is `Enclosing Scope`
```
def outerFunction():
    "The local scope of the outer function begins here"

        1. Global scope of the program level
        2. Local scope of the outer function level
        3. Built-in scope of the programming language level

    def innerFunction() :
        "The local scope of the inner function begins here"
        
        1. Local scope of the inner function (first priority)
        2. Enclosing Scope of the outer functions local scope
        3. Global scope of the program level
        4. Built-in scope of the programming language level

        return
        "The local scope of the inner function ends here"

    return 
    "The local scope of the outer function ends here"
```

### What is meant by Closure ?
1. A `Closure` is the "Cobination of a function bundled together with all its references to its surrounding spaces".
2. A `Closure` is a technique for implementing "lexically scoped name binding with respect to any programming language with the concept of `First class functions`".
3. Closures are possible in Python when
    1. We have a nested function: Outer function containing the definition of the inner function
    2. The nested function refers to a variable of the outer function
    3. The enclosing function "Returns the enclosed function".