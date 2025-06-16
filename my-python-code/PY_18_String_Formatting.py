# string formatting in Python

# Using .format()
letter = "Hey my name is {} and I am from {}"
letter1 = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Saksham"
print(letter.format(name, country))                             # Positional arguments
print(letter1.format(country, country))                         # Indexed arguments


# Using f-strings
print(f"Hey my name is {name} and I am from {country}")         # f-string interpolation


# Formatting numbers
price = 49.3265
txt = f"For only {price:.2f} Rupee!"                            # Two decimal places
print(txt)


# Escaping f-strings
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


# Expression in f-strings
print(f"Result: {2 * 30}")