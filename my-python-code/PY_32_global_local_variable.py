# Demonstrates global and local variable scope in Python

# Define a global variable
a = 10
print("Global a before function:", a)


def my_function():
    b = 56           # Local Variable
    print(b)

my_function()    
print(a)
# print(b)           # This will cause an error because 'b is a local variable and is not accessible outside of the function



# If we wants to change the global variable inside the function then :-
def my_function():
    global a          # Modify the global variable
    a = 1651
    b = 56            # Local variable
    print("Local b:", b)
    print("Global 'a' inside function:", a)           # Output: 1651

my_function()    
print("Global 'a' after function:", a)                # Output: 1651


# Note: b is not accessible here as it's local