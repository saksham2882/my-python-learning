# Demonstrates anonymous (lambda) functions in Python


# A lambda function is also like an expression.
# It means we create a function as a variable and use it just like a normal function.


# Simple Function 
def double(x):
    return x*2
print(double(5))  


# Shortcut for above code: Lambda for simple operations
double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print("Double of 5:", double(5))                             # Output: 10
print("Cube of 5:", cube(5))                                 # Output: 125
print("Avg of 7,9,5:", avg(7,9,5))                           # Output: 7.0  



# Lambda as argument in higher-order function
def apply(fx, value):
    return fx(value) + 6

print("apply(cube, 5):", apply(cube, 5))                     # Output: 131
print("apply(lambda x:x*x, 5):", apply(lambda x: x*x, 5))    # Output: 31
