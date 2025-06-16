# dictionaries in Python (ordered since Python 3.7)

# Define a dictionary
dic1 = {
    136: "Tom",
    137: "Kim",
    138: "Sam",
    143: "Lee"
}
print("Dictionary:", dic1)

# Access value by key
print("Value for key 143:", dic1[143])
# print("Value for key 148:", dic1[148])                        # key not exists -> show error


# Use get() to avoid KeyError
print("Value for key 143 with get():", dic1.get(143))        
print("Value for non-existent key 148:", dic1.get(148))       # key not exists -> Returns None


# Access all keys and values
print("Keys:", dic1.keys())
print("Values:", dic1.values())


# Iterate through keys
for key in dic1.keys():
    print(f"The value for key {key} is {dic1[key]}")


# Iterate through key-value pairs
print("Items:", dic1.items())
for key, value in dic1.items():
    print(f"The value for key {key} is {value}")



# common dictionary methods in Python

# dictionaries
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# Update ep1 with ep2
ep1_copy = ep1.copy()   # Avoid modifying original
ep1_copy.update(ep2)
print("After update:", ep1_copy)


# Remove specific key
ep1_copy.pop(122)
print("After pop(122):", ep1_copy)


# Remove last key-value pair
ep1_copy.popitem()
print("After popitem():", ep1_copy)


# Delete specific key
del ep1_copy[123]
print("After delete ep1_copy[123]:", ep1_copy)


# Clear dictionary
ep1_copy.clear()
print("After clear():", ep1_copy)