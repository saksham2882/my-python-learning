# string manipulation and iteration in Python

name = "Saksham"

# String with quotes
apple = """He said, "I want to eat an apple" """
# apple = '''He said, "I want to eat an apple" '''
# apple = 'He said, "I want to eat an apple" '
# apple = " He said, \"I want to eat an apple \" " 
print(apple)

# Multiline string
greeting = """
    Hey!
    Hello
    What's your name 
    My Name is """
print(greeting + name)   


# Iterate through each character in the string
print("Characters in name:")
for char in name:
    print(char)