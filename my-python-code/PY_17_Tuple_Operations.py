# tuple manipulation and methods in Python

# Modify tuple by converting to list
countries = ("India", "UK", "USA", "Germany", "South Korea")
temp = list(countries)
temp.append("Russia")                        # Add item
temp.pop(1)                                  # Remove item
temp[2] = "Japan"                            # Change item

countries = tuple(temp)
print("Modified tuple:", countries)


# Concatenate tuples
countries1 = ("India", "Japan", "South Korea")
countries2 = ("China", "Thailand")
asia = countries1 + countries2
print("Concatenated tuple:", asia)


# Tuple methods
tuple1 = (0, 1, 3, 5, 3, 11, 23, 8 , 3 , 4 , 4 , 4)
print("Count of 3:", tuple1.count(3))
print("Index of 5: ", tuple1.index(5))
print("Index of 3 between indices 4 and 9:", tuple1.index(3, 4, 9))