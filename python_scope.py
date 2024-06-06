"""
- Local Scope: A variable created inside a function belongs to the local scope of the function
and can only be used inside that function.
- Global Scope: A variable created outside a function is global and can be used by anyone.
"""
# Global scope

a = 20
b = 30


# Local Scope
def function1():
    x = 10
    print(x)
    print(a)  # use of global scope


function1()

# Global Keyword

num1 = 50


def function2():
    global num1
    num1 = 90
    print(num1)


function2()
