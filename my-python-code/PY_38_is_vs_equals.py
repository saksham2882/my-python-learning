# Demonstrates difference between 'is' (identity) and '==' (equality)


# "is" or "==" both are comparison operators.
# "is" compares the exact memory location of two objects.
# "==" compares the values of the objects. 

# Example 1:
l = 4
m = "4"
print("l is m:", l is m)                           # Output: False
print("l == m:", m == m)                           # Output: True


# Example 2:
x = [1, 2, 3]
y = [1, 2, 3]
print("x is y:", x is y)                           # Output: False (different objects)
print("x == y:", x == y)                           # Output: True (same content)


# Example 3:
a = 4
b = 4
print(a is b)                                      # Output: True, because both 'a' and 'b' are pointing to the same memory location. 
print(a == b)

# 4 is a value and also immutable, so it cannot be changed.
# Both give True because in Python, when we create a constant, it's stored once in memory.
# Since Python knows the constant won't change, it doesn't create a new memory location for the same value.
# Instead, it gives another name to the same memory location.


# Example 4:
p = None
q = None
print("p is None:", p is None)                     # Output: True (recommended way)
print("p is b:", p is q)                           # Output: True
print("p == b:", p == q)                           # Output: True
