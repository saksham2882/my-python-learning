# sets in Python: unordered, unique collections of items

# Set is a unordered collection of well defined data items.
# set value can not be changed or replaced one's set formed

# Create a set (duplicates are automatically removed)
s = {2, 4, 2, 6, 5, 2, 6}
print("Set with duplicates removed:", s)
print("Type:", type(s))


# Set with mixed data types
info = {"Nick", 19, False, 5.96, 19, "Nick"}
print("Mixed set:", info)


saksham = { }                            # empty dictionary
print(type(saksham))


# empty set (not a dictionary)
empty_set = set()
print("Empty set:", empty_set, "Type:", type(empty_set))


# Iterate through set items
print("Items in info set:")
for value in info:
    print(value)