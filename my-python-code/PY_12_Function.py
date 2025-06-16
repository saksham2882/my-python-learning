# functions in Python

# Calculate geometric mean of two numbers
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(f"Geometric mean: {mean}")


# Compare two numbers to find the greater one
def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")


# Compare two numbers to find the lesser one
def isLesser(a, b):
    if a < b:
        print("First number is lesser")
    else:
        print("Second number is lesser or equal")


# Test functions
c, d = 5, 9
isGreater(c, d)
calculateGmean(c, d)
isLesser(c, d)


def isEqual(a,b):
    pass                 # write when we want so pass it (move to other part of code)