# docstring in Python

# Docstring example
def square(n):
    '''Takes a number n and returns the square of n'''       # just below the function statement
    print(n ** 2)
square(5)
print("Docstring:", square.__doc__)


# Incorrect docstring placement (treated as a comment)
def square_wrong(n):
    print(n)
    '''This is not a docstring, just a comment'''
    print(n ** 2)
square_wrong(5)
print("Wrong docstring:", square_wrong.__doc__)              # Prints: None


# Note: PEP-8 is a style guide for Python code to ensure consistency and readability