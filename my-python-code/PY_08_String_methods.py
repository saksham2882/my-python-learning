# string methods in Python

# String are Immutable (You can not change original String)

name = "Saksham"
company = "Samsung Company is one of the largest Company. Samsung is Great."
exclamation = "!!!!Today!!!!"
heading = "introduction tO js"
message = "Welcome to the console and What is your name!!"

# Case conversion
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Swapcase:", name.swapcase())                              # convert lowercase into uppercase and vice versa


# Strip characters
print("Original:", exclamation)
print("Strip '!':", exclamation.rstrip("!"))


# Replace and split
print("Replace 'Samsung' with 'Microsoft':", company.replace("Samsung", "Microsoft"))
print("Split into list:", company.split(" "))


# Capitalize first letter
print("Capitalize:", heading.capitalize())


# string properties
print("Starts with 'Welcome':", message.startswith("Welcome"))
print("Ends with '!!':", message.endswith("!!"))
print(message.endswith("to",4,10))
print("Find 'the':", message.find("the"))                      # find first "the" in the string if element not found then show false
print(message.index("neceke"))                                 # find element in string if found give true if not then show an error
print("Count 'Samsung':", company.count("Samsung"))


# Check alphanumeric and alphabetic
print("Is message alphanumeric?:", message.isalnum())
print("Is 'Welcome' alphabetic?:", "Welcome".isalpha())                      # True


# Check case
print("Is 'hello world' lowercase?:", "hello world".islower())               # True
print("Is 'hello worldH' lowercase?:", "hello worldH".islower())             # False


# Check printable
print("Is printable?:", "I miss you a lot!!!".isprintable())                 # True
print("Is printable with newline?:", "I miss you a lot!!!\n".isprintable())  # False                      


# Check whitespace
print("Is all spaces?:", "        ".isspace())


# Title case
str1 = "His name is Dan. Dan is an honest man."
print("Title case:", str1.title())                            # convert first character of all element into Uppercase


str1 = "World Health Organization"
print(str1.istitle())                            