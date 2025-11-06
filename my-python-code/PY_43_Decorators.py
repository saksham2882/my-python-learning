# Demonstrates function decorators to modify behavior


# Decorators are functions that modify another function and return it.
# A decorator changes the behavior of a function without altering its actual code.

# syntax:- @decorators_function
#          def my_function():    
#              pass


# Example 1:
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx    

@greet                                                      # This is a decorator (and it is enhancing or modifying the 'hello' function).
def hello():
    print("Hello World")

# greet(hello)()                                            # Do the same thing manually by calling the decorator function directly. (But first, comment out the @greet line above.)
hello()     



# Example 2:
def greet(fx):
    def wrapper(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return wrapper

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a + b)


hello()
# Output:
# Good Morning
# Hello World
# Thanks for using this function

add(5, 9)
# Output:
# Good Morning
# 14
# Thanks for using this function


# another way
# greet(hello)()                     
# greet(add)(1,2)      