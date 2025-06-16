# lists and list comprehension in Python

# List is mutable and we store different datatype value in it

# list with mixed data types
marks = [3, 5, 6, "Saksham", True, 52, 65, 64, 45, 5454]
print(marks)


# Slicing examples
print("Slice [1:-1]:", marks[1:-1])
print("Slice [1:4]:", marks[1:4])
print("Slice [1:8:2]:", marks[1:8:2])


# Check if element exists
if "Saksham" in marks:
    print("Yes, 'Saksham' is in the list")


if 6 in marks:
    print("Yes")
else:
    print("No")    


if "6" in marks:
    print("Yes")
else:
    print("No")    


if "sham" in "Saksham":
    print("Yes")


# List comprehension
lst = [i for i in range(4)]                        # List of numbers 0 to 3
lst1 = [i * i for i in range(4)]                   # List of squares
lst2 = [i * i for i in range(4) if i % 2 == 0]     # List of even squares
print("List:", lst)
print("Squares:", lst1)
print("Even squares:", lst2)