# different types of function arguments in Python

# There are four type of arguments:
#     1. Default argument:
#     2. Keyword arguments
#     3. variable length arguments
#     4. required arguments


# 1. Default arguments: Uses default values if not provided
def average(a=4, b=5):
    print(f"The average is {(a + b) / 2}")
average()  
average(9)
average(b = 9)
average(6)
average(a = 16)

def name(fname , mname = "Saksham", lname = "Agrahari"):
    print("Hello, ", fname , mname , lname)
name("Mr." , "gupta")    


# 2. Keyword arguments: Pass arguments in any order using parameter names
average(b=45, a=6)


# 3. Required arguments: Must provide values if no default exists
def avg(a, b, c=8):
    print(f"The average is {(a + b + c) / 3}")
avg(5, 6)    


# 4. Variable-length arguments: Accepts any number of arguments as a tuple
def average(*numbers):
    sum_nums = sum(numbers)
    print(f"The average is {sum_nums / len(numbers)}")
    # return          # always first return print it print none
    # return 7        # it return 7
    return sum_nums / len(numbers)

result = average(5, 6, 7, 8)
print(f"Returned average: {result}")


def name(**name):
    print(type(name))   # dictionary
    print("Hello , " , name["fname"], name["mname"], name["lname"])
name(mname = "kumar", lname = "Gupta", fname = "Mohan")    