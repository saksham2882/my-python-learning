# string slicing in Python

name = "Saksham Agrahari"

# slicing: include start, exclude end
print("Slice [0:10]:", name[0:10])            # Prints 'Saksham Ag' ,  including 0 but not 10
print("Slice [1:10]:", name[1:10])            # Prints 'aksham Ag'


# Omitting start defaults to 0
print("Slice [:10]:", name[:10])

print("Slice [:]:", name[:])
print("Slice [0:-4]:", name[0:-4])
print("Slice [0:len - 4]:", name[0:len(name)-4])


# Negative indexing
print("Slice [-3:-1]:", name[-3:-1])         # Prints 'ar' (from 3rd last to 2nd last)
print("Slice [-1:-3]:", name[-1:-3])         # blank, nothing printing


# Length of the string
print("Length of name:", len(name))