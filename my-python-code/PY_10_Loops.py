# for loops and the range function in Python

# Iterate through a string
name = "Saksham"
for char in name:
    print(char)
    if char == "h":
        print("This is something special!")


# Iterate through a list and its elements
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for char in color:
        print(char)


# Using range with step size
for k in range(3):        
    print(k)                       #  0 - 2
    
for k in range(1 , 4):             # range goes to n-1
    print(k)                       #  1 - 3
    
for k in range(1, 12, 3):          # Starts at 1, increments by 3, stops before 12
    print(k)



######### while loops in Python  ############

# Basic while loop to count up
i = 0
while i <= 3:
    print(i)
    i += 1
print("Done")


# While loop with user input
i = int(input("Enter the number: "))
while i <= 30:
    i = int(input("Enter the Number: "))
    print(i)
print("Done")


# While loop to count down with else clause
count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside else")

# Note: Python does not have a do-while loop



#############   use of else with loops in Python    ###################

# Else executes only if the loop completes without breaking
for i in range(6):
    print(i)
else:
    print("Loop completed without breaking")


# Else does not execute if loop breaks
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("This won't print due to break")


# While loop with else
i = 0
while i < 7:
    print(i)
    i += 1
else:
    print("While loop completed without breaking")


# Example with formatted output
for x in range(5):
    print(f"Iteration no {x + 1} in for loop")
else:
    print("Else block in loop")
print("Out of loop") 
