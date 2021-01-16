def someFunc():
    print("SomeFunction")

someFunc()  
"""
calls func directly
"""

print(someFunc()) 
"""
calls func inside print + print executes, since nothing is returned, prints None
"""

print(someFunc) 
"""
print value of function definition, hence functions are objects
"""


def VariableFunction(*args):
    for i in args:
        print(i)
        
VariableFunction(1,2,3,4,5)
VariableFunction(1,2,"HelloWorld")
