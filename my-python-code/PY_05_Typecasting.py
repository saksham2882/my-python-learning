# implicit and explicit typecasting in Python

# Integer addition
num1 = 1
num2 = 2
print("Integer addition:", num1 + num2)

# String concatenation
str1 = "1"
str2 = "2"
print("String concatenation:", str1 + str2)

name1 = "Saksham"
name2 = " Agrahari"
print("Name concatenation:", name1 + name2)


# Implicit typecasting (float + integer = float)
float_num = 1.9
int_num = 8
print("Implicit typecasting (float + int):", float_num + int_num)


# Explicit typecasting (string to integer)
print("Explicit typecasting (string to int):", int(str1) + int(str2))


# Note: Converting non-numeric strings to integers will raise a ValueError
# Example: int(name1) + int(name2) would fail because "Saksham" and " Agrahari" are not numeric