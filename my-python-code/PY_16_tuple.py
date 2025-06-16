# tuples and their immutability in Python
# list  -> []
# tuple -> ()

# tuple with mixed data types
tup = (1, 2, 6, "saksham", True)
print("Type:", type(tup), "Tuple:", tup)    # This print class tuple


# Single element tuple requires a comma
tup_single = (1,)
print("Single element tuple:", tup_single)


tup2 = (1)                                  # This print class int
print(type(tup2) , tup2)


# tup = (1 , 2 , 5 , 655 ,9)  
# tup[0] = 60                               # tuple value does not changed in the  original tuple (this show an error)
# print(type(tup) , tup)


# Check if element exists
if "saksham" in tup:
    print("Yes, 'saksham' is in the tuple")

if 6 in tup:
    print("Yes")
    
if "6" in tup:
    print("Yes")
else:
    print("No")


# Tuple slicing creates a new tuple
tup2 = tup[1:4]
print("Sliced tuple:", tup2)

# Note: Tuples are immutable; cannot change elements directly