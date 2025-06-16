# conditional statements in Python

# Simple if-else to check age
age = int(input("Enter your Age: "))
print("Your Age is:", age)

if age > 18:
    print("Yes, you can drive")
else:
    print("No, you cannot drive")
print("Print Outside if-else..")


# Nested if-elif-else
num = int(input("Enter your Number: "))
if num < 0:
    print("Number is Negative")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



# Exercise:- Greets the user based on the current time of day
import time

# Get current time in human-readable format
present_time = time.strftime("%c")
print("Current time:", present_time)

# Get current hour (24-hour format)
hour = int(time.strftime("%H"))

# Greet based on time of day
if 0 <= hour < 12:
    print("Good Morning Sir")
elif 12 <= hour < 16:
    print("Good Afternoon Sir")  
elif 16 <= hour < 20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")



# use of Python's match statement for pattern matching
x = int(input("Enter the value of x: "))

# Match statement to check the value of x
match x:
    case 0: 
        print("x is zero")
    case 4: 
        print("x is 4")
    
    # case with if-condition
    case _ if x!=50:              # This is default if case
        print(x , "is not 50")
    case _ if x!=80:              # This is default if case
        print(x , "is not 80")
    case _:                       # This is default case
        print(x)                  # Default case for all other values




# Ternary operator in Python for concise if-else statements

a = 3304646
b = 4662

# Ternary operator: Print based on comparison
print("A") if a > b else print("=") if a == b else print("B")

# Ternary with empty else
print(9) if a > b else ""

# Assign value using ternary
c = 9 if a > b else 0
print("Assigned value:", c)

# Syntax: value_if_true if condition else value_if_false