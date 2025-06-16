# common list methods in Python

# Define a list
l = [45, 154, 656, 1, 2, 3, 6, 1]
print("Original list:", l)


# Append an element
l.append(7)
print("After append(7):", l)


# Sort in ascending order
l.sort()
print("After sort():", l)


# Sort in descending order
l.sort(reverse=True)
print("After sort(reverse=True):", l)


# Reverse the list
l.reverse()
print("After reverse():", l)


# Get index of first occurrence
print("Index of 1:", l.index(1))


# Count occurrences
print("Count of 1:", l.count(1))


# Copy the list
m = l.copy()
m[0] = 0
print("Copied and modified list:", m)


# Insert at index
l.insert(1, 899)
print("After insert(1, 899):", l)


# Concatenate lists
m = [900, 456, 56]
# l.extend(m)                        # changes original list
k = l + m                            # not changes original list
print("Concatenated list:", k)